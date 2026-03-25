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
