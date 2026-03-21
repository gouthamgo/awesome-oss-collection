# 🔀 LLM Gateway

Unified interfaces and proxies for routing between multiple LLM providers.

← [Back to collection](../README.md)

---

### [LiteLLM](https://github.com/BerriAI/litellm) ⭐ 39.8k

**One interface for 100+ LLMs — Python SDK and production-grade proxy server.**

Call OpenAI, Anthropic, Azure, Bedrock, VertexAI, and 100+ other models with the same API format. Use it as a Python library to standardise LLM calls in your codebase, or deploy the proxy server as an AI gateway with virtual keys, cost tracking per team, load balancing across providers, automatic retries, and guardrails. 8ms P95 latency at 1k requests/sec.

**Stack:** Python · Docker
**License:** MIT (core) · Custom enterprise license (enterprise/ directory only)
**Integrations:** LangChain · LlamaIndex · Langfuse · MLflow · MCP · A2A protocol

**Why it's notable:** Switching LLM providers normally means rewriting API calls. LiteLLM eliminates that entirely — one format, any model, anywhere. It's become the de facto standard for teams that need provider flexibility without vendor lock-in. The proxy mode turns it into a serious production gateway: auth, spend limits, observability, and failover all in one place. Committed to daily, used by companies running at scale.

---
