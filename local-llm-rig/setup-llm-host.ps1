<#
.SYNOPSIS
    Prepares a Windows 10 desktop to act as an always-on local LLM inference host.

.DESCRIPTION
    Audits the GPU, graphics driver, Vulkan runtime, power settings, firewall and
    Tailscale, then reports what is ready and what is not.

    By default the script only INSPECTS and reports. Nothing is changed unless
    -Apply is passed. This is deliberate: the changes touch power management and
    the Windows Firewall, and you should see the plan before it runs.

.PARAMETER Apply
    Actually perform the changes (power plan + firewall rule). Requires Administrator.

.PARAMETER Port
    TCP port the inference server listens on. Defaults to 1234 (LM Studio's default).
    Use 11434 if you run Ollama instead.

.EXAMPLE
    .\setup-llm-host.ps1
    Audit only. Safe to run any time.

.EXAMPLE
    .\setup-llm-host.ps1 -Apply
    Audit, then apply the power and firewall changes. Run from an elevated PowerShell.

.NOTES
    Target: Windows 10, AMD Radeon RX 5600 XT (RDNA1, 6 GB VRAM).
    RDNA1 is not supported by ROCm on Windows, so the inference path here is Vulkan.
#>

[CmdletBinding()]
param(
    [switch]$Apply,
    [ValidateRange(1, 65535)]
    [int]$Port = 1234
)

$ErrorActionPreference = 'Stop'

# Findings are collected as we go and printed as one summary at the end, so the
# user gets a verdict rather than having to read the whole transcript.
$script:Findings = @()

function Add-Finding {
    param(
        [Parameter(Mandatory)][ValidateSet('OK', 'WARN', 'FAIL', 'INFO')][string]$Level,
        [Parameter(Mandatory)][string]$Message
    )
    $script:Findings += [pscustomobject]@{ Level = $Level; Message = $Message }

    $color = switch ($Level) {
        'OK'   { 'Green' }
        'WARN' { 'Yellow' }
        'FAIL' { 'Red' }
        default { 'Gray' }
    }
    Write-Host ("  [{0,-4}] {1}" -f $Level, $Message) -ForegroundColor $color
}

function Write-Section {
    param([Parameter(Mandatory)][string]$Title)
    Write-Host ''
    Write-Host $Title -ForegroundColor Cyan
    Write-Host ('-' * $Title.Length) -ForegroundColor DarkGray
}

function Test-Admin {
    $identity = [Security.Principal.WindowsIdentity]::GetCurrent()
    $principal = New-Object Security.Principal.WindowsPrincipal($identity)
    return $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
}

$isAdmin = Test-Admin

Write-Host ''
Write-Host '=== Local LLM host setup ===' -ForegroundColor White
Write-Host ("Mode: {0}" -f $(if ($Apply) { 'APPLY (changes will be made)' } else { 'AUDIT ONLY (no changes)' })) -ForegroundColor White
Write-Host ("Port: {0}" -f $Port) -ForegroundColor White

if ($Apply -and -not $isAdmin) {
    Write-Host ''
    Write-Host 'ERROR: -Apply requires Administrator. Re-open PowerShell as admin and run again.' -ForegroundColor Red
    exit 1
}

# --- GPU -------------------------------------------------------------------
# Win32_VideoController.AdapterRAM is a signed 32-bit field and wraps at 4 GB,
# so a 6 GB card misreports as ~4 GB. The driver registry key holds the real
# value as a 64-bit qword.
Write-Section 'GPU'

$gpus = @(Get-CimInstance Win32_VideoController -ErrorAction SilentlyContinue)

if (-not $gpus) {
    Add-Finding FAIL 'No display adapter reported by WMI.'
} else {
    foreach ($gpu in $gpus) {
        $vramBytes = $null
        $classRoot = 'HKLM:\SYSTEM\CurrentControlSet\Control\Class\{4d36e968-e325-11ce-bfc1-08002be10318}'

        # Match the adapter to its driver key by description to read the true VRAM size.
        $subkeys = Get-ChildItem $classRoot -ErrorAction SilentlyContinue |
                   Where-Object { $_.PSChildName -match '^\d{4}$' }
        foreach ($key in $subkeys) {
            $props = Get-ItemProperty $key.PSPath -ErrorAction SilentlyContinue
            if ($props.DriverDesc -eq $gpu.Name -and $props.'HardwareInformation.qwMemorySize') {
                $vramBytes = [uint64]$props.'HardwareInformation.qwMemorySize'
                break
            }
        }

        if ($null -eq $vramBytes -and $gpu.AdapterRAM) {
            $vramBytes = [uint64]$gpu.AdapterRAM
        }

        $vramGB = if ($vramBytes) { [math]::Round($vramBytes / 1GB, 1) } else { 0 }

        Add-Finding INFO ("Adapter : {0}" -f $gpu.Name)
        Add-Finding INFO ("VRAM    : {0} GB" -f $vramGB)
        Add-Finding INFO ("Driver  : {0} ({1})" -f $gpu.DriverVersion, $gpu.DriverDate)

        # Driver age matters more than version number here: Vulkan on RDNA1 got
        # materially better over successive Adrenalin releases.
        if ($gpu.DriverDate) {
            $ageDays = (New-TimeSpan -Start $gpu.DriverDate -End (Get-Date)).Days
            if ($ageDays -gt 365) {
                Add-Finding WARN ("Graphics driver is {0} days old. Update AMD Adrenalin before troubleshooting Vulkan." -f $ageDays)
            } else {
                Add-Finding OK ("Graphics driver is {0} days old." -f $ageDays)
            }
        }

        if ($vramGB -gt 0 -and $vramGB -lt 8) {
            Add-Finding WARN ("{0} GB VRAM fits 7B-8B models at Q4 with a reduced context window. 13B and larger will spill to system RAM and crawl." -f $vramGB)
        }
    }
}

# --- Vulkan ----------------------------------------------------------------
# ROCm has no RDNA1 support on Windows, so Vulkan is the inference backend.
Write-Section 'Vulkan runtime'

$vulkanDll = Join-Path $env:SystemRoot 'System32\vulkan-1.dll'
if (Test-Path $vulkanDll) {
    $v = (Get-Item $vulkanDll).VersionInfo.FileVersion
    Add-Finding OK ("vulkan-1.dll present (version {0})." -f $v)
} else {
    Add-Finding FAIL 'vulkan-1.dll not found. Install/repair the AMD Adrenalin driver - it ships the Vulkan runtime.'
}

$vulkanInfo = Get-Command vulkaninfo -ErrorAction SilentlyContinue
if ($vulkanInfo) {
    Add-Finding INFO 'vulkaninfo is on PATH. Run "vulkaninfo --summary" to list the devices Vulkan actually sees.'
} else {
    Add-Finding INFO 'vulkaninfo not on PATH (optional - it ships with the Vulkan SDK, not the driver).'
}

# --- Power -----------------------------------------------------------------
# An always-on host that sleeps is not always-on. Display sleep is fine and is
# left alone; only system sleep and disk spindown are disabled.
Write-Section 'Power settings'

function Get-PowerSetting {
    param([string]$SubGroup, [string]$Setting)
    $raw = powercfg /query SCHEME_CURRENT $SubGroup $Setting 2>$null
    if (-not $raw) { return $null }
    $line = $raw | Select-String 'Current AC Power Setting Index:'
    if (-not $line) { return $null }
    return [Convert]::ToInt32(($line.ToString() -split ':')[-1].Trim(), 16)
}

# SUB_SLEEP / STANDBYIDLE, SUB_DISK / DISKIDLE - well-known power GUID aliases.
$sleepIdle = Get-PowerSetting 'SUB_SLEEP' 'STANDBYIDLE'
$diskIdle  = Get-PowerSetting 'SUB_DISK'  'DISKIDLE'

if ($null -ne $sleepIdle) {
    if ($sleepIdle -eq 0) {
        Add-Finding OK 'System sleep on AC is already disabled.'
    } else {
        Add-Finding WARN ("System sleeps after {0} minutes on AC. The inference server dies with it." -f ($sleepIdle / 60))
    }
}
if ($null -ne $diskIdle -and $diskIdle -ne 0) {
    Add-Finding WARN ("Disk spins down after {0} minutes on AC. This stalls model loading." -f ($diskIdle / 60))
}

if ($Apply) {
    powercfg /change standby-timeout-ac 0 | Out-Null
    powercfg /change hibernate-timeout-ac 0 | Out-Null
    powercfg /change disk-timeout-ac 0 | Out-Null
    Add-Finding OK 'Applied: system sleep, hibernate and disk timeout disabled on AC.'
    Add-Finding INFO 'Display sleep left unchanged - the screen may still turn off, which is harmless.'
} elseif (($sleepIdle -and $sleepIdle -ne 0) -or ($diskIdle -and $diskIdle -ne 0)) {
    Add-Finding INFO 'Re-run with -Apply to disable sleep and disk timeout.'
}

# --- Firewall --------------------------------------------------------------
# Scoped to private networks so the port is not exposed if the machine ever
# lands on a public Wi-Fi profile.
Write-Section 'Firewall'

$ruleName = "Local LLM inference server (TCP $Port)"
$existing = Get-NetFirewallRule -DisplayName $ruleName -ErrorAction SilentlyContinue

if ($existing) {
    Add-Finding OK ("Firewall rule already present: '{0}' (Enabled={1})." -f $ruleName, $existing.Enabled)
} elseif ($Apply) {
    New-NetFirewallRule -DisplayName $ruleName `
                        -Direction Inbound `
                        -Action Allow `
                        -Protocol TCP `
                        -LocalPort $Port `
                        -Profile Private `
                        -Description 'Allows the laptop to reach the local LLM server over the private/Tailscale network.' | Out-Null
    Add-Finding OK ("Applied: created inbound rule for TCP {0} on private networks." -f $Port)
} else {
    Add-Finding WARN ("No firewall rule for TCP {0}. The laptop will not be able to connect. Re-run with -Apply." -f $Port)
}

# --- Tailscale -------------------------------------------------------------
Write-Section 'Tailscale'

$tailscaleExe = Get-Command tailscale -ErrorAction SilentlyContinue
if (-not $tailscaleExe) {
    $candidate = Join-Path $env:ProgramFiles 'Tailscale\tailscale.exe'
    if (Test-Path $candidate) { $tailscaleExe = Get-Item $candidate }
}

if ($tailscaleExe) {
    Add-Finding OK ("Tailscale installed at {0}." -f $tailscaleExe.Source)
    try {
        $ip = & $tailscaleExe.Source ip -4 2>$null | Select-Object -First 1
        if ($ip) {
            Add-Finding OK ("Tailscale IPv4: {0}" -f $ip)
            Add-Finding INFO ("From the laptop: curl http://{0}:{1}/v1/models" -f $ip, $Port)
        } else {
            Add-Finding WARN 'Tailscale is installed but not connected. Run: tailscale up'
        }
    } catch {
        Add-Finding WARN 'Tailscale is installed but its status could not be read. Run: tailscale status'
    }
} else {
    Add-Finding WARN 'Tailscale not found. Install from https://tailscale.com/download and sign in on BOTH machines.'
}

# --- Listener --------------------------------------------------------------
Write-Section 'Inference server'

$listener = Get-NetTCPConnection -State Listen -LocalPort $Port -ErrorAction SilentlyContinue |
            Select-Object -First 1

if ($listener) {
    $proc = Get-Process -Id $listener.OwningProcess -ErrorAction SilentlyContinue
    Add-Finding OK ("Something is listening on port {0} ({1})." -f $Port, $(if ($proc) { $proc.ProcessName } else { "PID $($listener.OwningProcess)" }))

    if ($listener.LocalAddress -in @('0.0.0.0', '::')) {
        Add-Finding OK 'Bound to all interfaces - reachable from the laptop.'
    } else {
        Add-Finding WARN ("Bound to {0} only. Enable 'Serve on Local Network' in LM Studio, or the laptop cannot reach it." -f $listener.LocalAddress)
    }
} else {
    Add-Finding INFO ("Nothing listening on port {0} yet. Start the server in LM Studio (Developer tab)." -f $Port)
}

# --- Summary ---------------------------------------------------------------
Write-Section 'Summary'

$fails = @($script:Findings | Where-Object Level -eq 'FAIL')
$warns = @($script:Findings | Where-Object Level -eq 'WARN')

Write-Host ("  {0} OK  /  {1} warnings  /  {2} failures" -f
    @($script:Findings | Where-Object Level -eq 'OK').Count, $warns.Count, $fails.Count)

if ($fails) {
    Write-Host ''
    Write-Host '  Blocking issues:' -ForegroundColor Red
    $fails | ForEach-Object { Write-Host ("   - {0}" -f $_.Message) -ForegroundColor Red }
}
if ($warns) {
    Write-Host ''
    Write-Host '  Needs attention:' -ForegroundColor Yellow
    $warns | ForEach-Object { Write-Host ("   - {0}" -f $_.Message) -ForegroundColor Yellow }
}

if (-not $Apply -and ($fails -or $warns)) {
    Write-Host ''
    Write-Host '  Run again with -Apply (as Administrator) to fix the power and firewall items.' -ForegroundColor White
}

Write-Host ''
exit $(if ($fails) { 1 } else { 0 })
