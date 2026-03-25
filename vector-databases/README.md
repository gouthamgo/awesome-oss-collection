# 🗄️ Vector Databases

Self-hosted vector databases for semantic search, similarity search, and AI application memory.

← [Back to collection](../README.md)

---

### [Qdrant](https://github.com/qdrant/qdrant) ⭐ 29.8k

**High-performance vector database built in Rust — fast, lean, and self-hostable.**

Qdrant stores and queries high-dimensional vectors with attached metadata, enabling semantic search, recommendation systems, image matching, and RAG memory stores. Built entirely in Rust with HNSW indexing, SIMD acceleration, and async I/O via `io_uring`. Exposes REST and gRPC APIs with official client libraries for Python, Go, TypeScript, Rust, Java, and .NET. Deploy as a single container or scale out to a distributed cluster.

**Stack:** Rust, Python (client), REST + gRPC
**License:** Apache 2.0

**Why it's notable:** Qdrant is the vector database you reach for when performance and correctness matter more than hype. The Rust implementation means memory safety with near-zero overhead, and the HNSW + quantization combination gives you fast approximate nearest-neighbour search at any scale. Sparse vector support and hybrid search (dense + sparse) make it suitable for production RAG pipelines that mix semantic and keyword search. Apache 2.0 with no cloud lock-in, 29.8k stars, and an unusually complete client library ecosystem across six languages.

---

### [Milvus](https://github.com/milvus-io/milvus) ⭐ 43.5k

**Cloud-native distributed vector database — built for billions of vectors.**

Milvus is engineered for AI workloads at massive scale: tens of thousands of queries per second across billions of vectors, with GPU acceleration (NVIDIA CAGRA), horizontal scaling, and separated compute/storage for independent elasticity. Supports dense, sparse, and binary vectors with a wide choice of index types (HNSW, IVF, SCANN, DiskANN). Runs as a standalone container for development or as a full Kubernetes cluster for production. Offers Milvus Lite — a lightweight local version — for prototyping without infrastructure.

**Stack:** Go, C++, Kubernetes, pymilvus (Python SDK)
**License:** Apache 2.0

**Why it's notable:** Where Qdrant excels at single-node performance, Milvus is designed from the ground up to scale horizontally. The separated compute/storage architecture means you can scale query throughput and storage independently — critical for production AI systems where data growth outpaces query volume or vice versa. The LFX (Linux Foundation) backing, 43.5k stars, and last commit on March 25 2026 signal an actively maintained, enterprise-grade project rather than a VC-funded side project that may not survive its next funding round.

---
