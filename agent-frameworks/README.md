# 🕸️ Agent Frameworks

Frameworks for building, orchestrating, and deploying AI agents.

← [Back to collection](../README.md)

---

### [CrewAI](https://github.com/crewAIInc/crewAI) ⭐ 46.8k

**Multi-agent framework where agents have roles, goals, and backstories.**

Define a crew of AI agents — each with a role (Researcher, Writer, Analyst), a goal, and a backstory — then assign them tasks and let them collaborate. Agents can use tools, delegate to each other, and produce structured outputs. Lightweight, fast, and designed to feel intuitive rather than graph-theoretical.

**Stack:** Python
**License:** MIT

**Why it's notable:** Most multi-agent frameworks feel like wiring up a graph database. CrewAI's role/goal/backstory model maps to how humans think about teams — which is exactly why 46.8k developers reached for it. The simplicity is the feature: you can get a working crew in an afternoon. MIT license, active daily development, and a clear niche that doesn't overlap with lower-level frameworks.

---

### [DSPy](https://github.com/stanfordnlp/dspy) ⭐ 33k

**Program language models instead of prompting them.**

Stanford NLP's framework for building LLM-powered systems as programs rather than prompt strings. Define modules with typed signatures, chain them together, then let DSPy's optimizers automatically tune the prompts and few-shot examples to maximise performance on your metric. Replaces brittle hand-written prompts with compiled, optimised pipelines.

**Stack:** Python
**License:** MIT

**Why it's notable:** The insight that prompting is really a form of programming — and that programs can be optimised — is the key shift DSPy introduces. Instead of manually tweaking "say this, then say that", you define what you want and let the optimizer find the best way to get it. Stanford NLP backing and 33k stars signal this is academically serious and practically useful.

---

### [DeerFlow](https://github.com/bytedance/deer-flow) ⭐ 32.6k

**ByteDance's open-source super agent platform — deploy it, don't wire it.**

A complete, deployable agentic AI platform built on LangGraph. Spin it up with Docker and you get a full-stack web UI where agents autonomously research topics, execute code in isolated sandboxes, write reports, generate slides, and coordinate as sub-agents on complex tasks. Supports any LLM (Claude, GPT-4, DeepSeek, Gemini), ships with long-term memory, and integrates directly with Slack, Telegram, and Feishu.

**Stack:** Python 3.12+, Node.js 22+, LangGraph, LangChain, Docker, Kubernetes
**License:** MIT

**Why it's notable:** CrewAI and DSPy give you primitives to build agent systems — DeerFlow gives you the finished platform. ByteDance shipped this to #1 on GitHub Trending at v2.0 with 32.6k stars, and the February 2026 release shows it's in active production development, not maintenance mode. The sandboxed code execution environment is the piece that elevates it: agents can write and run arbitrary code safely without touching your host system. For teams that want to deploy an internal research agent rather than engineer one from scratch, this is the starting point.

---

### [AutoGen](https://github.com/microsoft/autogen) ⭐ 56.2k

**Microsoft's event-driven multi-agent framework — distributed, cross-language, with a no-code Studio.**

AutoGen builds multi-agent systems around an event-driven, message-passing architecture rather than a role/crew metaphor. Agents communicate through typed messages, can run as distributed processes across machines, and support both Python and .NET. Ships in three layers: Core (low-level message passing), AgentChat (higher-level patterns for rapid prototyping), and AutoGen Studio (a no-code web GUI for building and testing agent pipelines without writing code). Integrates with MCP for tool access and external APIs.

**Stack:** Python 3.10+, .NET, TypeScript (Studio), event-driven runtime
**License:** MIT

**Why it's notable:** CrewAI maps to how humans think about teams. AutoGen maps to how distributed systems engineers think about services — message passing, event streams, independent processes. The architectural difference matters at scale: AutoGen agents can run on separate machines, handle async workflows, and be mixed across Python and .NET codebases. The no-code Studio lowers the floor for non-engineers. Microsoft-backed at 56.2k stars with 471 open issues — a well-maintained, enterprise-tested project that predates most of the current agent framework wave.

---
