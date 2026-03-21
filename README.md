# awesome-oss-collection

A curated personal collection of open-source projects worth knowing about — organized by use case, with enough context to understand *why* each one matters.

---

## Collection Overview

> **10 categories · 11 projects** — growing over time

```
Collection Hub
├── 🎙️ Speech to Text
│   └── Handy (18.1k ⭐) — offline dictation for any text field
├── 📄 File to Markdown
│   └── MarkItDown (91.2k ⭐) — convert any file format to Markdown
├── 🎥 Screen Recording
│   └── Recordly (2.8k ⭐) — screen recorder with presentation-grade editor
├── 📑 PDF Parsing
│   └── OpenDataLoader PDF (7.3k ⭐) — structure-aware PDF extraction
├── 📈 Financial Analysis
│   ├── AI Hedge Fund (49.4k ⭐) — multi-agent stock analysis
│   └── Daily Stock Analysis (24k ⭐) — automated daily analysis with notifications
├── 🤖 AI Companions
│   └── AIRI (35k ⭐) — self-hosted AI companion with voice and game-playing
├── 🔍 Private Search
│   └── SearXNG (26.9k ⭐) — self-hosted metasearch, no tracking
├── 🔀 LLM Gateway
│   └── LiteLLM (39.8k ⭐) — one interface for 100+ LLMs
├── 🌐 Web Browsers
│   └── Ladybird (61.4k ⭐) — first independent browser engine in decades
└── 📱 On-Device AI
    └── RunAnywhere SDKs (10.3k ⭐) — local AI for iOS, Android, Flutter, Web
```

---

## Use Cases

| Folder | Projects | Summary |
|---|---|---|
| [🎙️ speech-to-text](./speech-to-text/README.md) | 1 | Offline & privacy-first transcription tools |
| [📄 file-to-markdown](./file-to-markdown/README.md) | 1 | Convert docs, PDFs, and more to clean Markdown |
| [🎥 screen-recording](./screen-recording/README.md) | 1 | Screen recorders with editing and presentation tools |
| [📑 pdf-parsing](./pdf-parsing/README.md) | 1 | Structure-aware extraction from complex PDFs |
| [📈 financial-analysis](./financial-analysis/README.md) | 2 | AI-powered stock analysis and investment research |
| [🤖 ai-companions](./ai-companions/README.md) | 1 | Self-hosted AI virtual companions with voice and personality |
| [🔍 private-search](./private-search/README.md) | 1 | Self-hosted search engines with no tracking or profiling |
| [🔀 llm-gateway](./llm-gateway/README.md) | 1 | Unified proxy and SDK for routing across 100+ LLM providers |
| [🌐 web-browsers](./web-browsers/README.md) | 1 | Independent browser engines built from scratch |
| [📱 on-device-ai](./on-device-ai/README.md) | 1 | Run AI locally on mobile and edge — no cloud required |

---

## What's in Here

Each entry documents:

- **What it does** — plain-language description
- **Tech stack** — languages, frameworks, key libraries
- **Star count** — community signal at time of writing
- **Why it's notable** — the actual reason it's worth saving

*Quality over quantity. No entry gets added without a clear "why".*

---

## Highlights

### [Handy](./speech-to-text/README.md#handy) ⭐ 18.1k
Offline speech-to-text for any text field on your computer. Hold a keyboard shortcut, speak, release — your words appear wherever your cursor is. Built on Whisper + Rust + Tauri. No cloud, no subscription.

### [MarkItDown](./file-to-markdown/README.md#markitdown) ⭐ 91.2k
Convert almost any file to clean Markdown — PDFs, Word, Excel, PowerPoint, images, audio, YouTube URLs and more. Built by Microsoft, designed for LLM workflows where document structure needs to survive into the model's context.

### [Recordly](./screen-recording/README.md#recordly) ⭐ 2.8k
Open-source alternative to Screen Studio. Records your screen then lets you add auto-zoom, cursor effects, webcam overlays, and styled backgrounds before exporting — presentation-grade output from a free, local tool.

