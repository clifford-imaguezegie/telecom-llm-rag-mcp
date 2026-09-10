# Module 5 Status

## Current state

**Module 5 is in progress. M05_03 — Controlled Incidents + Benchmark is complete and validated.**

### Completed M05_03 outcomes

- restored and verified the frozen M05_01/M05_02 upstream identities in one consolidated provenance gate
- formally recorded the roadmap amendment that defers Sionna without mutating M05_02 history
- defined 8 case families: 7 controlled faults + 1 healthy control
- generated 32 non-overlapping four-hour cases across the healthy baseline
- fixed the split at 24 DEVELOPMENT and 8 held-out EVAL cases
- copied 1,091,584 observations from healthy baseline windows before injection
- injected numeric symptoms only during INCIDENT periods
- added required configuration/boundary state changes, 12 controlled events and mild non-causal distractors
- created an agent-visible layer with zero hidden-truth schema/text hits
- recomputed 46,080 cell/5QI formal Accessibility KPI records from PM counters
- reproduced M05_02 exactly in PRE, RECOVERY and HEALTHY_CONTROL periods
- validated direct evidence, exclusion evidence and target-KPI diagnosability across all fault cases
- separated public case definitions from private ground truth
- isolated all 8 EVAL answers from the DEVELOPMENT label artifact
- persisted immutable benchmark/private/manifests on Google Drive
- completed all 18 stage validation gates
- `M05_03_CLOSEOUT_PASS=True`

### Benchmark summary

```text
Case families                 8
Fault families                7
Healthy-control family        1
Cases                         32
DEVELOPMENT                   24
Held-out EVAL                 8
Intervals per case            16
Case duration                 4 hours
Agent-visible telemetry rows  1,091,584
Formal cell KPI rows          46,080
Controlled event rows         12
```

Observed formal KPI range after controlled incidents:

```text
Partial DRB Accessibility minimum : 65.315388%
Total DRB Accessibility minimum   : 70.663885%
```

These are synthetic benchmark outcomes, not universal operational thresholds.

## Authoritative identities

```text
M05_01 freeze semantic SHA
4a9f6ecec30613c160b618dfe50e11e63b8f4c8c24d06eac351d5275c744a968

Canonical healthy telemetry semantic SHA
c1fb3a49eacd63f45a98986322d536b74d21e585ff8bc49a4649ef11b3b34cd7

M05_02 KPI manifest semantic SHA
3b0d6271c0aba98d3cf0ac3907ec21fea7fc113ba865ae8f6f0cdf864dd5104e

M05_02 validation receipt semantic SHA
08d12c9564b3d5dff14f4770a3bfbf0d4853df1a3dcbbfd824511102051b66ae

M05_03 roadmap amendment semantic SHA
49e934eee8af16281615a923248ee29768e5ca9d282cdd194712a0fcb260b057

M05_03 benchmark manifest semantic SHA
005232cb9326334e9a03f0a751b6eff325ffad4bc13c42caf48df8773193f7e7

M05_03 validation receipt semantic SHA
59a0658f880fae4f8acea6358ad74702839a46eeb46e4c17e48b6c9013f8daca

Reviewed M05_03 notebook SHA-256
1fce555bf96adc3a8f27b0f08da9717b6ac93345b783e4b57d44336d91e0df7e
```

## Integrity boundaries

- M05_01 artifacts modified: **NO**
- M05_02 artifacts modified: **NO**
- Sionna introduced: **NO — DEFERRED**
- ML/LLM inference introduced: **NO**
- formal KPI values directly injected: **NO**
- private truth exposed to agent-visible data: **NO**
- `M05_04` access to `M05_03/private/`: **FORBIDDEN**

## Next stage

**M05_04 — Telemetry MCP Service**

The next stage will turn the frozen agent-visible benchmark into a deterministic hierarchical investigation interface. The agent will later retrieve evidence through bounded tools rather than reading the full Parquet dataset directly.
