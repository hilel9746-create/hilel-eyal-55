<#
.SYNOPSIS
    Turns the always-on Windows 10 desktop into an SSH server the laptop can drive.

.DESCRIPTION
    Installs the Windows OpenSSH Server feature, starts it, sets PowerShell as the
    default remote shell, opens the firewall, and installs a public key for
    key-based login.

    Like setup-llm-host.ps1 this only INSPECTS by default. Pass -Apply to make
    changes. Requires Administrator when applying.

    Order matters: get key login working FIRST, verify it from the laptop, and
    only then run -DisablePasswordAuth. Doing it in the other order can lock you
    out of a machine you are not sitting in front of.

.PARAMETER Apply
    Perform the installation and configuration. Requires Administrator.

.PARAMETER PublicKey
    The contents of the laptop's public key (the single line from id_ed25519.pub).
    Installed into the correct authorized_keys file for this account type.

.PARAMETER DisablePasswordAuth
    Turn off password authentication, leaving key-only login. Run this ONLY after
    you have confirmed key login works from the laptop.

.EXAMPLE
    .\enable-ssh-server.ps1
    Report current SSH state. Changes nothing.

.EXAMPLE
    .\enable-ssh-server.ps1 -Apply -PublicKey "ssh-ed25519 AAAAC3Nza... hillel@laptop"
    Install and configure the server, and authorise that key.

.EXAMPLE
    .\enable-ssh-server.ps1 -Apply -DisablePasswordAuth
    Harden to key-only. Only after key login is verified.
#>

[CmdletBinding()]
param(
    [switch]$Apply,
    [string]$PublicKey,
    [switch]$DisablePasswordAuth
)

$ErrorActionPreference = 'Stop'

function Write-Section {
    param([string]$Title)
    Write-Host ''
    Write-Host $Title -ForegroundColor Cyan
    Write-Host ('-' * $Title.Length) -ForegroundColor DarkGray
}

function Say {
    param(
        [ValidateSet('OK', 'WARN', 'FAIL', 'INFO')][string]$Level,
        [string]$Message
    )
    $color = switch ($Level) { 'OK' {'Green'} 'WARN' {'Yellow'} 'FAIL' {'Red'} default {'Gray'} }
    Write-Host ("  [{0,-4}] {1}" -f $Level, $Message) -ForegroundColor $color
}

$isAdmin = ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()
           ).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

Write-Host ''
Write-Host '=== SSH server setup ===' -ForegroundColor White
Write-Host ("Mode: {0}" -f $(if ($Apply) { 'APPLY' } else { 'AUDIT ONLY' })) -ForegroundColor White

if ($Apply -and -not $isAdmin) {
    Write-Host ''
    Write-Host 'ERROR: -Apply requires Administrator. Re-open PowerShell as admin.' -ForegroundColor Red
    exit 1
}

# --- Feature ---------------------------------------------------------------
Write-Section 'OpenSSH Server feature'

$capability = Get-WindowsCapability -Online -Name 'OpenSSH.Server*' -ErrorAction SilentlyContinue |
              Select-Object -First 1

if (-not $capability) {
    Say FAIL 'OpenSSH.Server capability not offered by this Windows build.'
} elseif ($capability.State -eq 'Installed') {
    Say OK 'OpenSSH Server is installed.'
} elseif ($Apply) {
    Say INFO 'Installing OpenSSH Server (this downloads from Windows Update, give it a minute)...'
    Add-WindowsCapability -Online -Name $capability.Name | Out-Null
    Say OK 'OpenSSH Server installed.'
} else {
    Say WARN 'OpenSSH Server is NOT installed. Re-run with -Apply.'
}

# --- Service ---------------------------------------------------------------
Write-Section 'sshd service'

$sshd = Get-Service sshd -ErrorAction SilentlyContinue

