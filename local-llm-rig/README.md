# local-llm-rig

Setup for turning an always-on Windows 10 desktop into a local LLM inference
host that a laptop can reach from anywhere over Tailscale, plus SSH so the
laptop can run jobs, move files and tunnel ports to it.

**This folder is unrelated to the website in the rest of this repository.**
`netlify.toml` serves the repository root, so a redirect rule there returns 404
for `/local-llm-rig/*` to keep these files off the public site.

## Target hardware

| | |
|---|---|
| GPU | AMD Radeon RX 5600 XT (RDNA1, Navi 10, gfx1010) |
| VRAM | 6 GB (6103 MB reported by dxdiag) |
| System RAM | ~16 GB |
| OS | Windows 10 |

## Why Vulkan and not ROCm

AMD's ROCm stack does not support RDNA1 on Windows. Ollama's Windows AMD path
is ROCm-based, so it will not detect this card and will silently fall back to
CPU inference. The working path is Vulkan, which RDNA1 supports well.

LM Studio ships a Vulkan runtime and an OpenAI-compatible server, so it is the
recommended host application here.

## What fits in 6 GB

| Model | Q4_K_M | Verdict |
|---|---|---|
| Mistral 7B | ~4.4 GB | Comfortable |
| Qwen2.5 7B Instruct | ~4.7 GB | Comfortable |
| Llama 3.1 8B | ~4.9 GB | Fits, reduce context to 4-8k |
| Anything 13B+ | 9 GB+ | Spills to system RAM, unusably slow |

Expect roughly 25-40 tokens/sec in the 7-8B range.

Ignore the "total available graphics memory" figure Windows reports (~14 GB
here). That is VRAM plus system memory Windows is willing to lend the GPU.
A model that overflows into shared memory is not still running on the GPU — it
is crossing the PCIe bus per access, and throughput collapses. The number that
governs model choice is the 6 GB of real VRAM.

## Scripts

### setup-llm-host.ps1

Audit only — safe to run at any time, changes nothing:

```powershell
.\setup-llm-host.ps1
```

Apply the power and firewall changes (elevated PowerShell required):

```powershell
.\setup-llm-host.ps1 -Apply
```

If you use Ollama instead of LM Studio, pass its port:

```powershell
.\setup-llm-host.ps1 -Apply -Port 11434
```

Checks: GPU model and true VRAM size (read from the driver registry key,
because WMI's `AdapterRAM` field wraps at 4 GB and misreports 6 GB cards),
graphics driver age, the Vulkan runtime, sleep/hibernate/disk timeouts on AC,
an inbound firewall rule scoped to private networks, Tailscale state, and
whether the inference port is listening and bound to all interfaces.

### enable-ssh-server.ps1

```powershell
.\enable-ssh-server.ps1                                      # audit
.\enable-ssh-server.ps1 -Apply -PublicKey "ssh-ed25519 ..."  # install + authorise
.\enable-ssh-server.ps1 -Apply -DisablePasswordAuth          # harden, last
```

Installs the OpenSSH Server feature, sets it to start automatically, makes
PowerShell the default remote shell, opens TCP 22 on private networks, and
installs a public key.

It handles the trap that catches most people: for accounts in the
Administrators group Windows ignores `~/.ssh/authorized_keys` and reads
`C:\ProgramData\ssh\administrators_authorized_keys`, which must have
inheritance stripped and be writable only by Administrators and SYSTEM. With a
permissive ACL, sshd rejects the key and falls back to asking for a password,
with no error explaining why.

Run `-DisablePasswordAuth` only after key login is confirmed from the laptop.
Reversing it requires physical access to the machine.

## Manual steps the scripts cannot do

1. Install the latest AMD Adrenalin driver from amd.com
2. Install LM Studio from lmstudio.ai, set **Settings → Runtime → Vulkan**
3. Download a model (start with Qwen2.5 7B Instruct GGUF, Q4_K_M)
4. In the **Developer** tab: start the server and tick **Serve on Local Network**
5. Install Tailscale on both the desktop and the laptop, signed into the same account

## Connecting from the laptop

See `CONNECT-RUNBOOK.md` for the full ordered sequence with a verification step
after each stage.

```
base_url: http://<tailnet-name-or-ip>:1234/v1
api_key:  lm-studio          # any non-empty string; not validated
```
