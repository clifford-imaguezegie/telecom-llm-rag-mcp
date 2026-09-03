# Module 2 Architecture — Telecom RAG V1

Module 2 introduces Retrieval-Augmented Generation while preserving the Module 1 benchmark.

```text
Question
   |
   +----------------------+
   |                      |
   v                      v
Standalone LLM        RAG V1
                          |
                    BGE-M3 Embedding
                          |
                         FAISS
                          |
                       Top-7
                          |
                    Retrieved Evidence
                          |
                         LLM
```

## Frozen RAG V1

- Embedding model: `BAAI/bge-m3`
- Embedding dimension: 1,024
- Vector store: FAISS
- Indexed vectors: approximately 1.5 million
- Retrieval baseline: Top-7 chunks

## Evaluated systems

1. Essential AI + RAG V1
2. Essential AI LLM-only
3. OTel 2.0 LLM-only
4. Gemma 4 LLM-only
5. Gemma 4 + RAG V1

## Notebook roles

| Notebook | Role |
|---|---|
| 02 | Build corpus/chunks/embeddings/FAISS and validate retrieval |
| 03 | EssentialAI + RAG V1 |
| 04 | EssentialAI LLM-only |
| 05 | OTel 2.0 LLM-only |
| 06 | Gemma 4 LLM-only |
| 07 | Gemma 4 + RAG V1 |
| 08 | Final cross-system evaluation and RAG diagnostics |

RAG V1 is retained as a frozen experimental baseline. Later modules do not retroactively alter these results.
