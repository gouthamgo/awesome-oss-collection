# 🧪 Testing

Tools for automated test generation, API testing, and integration testing — without writing tests by hand.

← [Back to collection](../README.md)

---

### [Keploy](https://github.com/keploy/keploy) ⭐ 16.6k

**Auto-generate tests and mocks by recording real traffic — zero code changes required.**

Keploy sits at the network layer using eBPF and intercepts your application's actual traffic — HTTP calls, database queries (PostgreSQL, MySQL, MongoDB), message queue events (Kafka, RabbitMQ), gRPC, GraphQL — then replays them as automated test cases with mocked dependencies. No SDKs to install, no instrumentation, no code changes. Record once in development, replay in CI to catch regressions across the full integration surface.

**Stack:** Go, eBPF, Docker, Kubernetes — language-agnostic (Go, Java, Node.js, Python, Rust, C#, PHP, Ruby, and more)
**License:** Apache 2.0

**Why it's notable:** The eBPF network-layer approach is the key insight: instead of asking developers to write tests or instrument their code, Keploy captures what the application *actually does* under real conditions and turns that into a reproducible test suite. It mocks the entire infrastructure stack — not just HTTP endpoints, but databases, queues, and caches — so tests run without external dependencies. The result is integration test coverage that reflects production behaviour rather than what a developer imagined production would look like. 16.6k stars, Apache 2.0, works with any language or framework, and drops straight into GitHub Actions or Kubernetes CI pipelines.

---