### [OpenDataLoader PDF](./pdf-parsing/README.md#opendataloader-pdf) ⭐ 7.3k
Structure-aware PDF extraction to Markdown, JSON, and HTML. XY-Cut++ reading order, OCR in 80+ languages, LaTeX formula extraction, and #1 benchmark accuracy for table parsing. For when MarkItDown's general conversion isn't enough and you need the structure to actually survive.

### [AI Hedge Fund](./financial-analysis/README.md#ai-hedge-fund) ⭐ 49.4k
12 AI agents each embodying a legendary investor philosophy — Buffett, Cathie Wood, and more — independently analyse a stock then debate a final recommendation. Multi-agent architecture for investment research, with backtesting and a web UI. Educational use only.

### [Daily Stock Analysis](./financial-analysis/README.md#daily-stock-analysis) ⭐ 24k
Automated daily stock analysis pipeline via GitHub Actions — pulls live data, generates AI buy/sell signals and entry/exit points, pushes results to WeChat, Feishu, Telegram, Slack, or email. A-shares, HK, and US markets. Zero infrastructure cost.

### [AIRI](./ai-companions/README.md#airi) ⭐ 35k
Self-hosted open-source Neuro-sama. Voice conversations, Live2D/VRM avatar animation, and actual game-playing (Minecraft, Factorio, KSP) — all running locally via WebGPU and WASM. MIT licensed, cross-platform, no cloud required.

### [SearXNG](./private-search/README.md#searxng) ⭐ 26.9k
The definitive self-hosted private metasearch engine. Aggregates results from dozens of search services without passing your identity to any of them. 277 contributors, 9,000+ commits, and the standard behind most privacy-respecting search frontends.

### [LiteLLM](./llm-gateway/README.md#litellm) ⭐ 39.8k
One Python SDK and proxy server for 100+ LLMs. Call OpenAI, Anthropic, Azure, Bedrock, and more with the same format. Deploy as a production AI gateway with cost tracking, load balancing, virtual keys, and 8ms P95 latency. The de facto standard for teams that need provider flexibility without lock-in.

### [Ladybird](./web-browsers/README.md#ladybird) ⭐ 61.4k
The first truly independent browser engine in decades — zero shared code with Blink, Gecko, or WebKit. Multi-process, sandboxed, cross-platform. Still pre-alpha but 61.4k stars on developer-only software signals the community understands exactly why browser engine diversity matters.

### [RunAnywhere SDKs](./on-device-ai/README.md#runanywhere-sdks) ⭐ 10.3k
Multi-platform SDKs for on-device AI across iOS, Android, Flutter, React Native, and Web. Wraps llama.cpp and ONNX into idiomatic developer APIs — LLMs, Whisper STT, TTS, vision, and full voice pipelines, all running locally with zero data transmission.

---

## Recent Additions

| Project | Category | Stars | Added |
|---|---|---|---|
| [Daily Stock Analysis](./financial-analysis/README.md) | Financial Analysis | 24k ⭐ | 2026-03 |
| [RunAnywhere SDKs](./on-device-ai/README.md) | On-Device AI | 10.3k ⭐ | 2026-03 |
| [Ladybird](./web-browsers/README.md) | Web Browsers | 61.4k ⭐ | 2026-03 |
| [LiteLLM](./llm-gateway/README.md) | LLM Gateway | 39.8k ⭐ | 2026-03 |
| [SearXNG](./private-search/README.md) | Private Search | 26.9k ⭐ | 2026-03 |
| [AIRI](./ai-companions/README.md) | AI Companions | 35k ⭐ | 2026-03 |
| [AI Hedge Fund](./financial-analysis/README.md) | Financial Analysis | 49.4k ⭐ | 2026-03 |
| [OpenDataLoader PDF](./pdf-parsing/README.md) | PDF Parsing | 7.3k ⭐ | 2026-03 |
| [Recordly](./screen-recording/README.md) | Screen Recording | 2.8k ⭐ | 2026-03 |
| [MarkItDown](./file-to-markdown/README.md) | File to Markdown | 91.2k ⭐ | 2026-03 |
| [Handy](./speech-to-text/README.md) | Speech to Text | 18.1k ⭐ | 2026-03 |
