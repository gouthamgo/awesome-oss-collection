# 🛠️ AI Dev Tools

Tools that augment the software development workflow with AI — spec generation, planning, implementation, and code automation.

← [Back to collection](../README.md)

---

### [Spec Kit](https://github.com/github/spec-kit) ⭐ 81.1k

**Turn specifications into working software — spec-driven development with AI.**

A CLI toolkit from GitHub that implements Spec-Driven Development: a structured workflow where you write a human-readable specification first, then use AI to generate a plan, break it into tasks, and implement each one. Install the `specify` CLI, and a set of slash commands (`/speckit.specify`, `/speckit.plan`, `/speckit.tasks`, `/speckit.implement`) guide you through the entire cycle inside your AI coding agent of choice — Claude Code, Cursor, GitHub Copilot, Gemini, and 20+ others.

**Stack:** Python (`specify` CLI), git-native, works with any AI coding agent
**License:** MIT

**Why it's notable:** Spec Kit addresses the biggest failure mode in AI-assisted development: jumping straight to implementation without a clear specification. By making the spec the source of truth — executable, versioned, and agent-readable — it brings engineering discipline to vibe-coding workflows. GitHub built this internally before open-sourcing it, and 81.1k stars in its first months signals strong developer resonance. It's not a framework you adopt once and forget; it's a workflow pattern that scales from solo projects to team codebases, and the multi-agent support means it's not locked to any single AI tool.

---

### [Agent Orchestrator](https://github.com/ComposioHQ/agent-orchestrator) ⭐ 5.3k

**Run a fleet of parallel AI coding agents across git branches — autonomously.**

Spin up dozens of AI coding agents simultaneously, each working in its own isolated git worktree on a separate branch. The orchestrator coordinates them across the full development loop: writing code, resolving CI failures, responding to review comments, and opening PRs — while you supervise from a unified dashboard and step in only when judgment is needed. Pluggable architecture supports Claude Code, Codex, and Aider as agent backends, with tmux, Docker, or Kubernetes as runtimes, and GitHub or Linear for issue tracking.

**Stack:** TypeScript, Node.js, Git worktrees, tmux/Docker/Kubernetes
**License:** MIT

**Why it's notable:** Most "AI coding" tools are single-agent — you give one agent a task and wait. Agent Orchestrator treats coding as a parallelisable workload, the same way CI pipelines parallelise test runs. The isolated worktree-per-agent model means agents can't step on each other, and the CI feedback loop means failures get resolved without human intervention. Built by Composio (a serious AI tooling company), 3,288 test cases, and the plugin architecture means it's not locked to any single agent or cloud provider. For teams drowning in a backlog of well-defined issues, this is the leverage point.

---
