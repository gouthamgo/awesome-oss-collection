# 📑 PDF Parsing

Tools for extracting structured data from PDFs — beyond basic text dumps, into accurate, layout-aware extraction.

← [Back to collection](../README.md)

---

### [OpenDataLoader PDF](https://github.com/opendataloader-project/opendataloader-pdf) ⭐ 7.3k

**Accurate, structure-aware PDF extraction to Markdown, JSON, and HTML.**

Parses PDFs using an XY-Cut++ reading order algorithm to produce properly ordered text — not just raw character dumps. Outputs Markdown, JSON with bounding boxes, or HTML. Handles scanned docs via OCR (80+ languages), extracts LaTeX formulas, describes charts and images via AI, and includes a hybrid mode that routes complex pages to an AI backend for benchmark-topping accuracy (0.90 overall, 0.93 for tables). Python and Node.js SDKs available, with LangChain integration.

**Stack:** Java 11+ (core) · Python SDK · Node.js SDK
**License:** Apache 2.0
**Note:** Hybrid AI mode requires an external API backend; local-only mode works fully offline.

**Why it's notable:** Most PDF parsers just dump text in the wrong order and call it done. The XY-Cut++ reading order, bounding box output, and formula extraction make this genuinely useful for complex documents — financial reports, academic papers, technical manuals — where structure matters. The #1 benchmark accuracy for table extraction is the headline claim, and the 15 open issues suggest the team is actually on top of it.

---
