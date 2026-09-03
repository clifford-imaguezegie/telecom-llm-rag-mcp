# Telecom RAG V1 Benchmark Summary

## Benchmark Scope

RAG V1 was evaluated using the same benchmark foundation established during the initial LLM baseline:

- **Track 1:** 20 custom telecom engineering questions
- **Track 2:** 32 industry-oriented telecom benchmark questions

Five system configurations were evaluated:

1. Essential AI + RAG
2. Essential AI Only
3. Otel 2.0 Only
4. Gemma 4 Only
5. Gemma 4 + RAG

---

## Track 1 Results

| Rank | System | Mean Score |
|---|---|---:|
| 1 | Otel 2.0 Only | **9.20 / 10** |
| 2 | Gemma 4 Only | **9.00 / 10** |
| 3 | Gemma 4 + RAG | 6.75 / 10 |
| 4 | Essential AI Only | 5.80 / 10 |
| 5 | Essential AI + RAG | 5.65 / 10 |

### RAG vs Standalone

**Essential AI**

- Standalone: 5.80
- RAG: 5.65
- Delta: -0.15
- Better with RAG: 9
- Same: 4
- Worse with RAG: 7

**Gemma 4**

- Standalone: 9.00
- RAG: 6.75
- Delta: -2.25
- Better with RAG: 0
- Same: 6
- Worse with RAG: 14

---

## Track 2 Results

| Rank | System | Correct | Accuracy |
|---|---|---:|---:|
| 1 | Otel 2.0 Only | **18 / 32** | **56.25%** |
| 2 | Essential AI Only | **13 / 32** | **40.62%** |
| 3 | Essential AI + RAG | 8 / 32 | 25.00% |
| 3 | Gemma 4 + RAG | 8 / 32 | 25.00% |
| 3 | Gemma 4 Only | 8 / 32 | 25.00% |

### Essential AI RAG

- Standalone: 40.62%
- RAG: 25.00%
- Delta: -15.62 percentage points
- RAG better: 4
- Same: 19
- Worse: 9
- Generation failures: 9 / 32

### Gemma 4 RAG

- Standalone: 25.00%
- RAG: 25.00%
- Delta: 0 percentage points
- RAG better: 7
- Same: 18
- Worse: 7

---

## RAG V1 Diagnostic Finding

A targeted diagnostic was performed on 13 priority Track 1 RAG degradation cases.

- 13 / 13: `STRICT_GROUNDING_ABSTENTION`
- 11 / 13: PARTIAL retrieved evidence
- 2 / 13: SUFFICIENT retrieved evidence
- 0 / 13: retrieval primarily at fault
- 13 / 13: generation/prompting primarily at fault

These findings apply specifically to the analyzed priority degradation cases and should not be generalized to every RAG response.

---

## Primary Conclusion

The experiment showed that retrieval augmentation does not automatically improve a telecom LLM.

In RAG V1, strict document-only grounding could suppress useful engineering reasoning even when relevant evidence was available.

The future design direction is:

> **Evidence-first grounded engineering reasoning rather than strict document extraction.**

---

## RAG V1 Status

RAG V1 is now retained as the **frozen experimental baseline**.

Future work may investigate:

- graded grounding,
- evidence-sufficiency classification,
- controlled engineering reasoning,
- multi-chunk synthesis,
- task-aware routing,
- runtime stability,
- and possible architectural evolution alongside MCP.

Detailed methodology, question-level results, diagnostics, and analysis are preserved in:

`notebooks/08_rag_evaluation.ipynb`