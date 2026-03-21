# 📄 File to Markdown

Tools for converting documents, files, and other formats into Markdown — useful for feeding content into LLMs, building pipelines, or just getting clean text out of messy formats.

← [Back to collection](../README.md)

---

### [MarkItDown](https://github.com/microsoft/markitdown) ⭐ 91.2k

**Convert almost any file format to Markdown — built by Microsoft.**

Drop in a PDF, Word doc, Excel sheet, PowerPoint, image, audio file, HTML page, YouTube URL, or CSV and get clean, structured Markdown back. Designed specifically for LLM workflows where you need to feed document content to a model without losing structure. Has both a CLI and a Python API, plus a plugin system for extending to new formats.

**Stack:** Python
**License:** MIT
**Supported formats:** PDF · DOCX · XLSX · PPTX · Images · Audio · HTML · CSV · JSON · XML · ZIP · YouTube URLs · EPubs

**Why it's notable:** 91k stars in a short time tells you this filled a real gap. The LLM-first design philosophy is what separates it — it doesn't just dump raw text, it preserves headings, tables, and lists as proper Markdown so the structure survives into the model's context. Azure Document Intelligence and OCR support via plugins means it handles scanned docs too. Microsoft backing means it's not going anywhere.

---
