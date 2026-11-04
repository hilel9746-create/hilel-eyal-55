# Handoff prompt

Copy everything below the line into a fresh session with another agent.

---

## Context

I have two machines and I want to run AI models locally on the stronger one and
use them from the weaker one.

**Desktop (the inference host)** — always on, always plugged in:
- AMD Radeon RX 5600 XT, 6 GB VRAM, RDNA1 (Navi 10, gfx1010)
- ~16 GB system RAM
- Windows 10

**Laptop** — where I actually work. It should reach the desktop remotely.

## What has already been decided (do not re-litigate)

1. **The inference backend is Vulkan, not ROCm.** AMD does not support RDNA1 in
   ROCm on Windows. Ollama's Windows AMD path is ROCm-based, so it will not see
   this card and will silently fall back to CPU. LM Studio with its Vulkan
   runtime is the chosen host application.

2. **Networking is Tailscale**, not port-forwarding. Both machines join the same
   tailnet; the laptop reaches the desktop by its tailnet address. No ports are
   exposed to the public internet.

3. **Remote control is SSH.** The Windows OpenSSH Server is installed and
   running, key-based auth only, password authentication disabled.

4. **6 GB VRAM is the binding constraint.** 7-8B models at Q4_K_M fit
   (Mistral 7B ~4.4 GB, Qwen2.5 7B ~4.7 GB, Llama 3.1 8B ~4.9 GB with reduced
   context). 13B and above spill into system RAM and are unusably slow. Do not
   propose 30B or 70B models for this machine, and do not count the ~14 GB
   "total available graphics memory" Windows reports — that is mostly shared
   system RAM, and a model that reaches into it collapses in throughput.

5. There are two scripts already written, `setup-llm-host.ps1` and
   `enable-ssh-server.ps1`. Both audit by default and only change anything when
   passed `-Apply`.

## What I want from you

Pick up from there. Specifically:

1. Walk me through installing and verifying the LM Studio + Vulkan setup on the
   desktop, including how to confirm the GPU is genuinely being used and not
   silently falling back to CPU.
2. Help me tune context length and GPU offload for 6 GB, and tell me what
   tokens/sec I should consider normal so I can tell a bad setup from a
   hardware limit.
3. Set up the laptop side against the OpenAI-compatible endpoint at
   `http://<tailnet-name>:1234/v1`.
4. Advise on running image and video generation on the same box — see the
   constraint below.

## Important constraint for image/video generation

This is AMD on Windows, so PyTorch has no CUDA. The realistic options are
**ZLUDA** (a CUDA translation layer; gfx1010 is supported and it is faster and
lighter on VRAM than the alternative) or **DirectML** (slower, more VRAM). Any
advice that assumes an NVIDIA card or a working `torch.cuda` is wrong for this
machine — say so rather than working around it silently.

For video generation specifically, 6 GB rules out most models. FramePack was
designed for this ceiling; Wan2GP targets it too. Full HunyuanVideo, Wan 2.2
14B and the larger LTX-Video variants do not fit.

## How I want you to work

- Tell me when something will not work on this hardware instead of giving me a
  workaround that quietly degrades to CPU. I would rather hear "6 GB is not
  enough for that" than wait ten minutes for a bad result.
- Give me exact commands and exact UI paths, not general direction.
- Ask me to run a verification step after each install, and tell me what the
  correct output looks like.
- I read Hebrew and English; reply in Hebrew.
