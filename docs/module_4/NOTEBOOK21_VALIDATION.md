# Notebook 21 Validation

## Fresh Sequential Canonical Run

Question:

```text
What is 5G?
```

### Routing and Retrieval

| Item | Result |
|---|---|
| Granite route | `TELECOM_GROUNDED` |
| Planner mode | `RAG_ONLY` |
| Retrieval rounds | 1 / 3 |
| RAG candidates | 5 |
| MCP candidates | 0 |
| Final evidence | 5 |
| Context | 12,500 chars |
| Requirement-bounded sufficiency | `True` |

### Comparative Evaluation

| Item | Result |
|---|---:|
| Baseline claims | 21 |
| Baseline supported | 13 |
| Baseline partially supported | 1 |
| Baseline unsupported | 7 |
| Baseline risk | 26.7% — MODERATE |
| Grounded claims | 15 |
| Grounded supported | 15 |
| Grounded unsupported | 0 |
| Grounded risk | 0.0% — LOW |
| Invalid evidence references | 0 |
| Empty judge reasons | 0 |

### Final Validation

All final checks passed:

- pre-LLM security,
- router output,
- baseline answer,
- flexible answer,
- baseline isolation,
- route execution,
- adaptive retrieval,
- judge-input contract,
- judge execution,
- complete `4C.6Y` validation.

## Hosted Judge Resilience

The deployment runtime preserves the frozen judge prompt and evaluation method.

Operational resilience was added for hosted-model formatting failures:

1. one controlled retry if Granite returns a structurally invalid result such as `{}`;
2. unexpected extra claim IDs are discarded only when all required fixed claim IDs remain present exactly once;
3. missing or duplicate required claim IDs still fail validation.

This hardening changes runtime robustness, not the evaluation rubric.
