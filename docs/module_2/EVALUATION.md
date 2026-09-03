# Module 2 Evaluation

Module 2 reuses the frozen Module 1 question suites and expands the comparison to five systems.

## Track 1 — Engineering Quality

| Rank | System | Mean Score |
|---|---|---:|
| 1 | **OTel 2.0 Only** | **9.20 / 10** |
| 2 | **Gemma 4 Only** | **9.00 / 10** |
| 3 | Gemma 4 + RAG | 6.75 / 10 |
| 4 | Essential AI Only | 5.80 / 10 |
| 5 | Essential AI + RAG | 5.65 / 10 |

Track 1 priority degradation diagnosis examined 13 RAG cases:
- 13/13 primarily `STRICT_GROUNDING_ABSTENTION`;
- 11/13 had PARTIAL evidence;
- 2/13 had SUFFICIENT evidence;
- 0/13 were classified primarily as retrieval failures;
- 13/13 were classified as generation/prompting failures.

These findings apply to the investigated priority cases rather than every RAG response.

## Track 2 — Objective Correctness

| Rank | System | Correct | Accuracy |
|---|---|---:|---:|
| 1 | **OTel 2.0 Only** | **18 / 32** | **56.25%** |
| 2 | **Essential AI Only** | **13 / 32** | **40.62%** |
| 3 | Essential AI + RAG | 8 / 32 | 25.00% |
| 3 | Gemma 4 Only | 8 / 32 | 25.00% |
| 3 | Gemma 4 + RAG | 8 / 32 | 25.00% |

Essential AI + RAG had 9 CUDA OOM generation failures, giving 71.88% response success. Conditional accuracy on the 23 successful responses was 34.78%.

## RAG impact

Gemma Track 1:
- standalone 9.00;
- RAG 6.75;
- RAG better 0/20;
- same 6/20;
- worse 14/20.

EssentialAI Track 1:
- standalone 5.80;
- RAG 5.65;
- better 9/20;
- same 4/20;
- worse 7/20.

Gemma Track 2:
- standalone 25.00%;
- RAG 25.00%;
- better 7/32;
- same 18/32;
- worse 7/32.

## Main conclusion

RAG V1 demonstrated that retrieval augmentation is not automatically beneficial. Retrieval success, evidence sufficiency, generation policy, task type and runtime reliability must be measured separately.
