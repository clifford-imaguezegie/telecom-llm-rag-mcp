# Module 5 Architecture

## Research question

> **Can an LLM-driven telecom agent autonomously select and sequence standards-grounded knowledge, hierarchical RAN telemetry and specialist ML tools to diagnose realistic 5G RAN incidents accurately, efficiently and safely?**

## North Star

> **The LLM orchestrates. Deterministic telemetry supplies network truth. Standards knowledge provides grounding. ML supplies probabilistic evidence. Policy controls actions. Verification closes the loop.**

## Target architecture

```text
Incident / engineering task
          ↓
LangGraph orchestration + state
          ↓
 ┌────────┼─────────┬──────────┐
 │        │         │          │
RAG   Knowledge  Telemetry   ML MCP
       MCP         MCP
 └────────┴─────────┴──────────┘
          ↓
Evidence + agent state
          ↓
Diagnosis / next investigation step
          ↓
Deterministic policy / approval gate
          ↓
Action MCP
          ↓
Post-action verification
```

## Staged implementation

| Stage | Purpose | Status |
|---|---|---|
| M05_00 | architecture / implementation / causal reference | maintained reference |
| M05_01 | foundation + healthy telemetry | **complete / frozen** |
| M05_02 | runtime restore + formal KPI derivation + healthy validation | **complete / validated** |
| M05_03 | Sionna independent radio reference validation | **next** |
| M05_04 | controlled incidents + benchmark | planned |
| M05_05 | Telemetry MCP | planned |
| M05_06 | specialist ML MCP | planned |
| M05_07 | LangGraph agentic investigation | planned |
| M05_08 | policy + Action MCP + verification | planned |
| M05_09 | formal evaluation / closeout | planned |

## M05_01 bounded domain

The first bounded operational domain is **5G RAN Accessibility**. The foundation distinguishes formal standardized KPIs/PM dependencies from synthetic operational diagnostics. RACH is treated as supporting pre-RRC diagnostic evidence rather than being mislabeled as a TS 28.554 Accessibility KPI.

## M05_01 environment

- 10 synthetic sites / DUs
- 3 sectors per site
- 30 logical cells
- 30 `NRCellCU` objects
- 30 `NRCellDU` objects
- two CU domains plus shared CU-CP/CU-UP/N2/E1 and local F1 observation scopes
- 15-minute PM observation interval
- healthy-only canonical baseline

M05_01 contains no injected incidents, hidden fault labels, specialist ML inference or autonomous action.

## M05_01 frozen handover state

M05_01 closes with two independently verified Google Drive restore sources:

```text
Foundation bundle V1.2
/content/drive/MyDrive/Telecom_AI_Engineering_Platform/Module_5/M05_01/foundation/foundation_bundle_v1_2

Canonical telemetry V1.1
/content/drive/MyDrive/Telecom_AI_Engineering_Platform/Module_5/M05_01/telemetry/healthy_baseline_v1_1
```

The authoritative freeze semantic SHA is `4a9f6ecec30613c160b618dfe50e11e63b8f4c8c24d06eac351d5275c744a968` and the canonical telemetry semantic SHA is `c1fb3a49eacd63f45a98986322d536b74d21e585ff8bc49a4649ef11b3b34cd7`.

The earlier V1 telemetry lineage is invalidated for downstream use. Kaggle publication of the corrected artifacts is deferred until final Module 5 clean-up.


## M05_02 validated handover state

M05_02 independently restored the frozen M05_01 lineage and established reusable deterministic KPI truth without introducing fault injection, ML inference or LLM inference.

```text
M05_01 frozen foundation + canonical telemetry
        ↓
M05_02 deterministic PM binding and KPI derivation
        ↓
Validated NRCellCU and SubNetwork Accessibility KPI products
        ↓
M05_03 independent Sionna radio reference validation
```

The validated M05_02 result space contains 794,880 `NRCellCU × 15-minute interval × 5QI` KPI records and 26,496 `SubNetwork × 15-minute interval × 5QI` KPI records.

Downstream stages restore and verify the M05_02 manifest/receipt identities rather than repeating the 92-partition physical verification and full KPI derivation workflow.
