# 🏗️ LLM App Builder

Platforms for building, deploying, and managing LLM-powered applications.

← [Back to collection](../README.md)

---

### [Dify](https://github.com/langgenius/dify) ⭐ 134k

**Open-source platform for building LLM apps with workflows, RAG, agents, and observability — all in one.**

Visual workflow builder for LLM pipelines: drag nodes for prompts, tools, loops, conditions, and RAG retrievers, then deploy as an API or chat interface. Includes a knowledge base engine for document ingestion and retrieval, a built-in agent mode, model provider management, and a full observability dashboard. Self-hostable via Docker.

**Stack:** Python · TypeScript · Docker
**License:** Apache 2.0
**Deployment:** Self-hosted (Docker) · Cloud

**Why it's notable:** Dify sits at the intersection of no-code and pro-code LLM development. The visual workflow editor lowers the floor — non-engineers can build RAG pipelines — while the API and Python SDK keep the ceiling high for developers. 134k stars is one of the highest in the entire AI infrastructure space, and the rate of development is relentless. If you're building anything with LLMs at the application layer, this is what you evaluate first.

---

### [AnythingLLM](https://github.com/Mintplex-Labs/anything-llm) ⭐ 56.7k

**Self-hosted AI workspace — chat with your docs, run agents, multi-user, no cloud needed.**

AnythingLLM is a fully self-hosted AI assistant platform: ingest documents (PDF, Word, TXT, URLs), chat with them via RAG, run autonomous agents, and manage multiple users with role-based access — all from a clean web UI. Supports 30+ LLM providers (OpenAI, Anthropic, Ollama, Azure, AWS Bedrock and more) and 10+ vector databases (Qdrant, Milvus, Chroma, LanceDB). Ships as a Docker container, desktop app (Mac, Windows, Linux), or cloud deployment.

**Stack:** Node.js, React/Vite, LanceDB (default), Docker
**License:** MIT
**Deployment:** Self-hosted (Docker) · Desktop app · Cloud

**Why it's notable:** Dify is for engineers building LLM workflows. AnythingLLM is for teams that just want a self-hosted ChatGPT with their own documents. The distinction matters: no workflow editor, no visual pipelines — just upload your files and start chatting, with full control over which LLM and vector store backs it. 56.7k stars with MIT licence and desktop apps for all three platforms means it's genuinely accessible to non-technical users who want data sovereignty without any cloud dependency.

---

### [Gradio](https://github.com/gradio-app/gradio) ⭐ 42.2k

**Build interactive ML and AI web UIs in pure Python — no frontend skills required.**

Gradio lets you wrap any Python function, ML model, or LLM in a shareable web interface with a few lines of code. Three building blocks cover most use cases: `gr.Interface` for quick single-function demos, `gr.Blocks` for custom multi-component layouts, and `gr.ChatInterface` for conversational AI. Built-in component library handles text, images, audio, video, files, dataframes, and plots. Share publicly via a built-in tunnel link or deploy to HuggingFace Spaces, Docker, or any server.

**Stack:** Python, FastAPI, Svelte/Vite, Tailwind CSS
**License:** Apache 2.0

**Why it's notable:** Gradio solves the fastest possible path from "working model" to "shareable demo." No JavaScript, no React, no deployment pipeline — just Python. It's why HuggingFace Spaces is filled with interactive AI demos: Gradio is the default interface layer for the entire ML research community. 42.2k stars, JavaScript and Python client libraries, and native HuggingFace integration make it the tool teams reach for when they need to go from notebook to web UI in an afternoon without compromising on interactivity.

---
