# 🎙️ Speech to Text

Tools for transcribing spoken audio into text — local, cloud, or hybrid.

← [Back to collection](../README.md)

---

### [Handy](https://github.com/cjpais/Handy) ⭐ 18.1k

> **How it works** — [view diagram on Excalidraw](https://excalidraw.com/#json=3w-oszIlnrwtrO_FRdSiM,mfEhz8r2_hJeQ1WoTM3LPw)
>
> Hold shortcut → Mic captures audio → Silero VAD strips silence → Whisper model transcribes → text injected at cursor via rdev

**Offline speech-to-text for any text field on your computer.**

Press a keyboard shortcut, speak, release — your words appear wherever your cursor is. No cloud, no subscription, no audio leaving your machine. Built on OpenAI's Whisper models (Small → Large, or Parakeet V3) with Silero VAD to filter silence, so transcriptions are clean without manual trimming.

**Stack:** Rust · TypeScript · React · Tauri · Whisper/whisper-rs · cpal · rdev
**License:** MIT
**Platforms:** macOS · Windows · Linux

**Why it's notable:** Tauri + Rust backend gives near-native performance. GPU acceleration kicks in automatically. The offline-first constraint isn't a limitation — it's the whole point. Privacy-respecting dictation that works anywhere in your OS.

---
