# Results

## Evaluation completeness

- Formal generator cases: **48 / 48**
- Planned independent judgments: **48**
- Valid independent judgments: **47**
- Completeness: **97.92%**
- Missing observation: `gemma4_12b::Q16`
- Missing-value policy: **no imputation / no manual score**

## Primary fair semantic comparison — Q1 to Q15

| Model | Mean quality | Median | Min | Max |
|---|---:|---:|---:|---:|
| **Gemma 4 12B** | **92.50%** | **100.00%** | 68.75% | 100.00% |
| **Qwen3.8 27B** | **85.08%** | 88.75% | 55.00% | 100.00% |
| **Qwen3.5 9B** | **72.92%** | 77.50% | 46.25% | 100.00% |

## Six judge dimensions — mean score out of 4

| Model | Correctness | Coverage | Grounding | Evidence consistency | Synthesis | Unsupported-claims control |
|---|---:|---:|---:|---:|---:|---:|
| **Gemma 4 12B** | **3.733** | **3.800** | **3.467** | **3.867** | **3.800** | **3.400** |
| Qwen3.8 27B | 3.600 | 3.333 | 3.133 | 3.733 | 3.467 | 2.867 |
| Qwen3.5 9B | 2.933 | 3.267 | 2.600 | 3.067 | 2.867 | 2.133 |

Gemma leads every dimension on the common set.

## Major errors and unsupported claims

| Model | Major-error rate | Unsupported-claim case rate |
|---|---:|---:|
| **Gemma 4 12B** | **0.00%** | **40.00%** |
| Qwen3.8 27B | 6.67% | 66.67% |
| Qwen3.5 9B | 20.00% | 86.67% |

Retrieval therefore improves evidence access but does not eliminate unsupported synthesis.

## Natural route distribution — all 16 questions

| Model | RAG only | MCP only | Hybrid |
|---|---:|---:|---:|
| Gemma 4 12B | 0 | 7 | 9 |
| Qwen3.8 27B | 2 | 10 | 4 |
| Qwen3.5 9B | 0 | 9 | 7 |

These distributions are descriptive. Natural route selection is question-dependent, so route-level means are not causal comparisons.

## Frozen stress-route alignment — Q9 to Q15

| Model | Alignment | Mean stress quality |
|---|---:|---:|
| Gemma 4 12B | 57.14% | **91.25%** |
| Qwen3.8 27B | **85.71%** | 85.18% |
| Qwen3.5 9B | 71.43% | 81.43% |

A key result is that the highest route-label alignment did not produce the highest stress-set quality.

## Retrieval stopping behaviour

### Gemma 4 12B

| Stop reason | n | Mean quality | Mean E2E |
|---|---:|---:|---:|
| `SUFFICIENT_EVIDENCE` | 7 | **95.89%** | 50.85 s |
| `MAX_RETRIEVAL_ROUNDS` | 8 | 89.53% | 66.14 s |

### Qwen3.8 27B

| Stop reason | n | Mean quality | Mean E2E |
|---|---:|---:|---:|
| `SUFFICIENT_EVIDENCE` | 12 | **87.92%** | 136.10 s |
| `MAX_RETRIEVAL_ROUNDS` | 3 | 73.75% | 162.04 s |

### Qwen3.5 9B

| Stop reason | n | Mean quality | Mean E2E |
|---|---:|---:|---:|
| `SUFFICIENT_EVIDENCE` | 12 | 73.02% | 45.84 s |
| `MAX_RETRIEVAL_ROUNDS` | 3 | 72.50% | 68.33 s |

The association should not be read causally: harder questions naturally require more retrieval. Operationally, however, exhausting the round limit is a useful unresolved-evidence indicator.

## Generation reliability

| Model | Formal answer-validation rate | Mean generation time | Mean E2E |
|---|---:|---:|---:|
| **Gemma 4 12B** | **100.00%** | 26.80 s | 57.11 s |
| Qwen3.8 27B | 12.50% | 82.23 s | 139.29 s |
| Qwen3.5 9B | 31.25% | 29.04 s | **49.67 s** |

Qwen truncations are preserved as formal operational failures. They are not automatically treated as semantic failures: failed Qwen3.8 outputs still averaged 84.02% independent semantic quality, and failed Qwen3.5 outputs averaged 73.18%.

This is why the experiment keeps **semantic quality** and **operational reliability** as separate axes.

## Negative control — Q16

Q16 asks for exact vendor-specific diagnosis/remediation for a fictional proprietary alarm.

| Model | Route | Judge quality | Abstention | Status |
|---|---|---:|---|---|
| Gemma 4 12B | MCP only | — | — | Not evaluated: judge schema-validation failure |
| Qwen3.8 27B | RAG only | 98.75% | True | Valid |
| Qwen3.5 9B | MCP only | 100.00% | True | Valid |

Qwen3.8 was still flagged for one unsupported claim despite correct overall abstention, which is why its score is 98.75% rather than 100%.

## Final interpretation

The experiment supports the following conclusion:

> RAG provides controlled semantic retrieval; MCP provides standardized access to a specialized knowledge service. They are complementary retrieval/access mechanisms. Their combined value is greatest when an intelligent orchestrator selects and sequences them according to the evidence needs of the problem rather than applying Hybrid retrieval universally.

## Analysis artifacts

Detailed CSV/JSON outputs and plots are available in:

- `results/module_4/final_analysis/`
- `results/module_4/formal_runs/`
