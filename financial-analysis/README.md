# 📈 Financial Analysis

AI-powered tools for analysing markets, stocks, and investment decisions.

← [Back to collection](../README.md)

---

### [AI Hedge Fund](https://github.com/virattt/ai-hedge-fund) ⭐ 49.4k

**Multi-agent stock analysis system modelled on legendary investor philosophies.**

12 AI agents — each embodying an investing style (Warren Buffett, Cathie Wood, and others) — independently analyse a stock across valuation, fundamentals, sentiment, and technicals, then a portfolio manager agent synthesises their signals into a final recommendation. Includes backtesting, a web UI, and CLI. Supports multiple LLM providers.

**Stack:** Python · TypeScript · Poetry
**License:** MIT
**Note:** Educational and research purposes only — does not execute real trades.

**Why it's notable:** Most "AI trading" repos are thin wrappers around a single model. This one simulates competing investment philosophies debating the same stock — the multi-agent architecture is what makes it interesting. 49.4k stars and still actively developed signals this hit a genuine gap. The educational-only constraint is the responsible call, not a limitation.

---

### [Daily Stock Analysis](https://github.com/ZhuLinsen/daily_stock_analysis) ⭐ 24k

**Automated daily AI stock analysis with push notifications — A-shares, HK, and US markets.**

Runs daily via GitHub Actions (zero cost), pulls live technical indicators, fundamentals, and news sentiment, then uses an LLM to generate a structured decision dashboard with buy/sell signals, entry/exit points, and an action checklist. Results push to WeChat, Feishu, Telegram, Discord, Slack, or email. Supports smart stock import via image OCR, CSV, or clipboard. Uses LiteLLM under the hood for model routing.

**Stack:** Python · FastAPI · React · LiteLLM · AkShare · YFinance · Tushare
**License:** MIT
**Markets:** A-shares (primary) · Hong Kong · US stocks and indices
**Note:** Designed primarily for Chinese market investors — WeChat/Feishu are first-class notification targets.

**Why it's notable:** Different job from AI Hedge Fund — this is an *operational automation pipeline*, not an analysis framework. The GitHub Actions approach means zero infrastructure cost for daily analysis. 454 commits and only 34 open issues suggests serious engineering care behind what is a lot of moving parts.

---
