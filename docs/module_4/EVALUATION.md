# Evaluation Methodology

## 1. Frozen benchmark

Module 4 uses `module4_hybrid_eval_v1` with **16 questions**.

SHA-256:

`c6160e33d5d2bd420ddffe7f820590c5becfa9521012d5373f06451bc9b44040`

The benchmark includes continuity questions inherited from Module 3 and stress questions designed to probe:

- RAG-favoured knowledge needs;
- MCP-favoured source-specific knowledge needs;
- genuine cross-domain Hybrid needs;
- unsupported proprietary knowledge.

## 2. Controlled retrieval validation vs formal generation

Two different experimental stages must not be confused.

### Controlled retrieval validation

Cell 6 evaluates all three retrieval modes against all 16 questions:

- 16 questions × 3 modes = **48 controlled retrieval comparisons**

This stage validates the architecture and evidence behaviour before formal generation.

### Formal generation

Formal generation uses **natural route selection**, not a forced three-route matrix:

- 16 questions × 3 generator models = **48 formal answers**

For each question, the active generator chooses one route naturally.

## 3. Frozen retrieval settings

- RAG `top_k = 5`
- MCP `top_k = 5`
- maximum retrieval rounds = 3
- maximum evidence items = 5
- maximum context = 12,500 characters
- Hybrid execution = concurrent RAG + MCP
- same query sent to both Hybrid branches
- fusion = Reciprocal Rank Fusion
- `RRF k = 60`
- near-duplicate threshold = `0.88`

The frozen Module 2 and Module 3 corpora/retrievers are restored rather than rebuilt.

## 4. Generator protocol

Three formal generator models are evaluated:

| Generator | Deployment |
|---|---|
| Gemma 4 12B | QAT W4A16 / compressed tensors |
| Qwen3.8 27B | official BF16 source -> runtime BitsAndBytes INT4 |
| Qwen3.5 9B | official BF16 source -> runtime BitsAndBytes INT4 |

The formal benchmark is not used to tune generator behaviour after results are observed.

Failures, truncations and token-limit events are preserved.

## 5. Evidence-sufficiency protocol

The controller creates explicit answer requirements and checks retrieved evidence against them.

Each question can stop with:

- `SUFFICIENT_EVIDENCE`
- `MAX_RETRIEVAL_ROUNDS`

Reaching the maximum round limit is preserved as an operational signal rather than automatically converted into a failure or retried until success.

## 6. Independent semantic evaluation

The independent judge is:

- `ibm-granite/granite-4.2-8b`
- revision `7fce579a7fbbad4b1e7703b6850cefd517a4002b`
- BF16
- standard/default thinking
- temperature `1.0`
- top-p `0.95`
- formal max model length `20,480`
- formal max judge output `12,288`
- reasoning parser `nemotron_v3`

The rubric is qualified on four synthetic non-benchmark cases before formal use.

Frozen rubric SHA-256:

`45d273ca621000ea43e208b233e25b906049de2f57601b9062b130b99e4f1809`

## 7. Six evaluation dimensions

| Dimension | Weight |
|---|---:|
| Technical Correctness | 30% |
| Requirement Coverage | 25% |
| Evidence Grounding | 20% |
| Evidence–Answer Consistency | 10% |
| Technical Synthesis | 10% |
| Unsupported Claims Control | 5% |

Granite returns raw dimension scores. Python calculates the weighted composite deterministically.

## 8. Fault-tolerant evaluation

The formal judge harness:

- checkpoints successful cases;
- records failed cases;
- continues after individual failures;
- archives incompatible checkpoints when the configuration changes;
- preserves generator outputs exactly.

Formal outcome:

- planned judgments: 48
- valid judgments: 47
- failed judgments: 1
- missing: `gemma4_12b::Q16`

The missing case is not manually repaired or imputed.

## 9. Fair comparison policy

The primary cross-model semantic comparison uses the complete common set:

**Q1–Q15 × 3 generators = 45 judgments**

Q16 is analyzed separately as a negative-control case using only valid independent observations.

## 10. Post-hoc analysis

Cell 12D and Cell 13 perform CPU-only deterministic analysis using persisted artifacts.

The post-hoc phase analyzes:

- semantic quality;
- six judge dimensions;
- major errors;
- unsupported claims;
- natural route distribution;
- stress-route alignment;
- retrieval rounds;
- stop reasons;
- RAG/MCP call counts;
- generation validity;
- latency;
- negative-control behaviour;
- quality-efficiency trade-offs.

No LLM inference is required for this final analysis stage.
