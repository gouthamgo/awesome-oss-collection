# 📚 RAG Frameworks

Retrieval-Augmented Generation frameworks — tools for grounding LLMs in your own documents and data.

← [Back to collection](../README.md)

---

### [LightRAG](https://github.com/hkuds/lightrag) ⭐ 29.8k

**RAG with a knowledge graph layer — dual-level retrieval for richer, more relational answers.**

Standard RAG chunks documents into vectors and retrieves by semantic similarity. LightRAG goes further: it extracts entities and relationships from your documents to build a knowledge graph, then queries both the graph and the vector store together. The result is answers that understand *connections* between concepts, not just surface similarity. Supports PostgreSQL, MongoDB, Neo4j, Milvus, Chroma, Faiss, and more as storage backends. LLM-agnostic — works with OpenAI, local models via Ollama, or any compatible API.

**Stack:** Python 3.10+ · NetworkX · Neo4j · PostgreSQL · Milvus · Chroma · Faiss · Qdrant
**License:** MIT
**Integrations:** Ollama · OpenAI · BAAI embedding models · REST API

**Why it's notable:** The limitation of pure vector RAG is that it misses relationships — "how does concept A connect to concept B?" isn't answerable by similarity search alone. LightRAG's knowledge graph layer fills that gap. Research-backed from HKU, 29.8k stars, and MIT licensed. The dual-level retrieval (local for specific facts, global for high-level synthesis) maps to how humans actually reason about complex documents.

---

### [RAGFlow](https://github.com/infiniflow/ragflow) ⭐ 76.2k

**End-to-end self-hosted RAG platform — deep document understanding, grounded citations, built-in agents.**

RAGFlow is a complete, deployable RAG engine: upload documents (PDFs, Word, Excel, slides, images, web pages), watch it intelligently chunk them with layout-aware parsing, then query through a chat interface or API with citations grounded in the actual source text. Supports hybrid search (dense + sparse), human-in-the-loop chunk review, and an agentic mode for multi-step reasoning. Backs everything on Elasticsearch/Infinity + MySQL + MinIO, deployable via Docker Compose.

**Stack:** Python, Go, React, Elasticsearch/Infinity, MySQL, MinIO, Docker
**License:** Apache 2.0

**Why it's notable:** LightRAG is a Python library you integrate into your own application. RAGFlow is the complete platform you deploy and hand to users. The difference is the document understanding layer: RAGFlow's parser preserves the structure of complex documents — tables, charts, headers, footers — rather than naively splitting by token count, which is why it produces grounded citations rather than hallucinated paraphrases. 76.2k stars makes it one of the most starred RAG projects in existence, and the Apache 2.0 licence means you can deploy it commercially without restrictions.

---
