# 🎙️ Speech to Text

Tools for transcribing spoken audio into text — local, cloud, or hybrid.

← [Back to collection](../README.md)

---

### [Handy](https://github.com/cjpais/Handy) ⭐ 18.1k

**Offline speech-to-text for any text field on your computer.**

Press a keyboard shortcut, speak, release — your words appear wherever your cursor is. No cloud, no subscription, no audio leaving your machine. Built on OpenAI's Whisper models (Small → Large, or Parakeet V3) with Silero VAD to filter silence, so transcriptions are clean without manual trimming.

**Stack:** Rust · TypeScript · React · Tauri · Whisper/whisper-rs · cpal · rdev
**License:** MIT
**Platforms:** macOS · Windows · Linux

**Why it's notable:** Tauri + Rust backend gives near-native performance. GPU acceleration kicks in automatically. The offline-first constraint isn't a limitation — it's the whole point. Privacy-respecting dictation that works anywhere in your OS.

---

### [RealtimeSTT](https://github.com/KoljaB/RealtimeSTT) ⭐ 9.6k

**Python library for real-time speech-to-text with voice activity detection and wake word support.**

Three lines of Python to start streaming microphone transcription. RealtimeSTT handles the hard parts: WebRTCVAD and SileroVAD detect when speech starts and stops so you're not transcribing silence, Faster-Whisper does the actual transcription, and Porcupine or OpenWakeWord enables always-listening wake word activation ("Hey Jarvis", then speak). Runs on CPU or CUDA GPU. Designed to be embedded into voice assistants, smart home controllers, transcription apps, or any Python project that needs to hear and respond.

**Stack:** Python · Faster-Whisper · SileroVAD · WebRTCVAD · Porcupine / OpenWakeWord · CUDA
**License:** MIT

**Why it's notable:** Handy (the other entry here) is an end-user app — you install it and it just works. RealtimeSTT is for developers building the next Handy. The combination of dual VAD (WebRTC for speed, Silero for accuracy), wake word support, and Faster-Whisper's efficiency makes it the most complete open-source foundation for real-time voice features. 9.6k stars and 836 forks for a Python library signals serious developer adoption — it's the go-to dependency when you need to add ears to your application.

---
