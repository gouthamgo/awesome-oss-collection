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
