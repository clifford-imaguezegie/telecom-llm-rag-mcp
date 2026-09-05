# Limitations

## 1. Small formal benchmark

The formal benchmark contains 16 questions. It is deliberately broad across telecom standards, cloud-native systems, internet protocols, O-RAN, AI/ML and fault isolation, but it is not large enough to support broad statistical generalization to all telecom knowledge tasks.

## 2. Natural-route means are confounded

Formal generation uses natural route selection.

Therefore, mean quality for `RAG_ONLY`, `MCP_ONLY` and `HYBRID` is **descriptive**, not causal. Different routes receive different questions and different models make different routing decisions.

A controlled forced-route experiment would be required to estimate causal Hybrid gain on the exact same questions.

## 3. One missing independent judgment

The Granite judge produced 47 valid judgments out of 48 planned.

Missing case:

`gemma4_12b::Q16`

The judge inference completed normally, but `negative_control_abstention` failed Boolean schema validation. The observation is intentionally left missing and is not imputed.

## 4. Generator token-limit failures

Qwen3.8 and Qwen3.5 frequently reached the 1,024-token answer limit.

This means their low formal generation-validation rates reflect operational completion problems as well as answer quality.

The experiment keeps semantic quality and generation reliability separate, but the configured token ceiling still affects comparability.

## 5. LLM judge is not human ground truth

Granite is independent from the Gemma/Qwen generator families used here, but LLM-as-a-judge remains an automated evaluator.

The qualification pilot reduces obvious rubric failure risk but does not replace expert human validation.

## 6. Retrieval corpus coverage affects routing outcomes

RAG and MCP are evaluated using the frozen corpora available to the project.

A route may underperform because the relevant information is absent or weakly represented in that corpus rather than because the retrieval mechanism itself is intrinsically inferior.

## 7. Evidence-sufficiency association is not causal

Cases that require more retrieval rounds tend to be harder.

The observed relationship between more rounds and lower quality should therefore be interpreted as a **difficulty / unresolved-evidence signal**, not proof that extra retrieval causes lower quality.

## 8. Quantization and runtime differences

The three generators were not served with identical numerical precision:

- Gemma used its QAT W4A16 checkpoint;
- Qwen3.8 and Qwen3.5 used runtime BitsAndBytes INT4.

The experiment compares practical deployable model/runtime configurations, not a pure architecture-only comparison at identical precision.

## 9. Local runtime results are hardware/context dependent

Latency results are specific to the executed Google Colab NVIDIA L4 environment and the serving configurations captured in the manifests.

They should not be generalized directly to production infrastructure.

## 10. No action-taking autonomy is evaluated

Module 4 is a knowledge-access and evidence-grounding experiment.

It does not evaluate network telemetry tools, action tools, policy gates or production autonomy. Those are explicitly deferred to Module 5 and later modules.