if (-not $sshd) {
    Say WARN 'sshd service not present yet (expected if the feature was just installed in audit mode).'
} else {
    Say INFO ("Status: {0}, StartType: {1}" -f $sshd.Status, $sshd.StartType)

    if ($Apply) {
        # Automatic start is the whole point: the box must serve after a reboot
        # without anyone logging in.
        Set-Service sshd -StartupType Automatic
        if ($sshd.Status -ne 'Running') { Start-Service sshd }
        Say OK 'sshd set to start automatically and is running.'

        # ssh-agent is optional on the server side but harmless and useful if you
        # ever hop onward from this machine.
        Set-Service ssh-agent -StartupType Automatic -ErrorAction SilentlyContinue
    } else {
        if ($sshd.StartType -ne 'Automatic') { Say WARN 'Start type is not Automatic - it will not come back after a reboot.' }
        if ($sshd.Status -ne 'Running')      { Say WARN 'Service is not running.' }
    }
}

# --- Default shell ---------------------------------------------------------
# Without this the remote shell is cmd.exe, which makes every PowerShell command
# from the laptop need awkward quoting.
Write-Section 'Default remote shell'

$sshRegPath = 'HKLM:\SOFTWARE\OpenSSH'
$currentShell = (Get-ItemProperty $sshRegPath -Name DefaultShell -ErrorAction SilentlyContinue).DefaultShell

if ($currentShell) {
    Say OK ("Default shell: {0}" -f $currentShell)
} elseif ($Apply) {
    $pwshPath = "$env:SystemRoot\System32\WindowsPowerShell\v1.0\powershell.exe"
    if (-not (Test-Path $sshRegPath)) { New-Item -Path $sshRegPath -Force | Out-Null }
    New-ItemProperty -Path $sshRegPath -Name DefaultShell -Value $pwshPath -PropertyType String -Force | Out-Null
    Say OK "Default shell set to PowerShell."
} else {
    Say WARN 'Default shell is cmd.exe. Re-run with -Apply to switch to PowerShell.'
}

# --- Firewall --------------------------------------------------------------
Write-Section 'Firewall'

$sshRule = Get-NetFirewallRule -Name 'OpenSSH-Server-In-TCP' -ErrorAction SilentlyContinue

if ($sshRule) {
    Say OK ("Rule 'OpenSSH-Server-In-TCP' present (Enabled={0})." -f $sshRule.Enabled)
} elseif ($Apply) {
    New-NetFirewallRule -Name 'OpenSSH-Server-In-TCP' `
                        -DisplayName 'OpenSSH Server (sshd)' `
                        -Direction Inbound -Action Allow `
                        -Protocol TCP -LocalPort 22 `
                        -Profile Private | Out-Null
    Say OK 'Created inbound rule for TCP 22 on private networks.'
} else {
    Say WARN 'No firewall rule for TCP 22.'
}

# --- Public key ------------------------------------------------------------
# Windows OpenSSH has a trap here: for accounts in the Administrators group it
# ignores ~/.ssh/authorized_keys and reads a single shared file instead, which
# must have inheritance stripped and be writable only by Administrators and
# SYSTEM. Getting the ACL wrong makes sshd silently refuse the key.
Write-Section 'Authorized keys'

$userIsAdmin = ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()
               ).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

$adminKeyFile = Join-Path $env:ProgramData 'ssh\administrators_authorized_keys'
$userKeyFile  = Join-Path $env:USERPROFILE '.ssh\authorized_keys'
$targetFile   = if ($userIsAdmin) { $adminKeyFile } else { $userKeyFile }

Say INFO ("This account is {0}an Administrator." -f $(if ($userIsAdmin) { '' } else { 'NOT ' }))
Say INFO ("Keys must go in: {0}" -f $targetFile)

