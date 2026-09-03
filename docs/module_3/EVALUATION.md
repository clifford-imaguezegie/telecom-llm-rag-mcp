# Module 3 Evaluation Methodology

## Frozen controls

- Benchmark: `module3_eval_v2`
- Benchmark SHA256: `d40c0090c371f0a99ea6057bbb3fa8024e6b7d4174e037e7a6cf9fef9b9667f5`
- Frozen prompt SHA256: `854374b0ea09e63dc8ddde34d722788231c2be860f4b8ac1a709e907966baf09`
- 8 questions per scored experiment
- Same deterministic 3GPP/TCC/Hybrid routing semantics
- Same public MCP tool interface and bounded orchestration limits

## Evaluation layers

1. Execution reliability: COMPLETED / CHECK / ERROR
2. MCP search discipline and latency
3. Route accuracy and strict route adherence
4. Source-family, collection and 3GPP-spec diagnostics
5. Expected-element coverage
6. Evidence coverage and authority alignment
7. Blind technical-quality LLM judge
8. Evidence-only claim-grounding LLM judge
9. Paired architecture and cross-model comparisons

## Judge separation

Technical-quality judging asks whether the answer is technically correct, complete, relevant and useful to an engineer; the blind judge may use its technical knowledge.

Grounding judging separately asks whether each material claim is supported by the evidence actually retrieved through MCP. Outside knowledge is not allowed to rescue unsupported claims.

This separation prevents execution success, technical plausibility and evidence support from being conflated.

## Interpretation limits

The judge is a consistent automated evaluator, not human ground truth. Results are triangulated with deterministic diagnostics. No statistical-significance claim is made from the eight-question benchmark.
