# 🧰 Agent Tools

Extensions and capabilities for AI coding agents — internet access, platform integrations, and agent enhancement utilities.

← [Back to collection](../README.md)

---

### [Agent-Reach](https://github.com/Panniantong/Agent-Reach) ⭐ 15.4k

**Give your AI coding agent internet access across 14+ platforms — zero API costs.**

A single install command (`npx agent-reach`) bundles a set of free open-source utilities — twitter-cli, yt-dlp, Jina Reader, RSS parsers — and exposes them to your AI agent as a unified CLI toolkit. Agents gain the ability to search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu, and more, transcribe videos, parse RSS feeds, and read any web page. Local credential storage keeps tokens on your machine. Ships with `agent-reach doctor` for diagnosing setup issues. Works with Claude Code, Cursor, Windsurf, and OpenClaw.

**Stack:** Python
**License:** MIT

**Why it's notable:** Most agent internet access solutions require paid API subscriptions — OpenAI's browsing tool, Perplexity API, various search APIs. Agent-Reach takes the opposite approach: assemble the best free open-source utilities and wire them together into a single interface agents can call. The 14+ platform coverage is remarkable for a zero-cost tool, and the fact that it's agent-agnostic (not locked to any single coding assistant) means it works wherever you do. 15.4k stars and 1.3k forks for a utility library is exceptional signal — developers are clearly hungry for this kind of integration.

---

### [Graphify](https://github.com/safishamsi/graphify) ⭐ 4.2k

**Turn any codebase or document folder into a queryable knowledge graph — 71.5x token reduction.**

Point Graphify at any folder and it builds a structured knowledge graph from everything inside: code files (Python, TypeScript, JavaScript, Go, Rust, Java, C/C++), Markdown docs, PDFs, and images. Two-pass extraction — AST-based parsing for code structure, semantic subagents for meaning — produces an interactive HTML graph, a markdown report highlighting "god nodes" and surprising cross-file connections, and a persistent JSON cache for incremental updates. Community detection via Leiden clustering surfaces hidden module boundaries. SHA256 caching means only changed files get reprocessed. Works as a standalone CLI or as an always-on skill registered in CLAUDE.md / AGENTS.md.

**Stack:** Python, NetworkX, tree-sitter, vis.js — fully local, no external API required
**License:** MIT

**Why it's notable:** The core insight is that reading raw files is the wrong interface for understanding a large codebase — a knowledge graph captures *relationships*, not just content. The 71.5x token reduction claim is striking: instead of dumping thousands of lines into context, an agent queries the graph for what it actually needs. Supports Claude Code, Codex, OpenCode, OpenClaw, and Factory Droid — not locked to any single agent. Transparent confidence scoring (EXTRACTED / INFERRED / AMBIGUOUS tags on every relationship) means you know when the graph is certain vs. guessing. 4.2k stars, v0.3.4 released April 7, 2026 — active and shipping.

---

### [agent-skills](https://github.com/addyosmani/agent-skills) ⭐ 11.9k

**Production-grade engineering workflows for AI coding agents — 20 skills across the full development lifecycle.**

Structures software engineering into 6 phases (Define → Plan → Build → Verify → Review → Ship) with 20 purpose-built skills covering each step. Drop it into your agent via a single slash command and it brings 3 engineering personas, 4 reference checklists, and 7 slash commands that encode real production discipline: Hyrum's Law awareness, trunk-based development, API contract verification, and pre-flight deployment checklists. Works with Claude Code, Cursor, Gemini CLI, Windsurf, OpenCode, and GitHub Copilot. By Addy Osmani (engineering lead at Google Chrome).

**Stack:** Shell (workflow definitions and slash command scripts)
**License:** MIT

**Why it's notable:** Most "AI coding tips" resources are informal advice. agent-skills is a structured engineering system — each skill has explicit inputs, step-by-step workflows, verification requirements, and red flag indicators. The 6-phase lifecycle maps to how real engineering teams ship software, not how tutorials teach it. Cross-agent support means it's not locked to any one tool. 11.9k stars and 1.4k forks signals this resonated broadly — developers recognize the gap between "AI writes code" and "AI ships production-quality code", and this is one of the most serious attempts to close it.

---