if ($PublicKey) {
    $trimmedKey = $PublicKey.Trim()

    if ($trimmedKey -notmatch '^(ssh-ed25519|ssh-rsa|ecdsa-sha2-\S+)\s+\S+') {
        Say FAIL 'That does not look like a public key line. Expected: "ssh-ed25519 AAAA... comment"'
    } elseif ($trimmedKey -match 'PRIVATE KEY') {
        Say FAIL 'That is a PRIVATE key. Never put a private key on the server. Use the .pub file.'
    } elseif (-not $Apply) {
        Say WARN 'Key looks valid but -Apply was not passed, so it was not installed.'
    } else {
        $dir = Split-Path $targetFile -Parent
        if (-not (Test-Path $dir)) { New-Item -ItemType Directory -Path $dir -Force | Out-Null }

        $alreadyPresent = (Test-Path $targetFile) -and
                          ((Get-Content $targetFile -ErrorAction SilentlyContinue) -contains $trimmedKey)

        if ($alreadyPresent) {
            Say OK 'That key is already authorised.'
        } else {
            Add-Content -Path $targetFile -Value $trimmedKey -Encoding UTF8
            Say OK 'Key added.'
        }

        if ($userIsAdmin) {
            # Strip inheritance and grant only Administrators + SYSTEM, or sshd
            # will reject the file as insecure and fall back to password auth.
            icacls $targetFile /inheritance:r /grant 'Administrators:F' /grant 'SYSTEM:F' | Out-Null
            Say OK 'Applied the required restrictive ACL.'
        }
    }
} else {
    if (Test-Path $targetFile) {
        $count = @(Get-Content $targetFile | Where-Object { $_.Trim() -and $_ -notmatch '^\s*#' }).Count
        Say OK ("{0} key(s) currently authorised." -f $count)
    } else {
        Say WARN 'No authorized_keys file yet. Pass -PublicKey with the laptop key.'
    }
}

# --- Password auth ---------------------------------------------------------
Write-Section 'Password authentication'

$sshdConfig = Join-Path $env:ProgramData 'ssh\sshd_config'

if (-not (Test-Path $sshdConfig)) {
    Say WARN 'sshd_config not found yet (it appears after the service first starts).'
} else {
    $configLines = Get-Content $sshdConfig
    $activeSetting = $configLines | Where-Object { $_ -match '^\s*PasswordAuthentication\s+' } | Select-Object -Last 1
    $passwordsOn = -not ($activeSetting -match 'no\s*$')

    Say INFO ("PasswordAuthentication is currently {0}." -f $(if ($passwordsOn) { 'ENABLED' } else { 'disabled' }))

    if ($DisablePasswordAuth -and $Apply) {
        Copy-Item $sshdConfig "$sshdConfig.bak" -Force
        $updated = $configLines | ForEach-Object {
            if ($_ -match '^\s*#?\s*PasswordAuthentication\s+') { 'PasswordAuthentication no' } else { $_ }
        }
        if ($updated -notcontains 'PasswordAuthentication no') { $updated += 'PasswordAuthentication no' }
        Set-Content -Path $sshdConfig -Value $updated -Encoding UTF8
        Restart-Service sshd
        Say OK 'Password authentication disabled (backup at sshd_config.bak) and sshd restarted.'
    } elseif ($passwordsOn) {
        Say INFO 'Leave it on until key login is proven, then re-run with -Apply -DisablePasswordAuth.'
    }
}

# --- How to connect --------------------------------------------------------
Write-Section 'Connect from the laptop'

$tsExe = (Get-Command tailscale -ErrorAction SilentlyContinue).Source
if (-not $tsExe) {
    $candidate = Join-Path $env:ProgramFiles 'Tailscale\tailscale.exe'
    if (Test-Path $candidate) { $tsExe = $candidate }
}

$host_ = $env:COMPUTERNAME
if ($tsExe) {
    $tsIp = & $tsExe ip -4 2>$null | Select-Object -First 1
    if ($tsIp) { $host_ = $tsIp; Say OK ("Tailscale IPv4: {0}" -f $tsIp) }
    else       { Say WARN 'Tailscale installed but not connected. Run: tailscale up' }
} else {
    Say WARN 'Tailscale not installed - you will only be able to connect from the same LAN.'
}

Say INFO ("ssh {0}@{1}" -f $env:USERNAME, $host_)
Write-Host ''
