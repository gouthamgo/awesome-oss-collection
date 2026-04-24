# awesome-oss-collection

A curated personal collection of open-source projects worth knowing about — organized by use case, with enough context to understand *why* each one matters.

![Projects](https://img.shields.io/badge/projects-52-blue?style=flat-square)
![Categories](https://img.shields.io/badge/categories-31-blueviolet?style=flat-square)
![License](https://img.shields.io/github/license/gouthamgo/awesome-oss-collection?style=flat-square)
![Last Commit](https://img.shields.io/github/last-commit/gouthamgo/awesome-oss-collection?style=flat-square)

---

## Collection Overview

> **31 categories · 52 projects** — growing over time

```
Collection Hub
├── 🎙️ Speech to Text
│   ├── Handy (18.1k ⭐) — offline dictation for any text field
│   └── RealtimeSTT (9.6k ⭐) — Python library for real-time STT with VAD and wake word support
├── 📄 File to Markdown
│   └── MarkItDown (91.2k ⭐) — convert any file format to Markdown
├── 🎥 Screen Recording
│   └── Recordly (2.8k ⭐) — screen recorder with presentation-grade editor
├── 📑 PDF Parsing
│   └── OpenDataLoader PDF (7.3k ⭐) — structure-aware PDF extraction
├── 📈 Financial Analysis
│   ├── AI Hedge Fund (49.4k ⭐) — multi-agent stock analysis
│   ├── Daily Stock Analysis (24k ⭐) — automated daily analysis with notifications
│   └── AI-Trader (12.5k ⭐) — agent swarm trading with signals marketplace and live execution
├── 🤖 AI Companions
│   └── AIRI (35k ⭐) — self-hosted AI companion with voice and game-playing
├── 🔍 Private Search
│   └── SearXNG (26.9k ⭐) — self-hosted metasearch, no tracking
├── 🔀 LLM Gateway
│   └── LiteLLM (39.8k ⭐) — one interface for 100+ LLMs
├── 🌐 Web Browsers
│   └── Ladybird (61.4k ⭐) — first independent browser engine in decades
├── 📱 On-Device AI
│   └── RunAnywhere SDKs (10.3k ⭐) — local AI for iOS, Android, Flutter, Web
├── 🧠 Local LLM
│   ├── Ollama (166k ⭐) — run any LLM locally with one command
│   ├── LlamaFile (23.9k ⭐) — LLM as a single executable
│   ├── llm (11.4k ⭐) — CLI and Python library for any LLM
│   └── vLLM (74.3k ⭐) — production LLM serving with PagedAttention
├── 🕸️ Agent Frameworks
│   ├── CrewAI (46.8k ⭐) — multi-agent with roles, goals, backstories
│   ├── DSPy (33k ⭐) — program LLMs instead of prompting them
│   ├── DeerFlow (32.6k ⭐) — deployable super agent platform with sandbox + memory
│   ├── AutoGen (56.2k ⭐) — Microsoft's event-driven distributed multi-agent framework
│   └── hermes-agent (51.8k ⭐) — self-improving autonomous agent, learns from experience
├── 🏗️ LLM App Builder
│   ├── Dify (134k ⭐) — visual workflow builder for LLM applications
│   ├── AnythingLLM (56.7k ⭐) — self-hosted AI workspace, chat with your docs
│   └── Gradio (42.2k ⭐) — build interactive ML/AI web UIs in pure Python
├── 🕷️ Web Scraping
│   └── Firecrawl (96.1k ⭐) — turn any website into LLM-ready data
├── 📚 RAG Frameworks
│   ├── LightRAG (29.8k ⭐) — RAG with knowledge graph for relational retrieval
│   └── RAGFlow (76.2k ⭐) — self-hosted RAG platform with deep document understanding
├── 🗄️ Vector Databases
│   ├── Qdrant (29.8k ⭐) — Rust-based vector DB, fast and self-hostable
│   └── Milvus (43.5k ⭐) — distributed vector DB for billions of vectors
├── 📊 LLM Evaluation
│   └── Ragas (13.1k ⭐) — evaluate RAG pipelines with objective metrics
├── 🏠 Home Automation
│   └── Home Assistant (85.7k ⭐) — self-hosted smart home, local control, privacy-first
├── 🛠️ AI Dev Tools
│   ├── Spec Kit (81.1k ⭐) — spec-driven development CLI for AI coding agents
│   ├── Agent Orchestrator (5.3k ⭐) — fleet of parallel coding agents across git branches
│   └── Aider (42.8k ⭐) — AI pair programming in your terminal, edits code and commits to git
├── 🧪 Testing
│   └── Keploy (16.6k ⭐) — auto-generate tests from real traffic via eBPF, zero code changes
├── 🔐 Security Testing
│   ├── Strix (21.3k ⭐) — autonomous AI agents that find and validate vulnerabilities
│   └── Garak (7.4k ⭐) — LLM vulnerability scanner for jailbreaks and prompt injection
├── 🎤 Voice Cloning
│   ├── LuxTTS (3.2k ⭐) — 48kHz voice cloning at 150x realtime on ~1GB VRAM
│   └── Voicebox (20.5k ⭐) — open-source voice synthesis studio, 5 engines, timeline editor, REST API
├── 🏢 AI Operations
│   └── Paperclip (35.9k ⭐) — run AI agent teams like a company, with org charts and budgets
├── 🎨 AI Generation
│   └── ComfyUI (108k ⭐) — node-based visual engine for AI image, video, audio, and 3D generation
├── 📡 Monitoring
│   └── Uptime Kuma (84.9k ⭐) — self-hosted uptime monitoring with 90+ notification integrations
├── 🚀 Self-Hosted Infra
│   └── Coolify (52.6k ⭐) — self-host everything, your open-source Heroku/Netlify/Vercel
├── 🔑 Password Manager
│   └── Vaultwarden (57.9k ⭐) — self-hosted Bitwarden server in Rust, uses 10MB of RAM
├── 📝 Productivity
│   ├── AppFlowy (69.1k ⭐) — self-hosted Notion alternative, local-first, Flutter + Rust
│   └── Rowboat (10k ⭐) — local-first AI coworker, emails + meetings → knowledge graph → action
├── 🎬 Automated Video
│   └── RedditVideoMakerBot (8.7k ⭐) — turn any Reddit thread into a TikTok/Shorts video with one command
├── 🧰 Agent Tools
│   ├── Agent-Reach (15.4k ⭐) — give AI agents internet access across 14+ platforms, zero API cost
│   ├── Graphify (4.2k ⭐) — turn any codebase into a queryable knowledge graph, 71.5x token reduction
│   └── agent-skills (11.9k ⭐) — 20 production engineering skills across 6 phases, multi-agent
└── 📲 Social Media
    └── Postiz (28.1k ⭐) — self-hosted Buffer alternative, 15+ platforms, AI-assisted scheduling
```

---

## Use Cases

| Folder | Projects | Summary |
|---|---|---|
| [🎙️ speech-to-text](./speech-to-text/README.md) | 2 | Offline & privacy-first transcription — desktop apps and developer libraries |
| [📄 file-to-markdown](./file-to-markdown/README.md) | 1 | Convert docs, PDFs, and more to clean Markdown |
| [🎥 screen-recording](./screen-recording/README.md) | 1 | Screen recorders with editing and presentation tools |
| [📑 pdf-parsing](./pdf-parsing/README.md) | 1 | Structure-aware extraction from complex PDFs |
| [📈 financial-analysis](./financial-analysis/README.md) | 3 | AI-powered stock analysis, research, and automated execution |
| [🤖 ai-companions](./ai-companions/README.md) | 1 | Self-hosted AI virtual companions with voice and personality |
| [🔍 private-search](./private-search/README.md) | 1 | Self-hosted search engines with no tracking or profiling |
| [🔀 llm-gateway](./llm-gateway/README.md) | 1 | Unified proxy and SDK for routing across 100+ LLM providers |
| [🌐 web-browsers](./web-browsers/README.md) | 1 | Independent browser engines built from scratch |
| [📱 on-device-ai](./on-device-ai/README.md) | 1 | Run AI locally on mobile and edge — no cloud required |
| [🧠 local-llm](./local-llm/README.md) | 4 | Run open-source LLMs locally — personal use to production serving |
| [🕸️ agent-frameworks](./agent-frameworks/README.md) | 5 | Frameworks for building, orchestrating, and deploying AI agents |
| [🏗️ llm-app-builder](./llm-app-builder/README.md) | 3 | Platforms for building and deploying LLM-powered applications |
| [🕷️ web-scraping](./web-scraping/README.md) | 1 | Extract structured, LLM-ready data from any website |
| [📚 rag-frameworks](./rag-frameworks/README.md) | 2 | Retrieval-Augmented Generation — knowledge graph and full platform |
| [🗄️ vector-databases](./vector-databases/README.md) | 2 | Self-hosted vector databases for semantic search and AI memory |
| [📊 llm-evaluation](./llm-evaluation/README.md) | 1 | Evaluate RAG pipelines and LLM outputs with objective metrics |
| [🏠 home-automation](./home-automation/README.md) | 1 | Self-hosted smart home control — local, private, no cloud required |
| [🛠️ ai-dev-tools](./ai-dev-tools/README.md) | 3 | AI-augmented development workflows — spec, plan, implement |
| [🧪 testing](./testing/README.md) | 1 | Auto-generate tests and mocks from real traffic — no instrumentation needed |
| [🔐 security-testing](./security-testing/README.md) | 2 | Pen testing for apps and LLM vulnerability scanning |
| [🎤 voice-cloning](./voice-cloning/README.md) | 2 | Local voice cloning — model library and full studio app, no cloud required |
| [🏢 ai-operations](./ai-operations/README.md) | 1 | Orchestrate and govern AI agent teams at the organisational level |
| [🎨 ai-generation](./ai-generation/README.md) | 1 | Node-based visual pipelines for AI image, video, audio, and 3D generation |
| [📡 monitoring](./monitoring/README.md) | 1 | Self-hosted uptime and performance monitoring with alerting |
| [🚀 self-hosted-infra](./self-hosted-infra/README.md) | 1 | Self-host your own PaaS — deploy apps, databases, and services on your server |
| [🔑 password-manager](./password-manager/README.md) | 1 | Self-hosted password vaults — your credentials on your own server |
| [📝 productivity](./productivity/README.md) | 2 | Self-hosted workspaces and AI coworkers — notes, docs, and persistent knowledge |
| [🎬 automated-video](./automated-video/README.md) | 1 | Automate short-form video creation from Reddit and online content — no editing needed |
| [🧰 agent-tools](./agent-tools/README.md) | 3 | Extend AI coding agents with internet access, knowledge graphs, and engineering workflows |
| [📲 social-media](./social-media/README.md) | 1 | Self-hosted social media scheduling and management across 15+ platforms |

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

### [RealtimeSTT](./speech-to-text/README.md#realtimestt) ⭐ 9.6k
Python library for building real-time voice features — three lines to start streaming mic transcription. SileroVAD + WebRTCVAD detect speech boundaries, Faster-Whisper transcribes, Porcupine/OpenWakeWord enables always-on wake word detection. CPU and CUDA. The developer foundation for voice assistants and transcription apps. MIT.

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

### [AI-Trader](./financial-analysis/README.md#ai-trader) ⭐ 12.5k
100% automated trading platform from HKUDS. Agent swarm intelligence — multiple strategies run in parallel, collective signal strength drives live execution. Signals marketplace with copy trading, supports stocks, crypto, and prediction markets. Paper trading mode for safe strategy testing. MIT, 2.1k forks.

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

### [Ollama](./local-llm/README.md#ollama) ⭐ 166k
Run any open-source LLM locally with one command. Pull Llama, Mistral, Gemma, Qwen and 100+ models, get an OpenAI-compatible REST API instantly. The tool that made local AI accessible to everyone — 166k stars is the highest in this collection.

### [LlamaFile](./local-llm/README.md#llamafile) ⭐ 23.9k
Mozilla-backed project that bundles an LLM and its runtime into a single executable. Download one file, run it anywhere — macOS, Windows, Linux, FreeBSD, x86 or ARM — with zero setup. The "LLM as binary" concept is genuinely novel.

### [llm](./local-llm/README.md#llm) ⭐ 11.4k
Simon Willison's CLI and Python library for querying any LLM — cloud or local. Logs every prompt and response to SQLite. Simple, composable, Unix-philosophy tool for humans at the terminal.

### [vLLM](./local-llm/README.md#vllm) ⭐ 74.3k
The industry standard for production LLM serving. PagedAttention eliminates GPU memory fragmentation, continuous batching maximises throughput across concurrent requests. OpenAI-compatible API, multi-GPU, quantization support. Apache 2.0, adopted by Google, Microsoft, and most major AI labs.

### [CrewAI](./agent-frameworks/README.md#crewai) ⭐ 46.8k
Multi-agent framework where agents have roles, goals, and backstories — maps to how humans think about teams. Define a crew, assign tasks, let agents collaborate and delegate. MIT licensed, intuitive enough to ship in an afternoon.

### [DSPy](./agent-frameworks/README.md#dspy) ⭐ 33k
Stanford NLP's framework for programming LLMs rather than prompting them. Define modules with typed signatures, chain them, then let optimizers automatically tune prompts and few-shot examples against your metric.

### [DeerFlow](./agent-frameworks/README.md#deerflow) ⭐ 32.6k
ByteDance's deployable super agent platform. Spin up with Docker and get a full-stack web UI where agents research, write reports, generate slides, and execute code in isolated sandboxes — with long-term memory and Slack/Telegram/Feishu integration. Built on LangGraph, MIT licensed, hit #1 GitHub Trending at v2.0.

### [AutoGen](./agent-frameworks/README.md#autogen) ⭐ 56.2k
Microsoft's event-driven multi-agent framework. Agents communicate through typed messages, run as distributed processes across machines, and support both Python and .NET. Ships with AutoGen Studio — a no-code web GUI for building agent pipelines without writing code. MIT, 56.2k stars, enterprise-tested.

### [Dify](./llm-app-builder/README.md#dify) ⭐ 134k
Open-source LLM app platform with visual workflow builder, RAG, agents, and observability. Drag-and-drop pipelines deployable as APIs. One of the highest-starred AI infrastructure projects in existence.

### [AnythingLLM](./llm-app-builder/README.md#anythingllm) ⭐ 56.7k
Self-hosted AI workspace — upload docs, chat with them via RAG, run agents, manage multiple users. Supports 30+ LLM providers and 10+ vector databases. Ships as Docker container or native desktop app. MIT licensed, zero cloud dependency.

### [Gradio](./llm-app-builder/README.md#gradio) ⭐ 42.2k
Build interactive ML/AI web UIs in pure Python — no frontend skills needed. `gr.Interface` for quick demos, `gr.Blocks` for custom layouts, `gr.ChatInterface` for conversational AI. HuggingFace-backed, Apache 2.0, the default interface layer for the entire ML research community.

### [Firecrawl](./web-scraping/README.md#firecrawl) ⭐ 96.1k
Turn any website into clean Markdown or structured JSON for LLM pipelines. Handles JS rendering, auth, rate limits, and anti-bot measures. Output designed for AI consumption — 96.1k stars with only 52 open issues.

### [LightRAG](./rag-frameworks/README.md#lightrag) ⭐ 29.8k
RAG with a knowledge graph layer — extracts entities and relationships from documents then queries both graph and vector store together. Answers questions about *connections* between concepts, not just surface similarity. MIT, LLM-agnostic, multiple storage backends.

### [RAGFlow](./rag-frameworks/README.md#ragflow) ⭐ 76.2k
End-to-end self-hosted RAG platform with layout-aware document parsing, grounded citations, hybrid search, and built-in agents. Deploy via Docker Compose, upload your documents, and query through a chat UI or API. Apache 2.0, 76.2k stars — one of the most starred RAG projects in existence.

### [Qdrant](./vector-databases/README.md#qdrant) ⭐ 29.8k
High-performance vector database built in Rust. HNSW indexing, SIMD acceleration, REST + gRPC APIs, hybrid dense/sparse search. Apache 2.0, self-hostable single container or distributed cluster, client libraries in 6 languages.

### [Milvus](./vector-databases/README.md#milvus) ⭐ 43.5k
Cloud-native distributed vector database for AI at scale. Separated compute/storage, GPU acceleration, Kubernetes-native, billions of vectors. Linux Foundation project, Apache 2.0, last commit March 25 2026.

### [Ragas](./llm-evaluation/README.md#ragas) ⭐ 13.1k
Evaluate RAG pipelines with objective metrics — faithfulness, answer relevancy, context precision. Generates synthetic test datasets from your documents automatically. Apache 2.0, integrates with LangChain, LlamaIndex, and most major LLM frameworks.

### [Home Assistant](./home-automation/README.md#home-assistant) ⭐ 85.7k
The definitive self-hosted smart home platform. Connect 3,000+ device integrations — Zigbee, Z-Wave, Matter, Philips Hue, Apple HomeKit and more — through a unified local interface. 4,672 contributors, monthly releases, Apache 2.0. Your home stays yours.

### [Spec Kit](./ai-dev-tools/README.md#spec-kit) ⭐ 81.1k
GitHub's CLI toolkit for Spec-Driven Development. Write a spec first, then slash commands guide your AI coding agent through planning, task breakdown, and implementation. Works with Claude Code, Cursor, Copilot, Gemini, and 20+ others. Fixes the biggest failure mode of AI-assisted development: jumping to code before the problem is clearly defined.

### [Agent Orchestrator](./ai-dev-tools/README.md#agent-orchestrator) ⭐ 5.3k
Composio's fleet manager for parallel AI coding agents. Each agent gets an isolated git worktree and branch, autonomously handles code, CI failures, and PR creation, while you supervise from a unified dashboard. Pluggable backends (Claude Code, Codex, Aider) and runtimes (tmux, Docker, K8s). Treats your issue backlog like a parallelisable CI pipeline.

### [Keploy](./testing/README.md#keploy) ⭐ 16.6k
eBPF-powered test generation from real traffic — no SDK, no instrumentation, no code changes. Records HTTP calls, database queries, and message queue events at the network layer, then replays them as integration tests with mocked infrastructure. Works with any language or framework, drops into GitHub Actions or Kubernetes CI. Apache 2.0.

### [Strix](./security-testing/README.md#strix) ⭐ 21.3k
Autonomous AI agents for penetration testing — they don't just find potential vulnerabilities, they validate each one through an actual proof-of-concept. Built on Nuclei, Caido, and Playwright with LiteLLM for LLM-agnostic intelligence. pip-installable, CI/CD-compatible, Apache 2.0.

### [Garak](./security-testing/README.md#garak) ⭐ 7.4k
NVIDIA's LLM vulnerability scanner — probes models for jailbreaks, prompt injection, data leakage, hallucination, and toxicity before they hit production. Plugin-based: swap probes, detectors, and generators independently. pip-installable, Apache 2.0, supports 15+ LLM providers.

### [LuxTTS](./voice-cloning/README.md#luxtts) ⭐ 3.2k
Local voice cloning with 48kHz output at 150x realtime — on ~1GB VRAM. Clone any voice from a short reference clip, runs on CUDA, CPU, or Apple MPS. Apache 2.0 with no model licence restrictions, unlike most TTS tools that use CC-BY-NC on their weights.

### [Paperclip](./ai-operations/README.md#paperclip) ⭐ 35.9k
Run autonomous AI agent teams like a company — org charts, per-agent budgets, persistent state, scheduled heartbeats, and multi-tenant isolation. Bring any agent backend (Claude Code, Codex, Cursor, Bash, HTTP). MIT, PostgreSQL-backed, single command to self-host.

### [Aider](./ai-dev-tools/README.md#aider) ⭐ 42.8k
AI pair programming in your terminal — edits your code, commits to git, works with 100+ LLMs. The terminal-native coding assistant that predated every IDE chat panel. Architect + editor mode routes reasoning to a strong model and edits to a fast one. Top of SWE-bench leaderboards. Apache 2.0.

### [ComfyUI](./ai-generation/README.md#comfyui) ⭐ 108k
The most powerful node-based visual engine for AI generation. Wire together model loaders, samplers, ControlNet, LoRA, and upscalers into custom pipelines without code. Supports Stable Diffusion, Flux, SDXL, HunyuanVideo, Stable Audio, and more. Runs entirely offline on NVIDIA, AMD, Intel, or Apple Silicon. GPL-3.0.

### [Uptime Kuma](./monitoring/README.md#uptime-kuma) ⭐ 84.9k
Self-hosted uptime monitoring with a beautiful UI and 90+ notification integrations — Telegram, Discord, Slack, PagerDuty, email, webhooks. Monitors URLs, APIs, Docker containers, DNS, and TCP ports at 20-second intervals. Single Docker container, zero config, publishes public status pages. MIT.

### [Coolify](./self-hosted-infra/README.md#coolify) ⭐ 52.6k
Turn any VPS or bare metal server into your own cloud platform. Deploy apps, databases, and 280+ one-click services (WordPress, Supabase, Ghost, Plausible, and more) via a clean web UI. Handles SSL, reverse proxy, Git deployments, and automated backups. The answer to Heroku's death and Vercel's price cliffs. Apache 2.0.

### [Vaultwarden](./password-manager/README.md#vaultwarden) ⭐ 57.9k
Unofficial Bitwarden server reimplemented in Rust — fully compatible with all official Bitwarden clients, runs in ~10MB of RAM vs the official server's ~2GB. Supports organisations, FIDO2/WebAuthn 2FA, secure file attachments, and an admin panel. Deploy as a single Docker container. AGPL-3.0 with the lowest issue-to-star ratio in this entire collection.

### [Rowboat](./productivity/README.md#rowboat) ⭐ 10k
Local-first AI coworker that ingests your emails and meetings into an editable Markdown knowledge graph, then generates briefs, PDFs, and draft emails grounded in your actual history. Persistent context, transparent working memory, MCP support, any LLM. Apache 2.0.

### [AppFlowy](./productivity/README.md#appflowy) ⭐ 69.1k
Self-hosted Notion alternative built with Flutter and Rust. Rich document editing, grid databases, kanban boards, calendar views, and team wikis — all in one cross-platform app with native desktop (macOS, Windows, Linux) and mobile apps. Local-first data ownership, built-in AI assistant powered by your LLM of choice. AGPL-3.0.

### [Agent-Reach](./agent-tools/README.md#agent-reach) ⭐ 15.4k
Give your AI coding agent internet access across Twitter, Reddit, YouTube, GitHub, Bilibili, and 9+ more platforms with zero API costs. One install command bundles yt-dlp, twitter-cli, Jina Reader, and RSS parsers into a unified CLI agents can call. Works with Claude Code, Cursor, Windsurf, and OpenClaw. MIT, 1.3k forks.

### [Voicebox](./voice-cloning/README.md#voicebox) ⭐ 20.5k
Open-source voice synthesis studio — clone voices, generate speech, edit multi-voice timelines, apply 8 audio effects, all locally. Tauri desktop app + FastAPI backend + React UI. Five engines including LuxTTS, built-in REST API for voice-powered apps. MIT.

### [hermes-agent](./agent-frameworks/README.md#hermes-agent) ⭐ 51.8k
Nous Research's self-improving autonomous agent. Deploys continuously, creates new skills from experience, maintains persistent user memory, and connects to Telegram, Discord, Slack, WhatsApp, and Signal out of the box. The agent you have tomorrow is smarter than the one you deployed today. MIT, 6.7k forks.

### [Postiz](./social-media/README.md#postiz) ⭐ 28.1k
Self-hosted Buffer alternative — schedule across 15+ social platforms (Instagram, X, TikTok, LinkedIn, Discord, and more), analyse metrics, collaborate with teams, and optimise content with AI. Temporal for workflow orchestration means no silent scheduling failures. AGPL-3.0, 5k forks.

### [agent-skills](./agent-tools/README.md#agent-skills) ⭐ 11.9k
Addy Osmani's production engineering workflow system for AI coding agents. 20 skills, 6 phases (Define → Plan → Build → Verify → Review → Ship), 7 slash commands. Encodes real engineering discipline — Hyrum's Law, trunk-based dev, deployment checklists. Works with Claude Code, Cursor, Gemini CLI, Windsurf, OpenCode, and GitHub Copilot. MIT.

### [Graphify](./agent-tools/README.md#graphify) ⭐ 4.2k
Turn any codebase or doc folder into a queryable knowledge graph with 71.5x token reduction vs raw file reading. AST parsing for code structure, semantic extraction for meaning, Leiden clustering for module discovery — outputs an interactive HTML graph, markdown report, and persistent JSON cache. Fully local, no external API. Also cross-listed in CLAUDE-ECOSYSTEM.md. MIT.

### [RedditVideoMakerBot](./automated-video/README.md#redditvideomakerbot) ⭐ 8.7k
The tool that spawned the "Reddit content on TikTok" genre. Give it a subreddit or thread URL and it handles everything: TTS narration, background footage overlay, screenshot rendering, duplicate prevention — and exports a finished video ready to upload. Zero manual editing. GPL-3.0, 2.1k forks, actively maintained.

---

## Recent Additions

| Project | Category | Stars | Added |
|---|---|---|---|
| [Voicebox](./voice-cloning/README.md) | Voice Cloning | 20.5k ⭐ | 2026-04 |
| [hermes-agent](./agent-frameworks/README.md) | Agent Frameworks | 51.8k ⭐ | 2026-04 |
| [Postiz](./social-media/README.md) | Social Media | 28.1k ⭐ | 2026-04 |
| [agent-skills](./agent-tools/README.md) | Agent Tools | 11.9k ⭐ | 2026-04 |
| [Rowboat](./productivity/README.md) | Productivity | 10k ⭐ | 2026-04 |
| [RealtimeSTT](./speech-to-text/README.md) | Speech to Text | 9.6k ⭐ | 2026-04 |
| [AI-Trader](./financial-analysis/README.md) | Financial Analysis | 12.5k ⭐ | 2026-04 |
| [Graphify](./agent-tools/README.md) | Agent Tools | 4.2k ⭐ | 2026-04 |
| [Agent-Reach](./agent-tools/README.md) | Agent Tools | 15.4k ⭐ | 2026-04 |
| [RedditVideoMakerBot](./automated-video/README.md) | Automated Video | 8.7k ⭐ | 2026-04 |
| [AppFlowy](./productivity/README.md) | Productivity | 69.1k ⭐ | 2026-04 |
| [Vaultwarden](./password-manager/README.md) | Password Manager | 57.9k ⭐ | 2026-04 |
| [Coolify](./self-hosted-infra/README.md) | Self-Hosted Infra | 52.6k ⭐ | 2026-04 |
| [Uptime Kuma](./monitoring/README.md) | Monitoring | 84.9k ⭐ | 2026-04 |
| [ComfyUI](./ai-generation/README.md) | AI Generation | 108k ⭐ | 2026-04 |
| [Aider](./ai-dev-tools/README.md) | AI Dev Tools | 42.8k ⭐ | 2026-04 |
| [Paperclip](./ai-operations/README.md) | AI Operations | 35.9k ⭐ | 2026-03 |
| [RAGFlow](./rag-frameworks/README.md) | RAG Frameworks | 76.2k ⭐ | 2026-03 |
| [AutoGen](./agent-frameworks/README.md) | Agent Frameworks | 56.2k ⭐ | 2026-03 |
| [Gradio](./llm-app-builder/README.md) | LLM App Builder | 42.2k ⭐ | 2026-03 |
| [vLLM](./local-llm/README.md) | Local LLM | 74.3k ⭐ | 2026-03 |
| [Qdrant](./vector-databases/README.md) | Vector Databases | 29.8k ⭐ | 2026-03 |
| [Milvus](./vector-databases/README.md) | Vector Databases | 43.5k ⭐ | 2026-03 |
| [AnythingLLM](./llm-app-builder/README.md) | LLM App Builder | 56.7k ⭐ | 2026-03 |
| [Ragas](./llm-evaluation/README.md) | LLM Evaluation | 13.1k ⭐ | 2026-03 |
| [Garak](./security-testing/README.md) | Security Testing | 7.4k ⭐ | 2026-03 |
| [LuxTTS](./voice-cloning/README.md) | Voice Cloning | 3.2k ⭐ | 2026-03 |
| [Strix](./security-testing/README.md) | Security Testing | 21.3k ⭐ | 2026-03 |
| [Keploy](./testing/README.md) | Testing | 16.6k ⭐ | 2026-03 |
| [Agent Orchestrator](./ai-dev-tools/README.md) | AI Dev Tools | 5.3k ⭐ | 2026-03 |
| [Spec Kit](./ai-dev-tools/README.md) | AI Dev Tools | 81.1k ⭐ | 2026-03 |
| [Home Assistant](./home-automation/README.md) | Home Automation | 85.7k ⭐ | 2026-03 |
| [DeerFlow](./agent-frameworks/README.md) | Agent Frameworks | 32.6k ⭐ | 2026-03 |
| [LightRAG](./rag-frameworks/README.md) | RAG Frameworks | 29.8k ⭐ | 2026-03 |
| [Firecrawl](./web-scraping/README.md) | Web Scraping | 96.1k ⭐ | 2026-03 |
| [Dify](./llm-app-builder/README.md) | LLM App Builder | 134k ⭐ | 2026-03 |
| [CrewAI](./agent-frameworks/README.md) | Agent Frameworks | 46.8k ⭐ | 2026-03 |
| [DSPy](./agent-frameworks/README.md) | Agent Frameworks | 33k ⭐ | 2026-03 |
| [Ollama](./local-llm/README.md) | Local LLM | 166k ⭐ | 2026-03 |
| [LlamaFile](./local-llm/README.md) | Local LLM | 23.9k ⭐ | 2026-03 |
| [llm](./local-llm/README.md) | Local LLM | 11.4k ⭐ | 2026-03 |
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
