# Module 4 Changelog

## 2026-09-05 — Module 4 v1.0

- Completed frozen 16-question Module 4 benchmark.
- Added three formal generators: Gemma 4 12B, Qwen3.8 27B and Qwen3.5 9B.
- Implemented natural `RAG_ONLY` / `MCP_ONLY` / `HYBRID` route selection.
- Implemented adaptive requirement-bounded evidence retrieval with a three-round cap.
- Implemented concurrent Hybrid RAG+MCP retrieval and RRF fusion.
- Completed 48/48 formal generator cases.
- Qualified IBM Granite 4.2 8B as the independent blind judge.
- Preserved 47/48 valid formal judge results; Gemma Q16 remains an explicit missing observation after schema-validation failure.
- Added deterministic Cell 12D and Cell 13 CPU analysis.
- Archived complete experiment artifacts to Google Drive and a versioned Kaggle dataset.
- Cleaned the executed master notebook for GitHub without altering any executed code cell or output.
