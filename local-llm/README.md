# 🧠 Local LLM

Tools for running large language models locally — no cloud, no API keys, no data leaving your machine.

← [Back to collection](../README.md)

---

### [Ollama](https://github.com/ollama/ollama) ⭐ 166k

**Run open-source LLMs locally with one command.**

Pull and run Llama, Mistral, Gemma, Qwen, and 100+ other models as easily as `ollama run llama3`. Exposes a local REST API compatible with the OpenAI format, so any tool built for OpenAI works against your local model. Cross-platform (macOS, Windows, Linux), GPU-accelerated, and the de facto standard for local LLM deployment.

**Stack:** Go
**License:** MIT
**Platforms:** macOS · Windows · Linux

**Why it's notable:** Ollama removed every barrier to running LLMs locally. One command downloads the model, manages quantization, and starts a server — no Python environment, no CUDA setup required. 166k stars is one of the highest in this entire collection and the community signal is real: this is the tool that made local AI accessible to everyone.

---

### [LlamaFile](https://github.com/Mozilla-Ocho/llamafile) ⭐ 23.9k

**LLM as a single executable — download one file, run everywhere.**

Mozilla-backed project that bundles an LLM and its runtime into a single binary using Cosmopolitan Libc. Download it, make it executable, run it — works on macOS, Windows, Linux, FreeBSD, and more, on both x86 and ARM, without installing anything. Supports GPU acceleration when available, falls back to CPU otherwise.

**Stack:** C++ · Shell
**License:** Apache 2.0
**Platforms:** macOS · Windows · Linux · FreeBSD · OpenBSD (x86 + ARM)

**Why it's notable:** Ollama is the best tool for running models as a service. LlamaFile is the best tool for distributing a model as a self-contained artifact — share one file and anyone can run the model anywhere, no setup at all. The "LLM as executable" concept is genuinely novel and Mozilla's backing gives it institutional credibility.

---

### [llm](https://github.com/simonw/llm) ⭐ 11.4k

**Lightweight CLI and Python library for interacting with LLMs — local and remote.**

Simon Willison's tool for running prompts against any LLM from the terminal or Python. Supports OpenAI, Anthropic, Google, and 50+ providers via plugins, plus local models via Ollama. Logs every prompt and response to SQLite for a permanent searchable history. Simple, composable, and built around the Unix philosophy.

**Stack:** Python
**License:** Apache 2.0
**Platforms:** macOS · Windows · Linux

**Why it's notable:** LiteLLM is for routing in production systems. llm is for humans at the terminal who want to query any model with one command and keep a history of everything they've asked. The SQLite logging is quietly one of the most useful features — a permanent record of every interaction, searchable and exportable.

---
