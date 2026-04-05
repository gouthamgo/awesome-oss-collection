# 📡 Monitoring

Self-hosted tools for monitoring uptime, performance, and availability — with alerts when things go wrong.

← [Back to collection](../README.md)

---

### [Uptime Kuma](https://github.com/louislam/uptime-kuma) ⭐ 84.9k

**Self-hosted uptime monitoring with a beautiful UI and 90+ notification services.**

Uptime Kuma monitors your websites, APIs, databases, Docker containers, DNS records, and TCP ports at 20-second intervals, then alerts you the moment something goes down. Ship it as a Docker container, connect 90+ notification channels (Telegram, Discord, Slack, PagerDuty, email, webhooks), and publish public status pages for your users — all from a clean, reactive web interface. No external services, no data leaving your server.

**Stack:** JavaScript, Vue.js, Node.js, Docker
**License:** MIT

**Why it's notable:** Self-hosted monitoring has historically meant wrestling with Prometheus + Grafana or paying for Pingdom. Uptime Kuma does the job 95% of teams actually need — "is this URL up and does someone get paged when it isn't?" — in a single Docker container with zero config. The 90+ notification integrations mean it fits whatever alerting setup you already have. 84.9k stars with only 662 open issues is a remarkably healthy ratio for a tool at this scale, and the MIT licence means it's genuinely free to run in production.

---
