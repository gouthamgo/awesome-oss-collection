# 🔐 Security Testing

AI-powered tools for automated penetration testing, vulnerability discovery, and security assessment.

← [Back to collection](../README.md)

---

### [Strix](https://github.com/usestrix/strix) ⭐ 21.3k

**Autonomous AI agents that find and validate security vulnerabilities — like a real pen tester.**

Strix deploys multiple AI agents to autonomously conduct security assessments: they run your code dynamically, identify vulnerabilities, and validate each finding through an actual proof-of-concept rather than flagging theoretical issues. Built on top of proven security primitives — Nuclei for vulnerability scanning, Caido for HTTP interception, Playwright for browser automation — with LiteLLM providing LLM-agnostic intelligence across the whole stack. Install via pip, point it at a target, and get a structured vulnerability report with validated findings.

**Stack:** Python, LiteLLM, Nuclei, Caido, Playwright, Docker
**License:** Apache 2.0

**Why it's notable:** Most security scanners produce a wall of theoretical warnings that require a human to validate one by one. Strix closes that loop automatically — agents don't just find a potential SQL injection, they attempt to exploit it and confirm it's real before reporting. The foundation on established tools (Nuclei has 23k+ stars of its own) means the detection primitives are battle-tested; the AI layer adds autonomous reasoning and validation on top. Apache 2.0, pip-installable, CI/CD-compatible, and 21.3k stars with only 39 open issues points to a carefully maintained project that's being used in production.

---

### [Garak](https://github.com/NVIDIA/garak) ⭐ 7.4k

**LLM vulnerability scanner — find jailbreaks, prompt injections, and data leakage before your users do.**

Garak is the nmap for LLMs: a modular security testing framework that probes language models for failure modes including prompt injection, jailbreaks, data leakage, hallucination, toxicity generation, and misinformation. Run it against any model — local (via Ollama or HuggingFace) or cloud (OpenAI, Anthropic, Bedrock, Cohere, Groq) — and get a structured report of what it can be made to do. Plugin-based architecture: swap probes, detectors, generators, and evaluators independently.

**Stack:** Python, plugin architecture, supports 15+ LLM providers
**License:** Apache 2.0

**Why it's notable:** Strix tests your web applications for vulnerabilities. Garak tests your LLMs themselves — a fundamentally different attack surface. As organisations ship AI-powered products, the model becomes the security boundary: can it be manipulated into leaking training data? Can it be jailbroken to bypass safety controls? Can it be prompted into generating harmful content? Garak answers those questions systematically before production, not after an incident. NVIDIA-backed, Apache 2.0, pip-installable, and built with the same mental model as established security tooling (probes, detectors, harnesses) so security teams don't need to learn a new paradigm.

---
