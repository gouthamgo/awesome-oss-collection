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

### [vLLM](https://github.com/vllm-project/vllm) ⭐ 74.3k

**Production-grade LLM inference engine — high throughput, low latency, multi-GPU.**

vLLM is the engine for serving LLMs in production at scale. Its PagedAttention memory management eliminates KV cache fragmentation, and continuous batching keeps GPUs saturated across concurrent requests. Serves models across multiple GPUs with tensor and pipeline parallelism, supports quantization (GPTQ, AWQ), speculative decoding, and is fully OpenAI API-compatible. Drop-in replacement for the OpenAI endpoint — any client that works with OpenAI works with vLLM.

**Stack:** Python, CUDA, C++, PyTorch
**License:** Apache 2.0
**Platforms:** NVIDIA GPU · AMD GPU · Intel · ARM · TPU

**Why it's notable:** Ollama makes local LLMs easy for one user. vLLM makes them fast for hundreds. The PagedAttention breakthrough (from a UC Berkeley paper) is why vLLM became the industry standard for production LLM serving — it manages GPU memory the way virtual memory manages RAM, eliminating the throughput bottleneck that plagued earlier serving frameworks. At 74.3k stars it's one of the most starred projects in the entire AI infrastructure space, with adoption at Google, Microsoft, and most major AI labs.

---
