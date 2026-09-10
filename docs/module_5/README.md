# Module 5 — Agentic Telecom AI

Module 5 extends the Telecom AI Engineering Platform from adaptive knowledge access into controlled, tool-driven network investigation and progressively safer closed-loop operation.

## Current milestone

**M05_03 — Controlled Incidents + Benchmark: complete and validated.**

M05_01 established deterministic healthy network truth. M05_02 established deterministic formal Accessibility KPI truth. M05_03 now provides the controlled incident benchmark against which Telemetry MCP, specialist ML and the future LangGraph agent can be developed and independently evaluated.

## Core principle

> **The LLM orchestrates. Deterministic telemetry supplies network truth. Standards knowledge provides grounding. ML supplies probabilistic evidence. Policy controls actions. Verification closes the loop.**

## M05_03 benchmark

```text
8 case families
7 fault families + 1 HEALTHY_CONTROL
4 episodes per family
32 cases total
24 DEVELOPMENT
8 held-out EVAL
4 hours per case: 1h PRE + 2h INCIDENT + 1h RECOVERY
```

The fault bank covers radio interference, radio-resource congestion, N2 loss/latency, CU-CP processing pressure, QoS configuration, RRC configuration and an AMF-facing boundary condition.

The benchmark is deliberately causal rather than randomly corrupted: fault cases contain supporting evidence, exclusion evidence, plausible competing hypotheses and mild non-causal distractors.

## Truth boundary

M05_03 creates two physically and logically separate layers:

```text
benchmark/  -> agent-visible telemetry, KPIs, events and public cases
private/    -> hidden ground truth, DEVELOPMENT labels and injection audit
```

`M05_04` and the future agent **must not load `M05_03/private/`**.

Formal Accessibility KPIs are recomputed from PM-counter changes using the M05_02 deterministic logic. No formal KPI value is directly injected.

## Durable working state

```text
M05_01 foundation
/content/drive/MyDrive/Telecom_AI_Engineering_Platform/Module_5/M05_01/foundation/foundation_bundle_v1_2

M05_01 healthy telemetry
/content/drive/MyDrive/Telecom_AI_Engineering_Platform/Module_5/M05_01/telemetry/healthy_baseline_v1_1

M05_02 formal KPIs
/content/drive/MyDrive/Telecom_AI_Engineering_Platform/Module_5/M05_02/

M05_03 controlled benchmark
/content/drive/MyDrive/Telecom_AI_Engineering_Platform/Module_5/M05_03/
```

Key semantic identities:

```text
M05_01 freeze        4a9f6ecec30613c160b618dfe50e11e63b8f4c8c24d06eac351d5275c744a968
M05_01 telemetry     c1fb3a49eacd63f45a98986322d536b74d21e585ff8bc49a4649ef11b3b34cd7
M05_02 KPI manifest  3b0d6271c0aba98d3cf0ac3907ec21fea7fc113ba865ae8f6f0cdf864dd5104e
M05_02 receipt       08d12c9564b3d5dff14f4770a3bfbf0d4853df1a3dcbbfd824511102051b66ae
M05_03 roadmap       49e934eee8af16281615a923248ee29768e5ca9d282cdd194712a0fcb260b057
M05_03 manifest      005232cb9326334e9a03f0a751b6eff325ffad4bc13c42caf48df8773193f7e7
M05_03 receipt       59a0658f880fae4f8acea6358ad74702839a46eeb46e4c17e48b6c9013f8daca
```

## Sionna roadmap decision

The M05_02 validation receipt is preserved exactly, including its historical Sionna next-stage authorization. M05_03 adds a separate immutable roadmap amendment that defers Sionna and establishes Controlled Incidents + Benchmark as the active stage. Sionna may be revisited later as an optional radio-physics reference; it is not an alternative PM/KPI truth source.

## Documents

- `ARCHITECTURE.md` — Module 5 architecture, revised roadmap, benchmark boundaries and closed-loop alignment.
- `STATUS.md` — M05_03 closeout state and M05_04 handover.
- `ARTIFACTS.md` — Git vs Google Drive artifact boundary and identities.
- `REPRODUCIBILITY.md` — restore, replay and provenance rules.
- `M05_01_NOTEBOOK_REVIEW.md` — M05_01 review record.
- `M05_02_NOTEBOOK_REVIEW.md` — M05_02 review record.
- `M05_03_NOTEBOOK_REVIEW.md` — M05_03 review/cleanup record.
- `MODULE5_CHANGELOG.md` — Git-visible milestone history.

## Next

**M05_04 — Telemetry MCP Service**

M05_04 will turn the static agent-visible benchmark into a deterministic investigation interface for hierarchical KPI, PM, radio, resource, transport, processing, event, configuration and topology queries.
