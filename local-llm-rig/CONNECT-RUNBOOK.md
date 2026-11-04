# Runbook: desktop as a server for the laptop

Goal: one command typed on the laptop reaches the desktop and does real work.

Everything here runs on your own machines. Follow the order — each step is
verified before the next one depends on it.

Legend: DESKTOP = run on the always-on desktop, LAPTOP = run on the laptop.

---

## Step 1 — DESKTOP — Tailscale

Install from https://tailscale.com/download, sign in, then:

```powershell
tailscale ip -4
```

**Verify:** you get an address like `100.x.y.z`. Write it down.

Tailscale is what makes this work from outside the house without exposing
anything to the public internet. Do not skip it and do not port-forward SSH.

---

## Step 2 — LAPTOP — Tailscale

Install, sign in to **the same account**, then:

```
tailscale status
```

**Verify:** the desktop appears in the list and is not marked `offline`.

If each machine lists only itself, they are signed into different accounts.
That is the most common failure here, and everything looks installed and
healthy until you try to connect.

---

## Step 3 — LAPTOP — Create an SSH key

**macOS / Linux:**
```bash
ssh-keygen -t ed25519 -C "laptop"
cat ~/.ssh/id_ed25519.pub
```

**Windows (PowerShell):**
```powershell
New-Item -ItemType Directory -Path "$env:USERPROFILE\.ssh" -Force | Out-Null
ssh-keygen -t ed25519 -C "laptop"
Get-Content "$env:USERPROFILE\.ssh\id_ed25519.pub"
```

Press Enter at the file prompt. A passphrase is optional but recommended.

The `New-Item` line matters on Windows: `ssh-keygen` does not create the `.ssh`
directory itself and fails with "No such file or directory" if it is missing.

**Verify:** the output is one line starting `ssh-ed25519 AAAA...`.
Copy that whole line. It is the **public** key and is safe to move around.
The other file, without `.pub`, is the private key — it never leaves the laptop.

---

## Step 4 — DESKTOP — Enable the SSH server

In an **Administrator** PowerShell, paste the public key from step 3:

```powershell
.\enable-ssh-server.ps1 -Apply -PublicKey "ssh-ed25519 AAAA...  laptop"
```

**Verify:** the output ends with a `ssh <user>@100.x.y.z` line and no red `[FAIL]`.

Administrator is not optional. For an account in the Administrators group the
key must land in `C:\ProgramData\ssh\administrators_authorized_keys` with a
restrictive ACL, and the script cannot write either without elevation.

---

## Step 5 — LAPTOP — First connection

```bash
ssh <windows-username>@100.x.y.z
```

**Verify:** you land in a PowerShell prompt on the desktop. Run `hostname` to
confirm you are really on the other machine, then `exit`.

If it asks for a password, the key is not being read — see Troubleshooting.

---

## Step 6 — LAPTOP — Give it a short name

Add to `~/.ssh/config` (on Windows: `%USERPROFILE%\.ssh\config`):

```
Host desktop
    HostName 100.x.y.z
    User <windows-username>
    ServerAliveInterval 30
    ServerAliveCountMax 6
```

`ServerAliveInterval` keeps long jobs from dropping on an idle connection.

**Verify — this is the one command you were after:**

```bash
ssh desktop "Get-CimInstance Win32_VideoController | Select-Object Name, DriverVersion"
```

You should see `AMD Radeon RX 5600 XT` printed on the laptop.

---

## Step 7 — DESKTOP — Lock it down

Only now that key login is proven:

```powershell
.\enable-ssh-server.ps1 -Apply -DisablePasswordAuth
```

**Verify:** reconnect from the laptop. It should still work, instantly, with no
password prompt.

Before you do this, make sure you have a second way in — a backup keypair whose
private half is in a password manager, or a known-good password on the account.
Key-only auth with one key means losing that key costs you a trip to the
machine.

---

## What you can now do from the laptop

**Run a heavy job on the desktop:**
```bash
ssh desktop "cd C:\work; python render.py"
```

**Push a file up / pull a result down:**
```bash
scp bigvideo.mp4 desktop:C:/work/
scp desktop:C:/work/out.mp4 .
```

**Use the desktop's LLM server as if it were local** — this is the port
forwarding piece. It maps the desktop's port 1234 onto the laptop's localhost:

```bash
ssh -N -L 1234:localhost:1234 desktop
```

Leave that running, and any tool on the laptop pointed at
`http://localhost:1234/v1` is really talking to the desktop's GPU. This is the
cleanest way to attach laptop tools that assume a local server.

**Keep a job alive after you close the laptop.** A plain `ssh desktop "long job"`
dies when the connection drops. Instead start it detached:

```bash
ssh desktop "Start-Process -NoNewWindow python -ArgumentList 'render.py' -RedirectStandardOutput C:\work\render.log"
```

then check on it later with:

```bash
ssh desktop "Get-Content C:\work\render.log -Tail 20"
```

---

## Troubleshooting

**It asks for a password even though the key is installed.**
Almost always the ACL on `administrators_authorized_keys`. Re-run step 4 from
an elevated prompt. To see the real reason, on the desktop:
```powershell
Get-WinEvent -LogName 'OpenSSH/Operational' -MaxEvents 20 | Format-List TimeCreated, Message
```

**It asks for a password and the account has none.**
Windows OpenSSH rejects blank passwords outright, so password auth is not a
fallback on an account without one. Either set a password or fix the key.

**Connection times out.**
Check `tailscale status` on both machines. If the desktop shows as offline it
has probably gone to sleep — run `setup-llm-host.ps1 -Apply`.

**Works at home, not away.**
You are on the LAN address instead of the tailnet address. `HostName` in
`~/.ssh/config` must be the `100.x.y.z` address, not `192.168.x.x`.

**Connection drops during long jobs.**
Confirm the `ServerAliveInterval` lines are in your config, and start long jobs
detached as shown above.
