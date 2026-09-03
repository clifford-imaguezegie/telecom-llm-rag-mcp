# Module 1 Architecture — Standalone LLM Baseline

Module 1 is the project's frozen **standalone LLM** baseline.

```text
Benchmark Question
       |
       +--------------------+
       |                    |
       v                    v
EssentialAI/rnj-1      OTel 1.0
       |                    |
       +---------+----------+
                 |
                 v
         Comparative Evaluation
```

## Scope

In scope:
- standalone model loading and inference;
- common generation conditions where technically practical;
- Track 1 and Track 2 benchmark creation;
- independent Track 1 LLM judging;
- expert telecom review;
- cross-track comparison.

Out of scope:
- RAG;
- vector retrieval;
- MCP;
- external tools;
- agentic or autonomous workflows.

The benchmark questions established here are frozen and reused in Module 2. Canonical copies are stored under `benchmarks/module_1_2/`.
