# 🏢 AI Operations

Platforms for orchestrating and governing autonomous AI agents at the organisational level — budgets, goals, org charts, and multi-agent coordination.

← [Back to collection](../README.md)

---

### [Paperclip](https://github.com/paperclipai/paperclip) ⭐ 35.9k

**Run autonomous AI agents like a company — with org charts, budgets, and governance.**

Paperclip is a control plane for coordinating fleets of AI agents toward shared business goals. Define an organisational structure, assign agents to roles, set per-agent budgets, and let them execute tasks autonomously — while Paperclip enforces cost limits, maintains persistent state across sessions, schedules recurring work via heartbeats, and isolates data across teams or customers. Bring any agent backend: Claude Code, Codex, Cursor, Bash, or any HTTP-accessible agent. Self-host with a single `npx paperclipai onboard` command; backs everything on PostgreSQL.

**Stack:** TypeScript, Node.js, React, PostgreSQL
**License:** MIT

**Why it's notable:** Agent frameworks like CrewAI and AutoGen give you primitives to build multi-agent systems in code. Paperclip operates one level higher — it's the management layer that answers "who's doing what, how much are they spending, and what's the goal?" The org chart metaphor maps directly to how businesses think about teams, which is why the budget enforcement and goal-tracking features exist alongside the agent coordination. 35.9k stars and MIT licensed, actively maintained, and the "any agent, any runtime" philosophy means it's not locked to a single AI provider.

---
