# 📱 On-Device AI

SDKs and tools for running AI locally on mobile and edge devices — no cloud, no data leaving the device.

← [Back to collection](../README.md)

---

### [RunAnywhere SDKs](https://github.com/RunanywhereAI/runanywhere-sdks) ⭐ 10.3k

**Multi-platform SDKs for on-device LLMs, speech, and vision — iOS, Android, Flutter, React Native, and Web.**

Wraps llama.cpp and ONNX into developer-friendly SDKs so you can embed local AI in your mobile or web app without touching C++. Supports LLM text generation (Llama, Mistral, Qwen, SmolLM), Whisper speech-to-text, neural TTS, vision language models, and a full voice pipeline (STT→LLM→TTS) — all running on-device with zero data transmission. Streaming responses, structured JSON output, and tool calling included.

**Stack:** Swift (iOS/macOS) · Kotlin (Android) · TypeScript (Web/React Native) · Dart (Flutter) · C++ core · llama.cpp · ONNX
**License:** Apache 2.0
**Status:** Swift and Kotlin stable; Web, React Native, Flutter in beta

**Why it's notable:** llama.cpp is the gold standard for local LLM inference but it's C++ — not something you drop into a Flutter or React Native app. RunAnywhere SDKs are the missing layer: idiomatic wrappers across every major mobile/web platform that make on-device AI as approachable as any other SDK call. 1,831 commits and 30 open issues suggests serious engineering depth behind the clean APIs.

---
