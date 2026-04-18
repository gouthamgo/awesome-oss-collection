# 🎙️ Voice Cloning

Tools for generating realistic speech and cloning voices locally — high-quality output without cloud dependencies.

← [Back to collection](../README.md)

---

### [LuxTTS](https://github.com/ysharma3501/LuxTTS) ⭐ 3.2k

**High-fidelity voice cloning at 150x realtime speed — runs on ~1GB VRAM.**

LuxTTS generates realistic 48kHz speech from text using a distilled ZipVoice architecture that runs in just 4 inference steps. Clone a voice from a short reference clip and synthesise new audio at over 150x realtime on a consumer GPU — or run it on CPU or Apple MPS without GPU hardware at all. Output is 48kHz stereo, double the typical 24kHz of most local TTS tools, making it suitable for production audio.

**Stack:** Python, ZipVoice architecture, CUDA/CPU/Apple MPS
**License:** Apache 2.0

**Why it's notable:** Most local voice cloning tools force a trade-off: quality or speed. LuxTTS gets both by distilling the generation process to 4 steps while using a custom 48kHz vocoder to preserve audio fidelity. The ~1GB VRAM requirement means it fits on virtually any modern GPU — including laptop GPUs — rather than requiring a high-end workstation. Apache 2.0 with no model licence restrictions (unlike many TTS tools that use CC-BY-NC for their weights) means it's freely usable in commercial projects.

---

### [Voicebox](https://github.com/jamiepine/voicebox) ⭐ 20.5k

**The open-source voice synthesis studio — clone, generate, edit, and ship voice-powered apps locally.**

Voicebox is a full desktop application for voice synthesis built on Tauri (Rust) with a FastAPI Python backend and React frontend. It wraps five TTS/voice-cloning engines — including LuxTTS — under a polished UI: clone a voice from a reference clip, generate speech with any engine, layer multiple voices on a timeline editor, apply eight post-processing audio effects (pitch, reverb, EQ, and more), and track versions. The built-in REST API lets you use Voicebox as a local voice synthesis backend for other applications. Deploy as a desktop app or via Docker for headless/server use.

**Stack:** Python (FastAPI), TypeScript/React, Rust (Tauri), MLX/PyTorch inference
**License:** MIT

**Why it's notable:** LuxTTS (the other entry here) is an excellent model — fast, high-quality, MIT-licensed. Voicebox is what you build when you want the studio experience around that model. Five engines means you can pick the right tool for the job without leaving the app: Qwen3 for quality, LuxTTS for speed, Chatterbox for naturalness. The timeline editor elevates it from "generate audio" to "produce audio" — the kind of multi-voice scene editing that previously required dedicated audio production software. 20.5k stars committed the day before evaluation confirms strong, active traction.

---
