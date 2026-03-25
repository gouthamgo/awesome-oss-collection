# 📊 LLM Evaluation

Tools for measuring, testing, and improving the quality of LLM applications — RAG pipelines, agents, and generative outputs.

← [Back to collection](../README.md)

---

### [Ragas](https://github.com/explodinggradients/ragas) ⭐ 13.1k

**Evaluate RAG pipelines with objective metrics — automatically.**

Ragas provides a suite of evaluation metrics specifically designed for Retrieval-Augmented Generation systems: faithfulness (does the answer match the retrieved context?), answer relevancy, context precision, context recall, and more. Feed it your questions, answers, and retrieved chunks — Ragas scores each dimension using LLM-based evaluators and statistical measures. Also generates synthetic test datasets from your document corpus so you don't need to hand-craft evaluation sets.

**Stack:** Python, LangChain-compatible, async-native
**License:** Apache 2.0

**Why it's notable:** RAG systems are notoriously hard to evaluate — "does this answer seem right?" is not a reproducible metric. Ragas replaces gut feel with standardised, reproducible scores. The automatic test dataset generation is the underrated feature: instead of spending weeks building evaluation sets by hand, Ragas generates them from your actual documents, exposing failure modes that human-crafted tests would miss. 13.1k stars, 3,500+ downstream dependents, and integration with LangChain, LlamaIndex, and most major LLM frameworks makes it the de facto evaluation layer for production RAG.

---
