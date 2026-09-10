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
Evidence + hypotheses
          ↓
Diagnosis / decision
          ↓
Deterministic policy / safety gate
          ↓
Action MCP
          ↓
Post-action verification
          ↓
Close / retry / escalate
```

## Revised staged implementation

| Stage | Purpose | Status |
|---|---|---|
| M05_00 | architecture / implementation / causal reference | maintained reference |
| M05_01 | foundation + healthy telemetry | **complete / frozen** |
| M05_02 | formal KPI derivation + healthy validation | **complete / validated** |
| M05_03 | controlled incidents + benchmark | **complete / validated** |
| M05_04 | Telemetry MCP | **next** |
| M05_05 | specialist ML MCP | planned |
| M05_06 | LangGraph agentic investigation | planned |
| M05_07 | policy + Action MCP + verification | planned |
| M05_08 | formal evaluation / closeout | planned |

## Roadmap amendment / Sionna

M05_02 was frozen when the next planned stage was `M05_03_SIONNA_RADIO_REFERENCE_VALIDATION`. That historical receipt is not rewritten.

M05_03 records an explicit roadmap amendment:

```text
Previous planned stage : Sionna radio reference
Decision               : DEFER_SIONNA
Current stage          : M05_03_CONTROLLED_INCIDENTS_AND_BENCHMARK
M05_02 mutated         : NO
```

Sionna remains an optional later specialist reference for propagation/channel or radio-physics validation if a specific experiment needs it. M05_01/M05_02 remain the single network-truth and formal-KPI foundation.

Roadmap-amendment semantic SHA:

`49e934eee8af16281615a923248ee29768e5ca9d282cdd194712a0fcb260b057`

## M05_03 benchmark architecture

```text
Frozen healthy telemetry + M05_02 formulas
                  ↓
       Copy selected windows
                  ↓
     Controlled causal overlays
                  ↓
 PM + operational + event evidence
                  ↓
 Recompute formal Accessibility KPIs
                  ↓
       Leakage / math / causal gates
             ┌────┴────┐
             ↓         ↓
      Agent-visible   Private truth
        benchmark      benchmark
             ↓
     M05_04 Telemetry MCP
```

### Case bank

The first formal bank has 8 case families:

1. `HEALTHY_CONTROL`
2. `RADIO_INTERFERENCE`
3. `RADIO_RESOURCE_CONGESTION`
4. `N2_PACKET_LOSS_LATENCY`
5. `CU_CP_PROCESSING_PRESSURE`
6. `QOS_CONFIGURATION`
7. `RRC_CONFIGURATION`
8. `AMF_FACING_BOUNDARY`

Each family has four deterministic episodes: three DEVELOPMENT cases and one held-out EVAL case. Each episode is four hours: one hour PRE, two hours INCIDENT and one hour RECOVERY.

### Causal design

Every non-control case is validated for:

- at least two changed direct-evidence metrics,
- unchanged declared exclusion evidence,
- plausible competing hypotheses,
- target topology scope,
- controlled chronology,
- no changes outside the incident period,
- one mild non-causal operational distractor,
- measurable target-KPI degradation.

Healthy controls contain no injected changes.

### KPI integrity

M05_03 does not inject formal KPI values. It modifies copied PM/operational evidence and reruns the deterministic M05_02 Partial/Total DRB Accessibility logic.

All 46,080 expected `scenario × NRCellCU × interval × 5QI` KPI records passed range, denominator, hierarchy and aggregation validation. PRE, RECOVERY and HEALTHY_CONTROL values reproduce M05_02 exactly.

## Public/private truth boundary

The future agent may consume only:

```text
M05_03/benchmark/
```

It must not consume:

```text
M05_03/private/
```

The private layer contains root-cause family, target, severity/phase information, expected diagnosis and held-out evaluation truth. This boundary is a hard experimental control, not merely a prompt instruction.

## TM Forum-aligned closed-loop target

Module 5 uses TM Forum Autonomous Networks and Closed Loop Automation concepts as an architectural reference, without claiming that our engineering decomposition is an official TM Forum eight-step model or a formal conformance implementation.

TM Forum material uses Intent/Awareness/Analysis/Decision/Execution (I-AADE) in Autonomous Networks solution work and also documents closed-loop/self-healing patterns. Our implementation makes policy/safety and outcome verification explicit:

```text
1. Intent
2. Awareness / Observe
3. Analyse
4. Decide
5. Policy & Safety
6. Execute
7. Verify
8. Close / Escalate / Re-enter
```

Mapping to the active roadmap:

```text
M05_03  controlled conditions + hidden benchmark truth
M05_04  Awareness via Telemetry MCP
M05_05  specialist analytical / probabilistic evidence
M05_06  Awareness → Analysis → Decision via LangGraph
M05_07  Policy → Execution → Verification
M05_08  formal feedback / trajectory assessment
```

Reference context includes TM Forum IG1551 (Autonomous Operations and Closed Loops), IG1373 (Self-Healing and Closed-Loop Automation), IG1253 (Intent in Autonomous Networks), and I-AADE-based Autonomous Networks solution packages. This is **standards/reference alignment, not a conformance claim**.

## M05_04 architectural contract

M05_04 should:

- restore M05_03 through the benchmark manifest/receipt and byte identities;
- expose deterministic telemetry tools rather than handing the agent raw files;
- support cell, site, CU-domain and boundary-level queries;
- provide KPI decomposition, measurements, radio/resource/transport/processing state, events/configuration and topology;
- preserve bounded query contracts and deterministic responses;
- never load or expose the private truth directory.

The intent is to create the agent's **eyes and ears** before adding specialist ML or LLM orchestration.
