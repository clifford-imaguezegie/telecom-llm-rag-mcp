# Module 5 Reproducibility

## Reproducibility principle

Module 5 separates expensive data generation from deterministic downstream restoration. Once a stage is frozen, later notebooks validate immutable identities rather than rebuilding prior stages unless the upstream lineage itself changes.

## M05_01 — network-truth foundation

M05_01 generated and qualified the synthetic healthy baseline, then froze:

- foundation bundle V1.2,
- canonical healthy telemetry V1.1,
- standards/topology/causal contracts,
- persistence and qualification receipts.

Root identities:

```text
M05_01 freeze     4a9f6ecec30613c160b618dfe50e11e63b8f4c8c24d06eac351d5275c744a968
Healthy telemetry c1fb3a49eacd63f45a98986322d536b74d21e585ff8bc49a4649ef11b3b34cd7
```

The older V1 telemetry is superseded and is not an authorized restore source.

## M05_02 — deterministic KPI truth

M05_02 restored M05_01 and derived formal Accessibility KPIs deterministically. It persisted NRCellCU/SubNetwork KPI products and a manifest/receipt.

```text
M05_02 manifest 3b0d6271c0aba98d3cf0ac3907ec21fea7fc113ba865ae8f6f0cdf864dd5104e
M05_02 receipt  08d12c9564b3d5dff14f4770a3bfbf0d4853df1a3dcbbfd824511102051b66ae
```

Downstream notebooks do not normally replay the full 92-partition verification and complete KPI derivation.

## M05_03 — controlled benchmark workflow

M05_03 executes the following gated workflow:

1. consolidated M05_01/M05_02 provenance restore;
2. explicit roadmap amendment and benchmark contract;
3. healthy telemetry runtime/evidence inventory;
4. topology inventory;
5. freeze the 8-family incident design;
6. create 32 deterministic non-overlapping case windows;
7. copy healthy windows into an independent working set;
8. apply numeric incident overlays only during INCIDENT periods;
9. apply controlled state/event/distractor overlays;
10. sanitize agent-visible telemetry and run leakage gates;
11. recompute formal M05_02 Accessibility KPIs from PM counters;
12. validate KPI mathematics and exact untouched-period reproduction;
13. validate causal signatures and exclusion evidence;
14. validate diagnosability;
15. separate public cases from private ground truth;
16. isolate 24 DEVELOPMENT from 8 held-out EVAL cases;
17. persist immutable outputs;
18. freeze benchmark manifest and validation receipt;
19. close out with `M05_03_CLOSEOUT_PASS=True`.

### Deterministic case contract

```text
8 families × 4 episodes = 32 cases
3 DEVELOPMENT + 1 EVAL per family
4 hours / case
16 × 15-minute intervals / case
```

Every case starts from copied M05_01 healthy telemetry. M05_01/M05_02 are read-only.

## M05_03 validation identities

```text
Roadmap amendment 49e934eee8af16281615a923248ee29768e5ca9d282cdd194712a0fcb260b057
Benchmark manifest 005232cb9326334e9a03f0a751b6eff325ffad4bc13c42caf48df8773193f7e7
Validation receipt 59a0658f880fae4f8acea6358ad74702839a46eeb46e4c17e48b6c9013f8daca
Reviewed notebook  1fce555bf96adc3a8f27b0f08da9717b6ac93345b783e4b57d44336d91e0df7e
```

## Review / cleanup rule

The final M05_03 Git notebook review made no semantic change to the benchmark. It preserved successful execution evidence, corrected no remaining experiment logic, removed transient progress-widget metadata, normalized successful execution numbering and finalized observations.

Therefore a full rerun is **not required** merely because the reviewed Git notebook has a different presentation/metadata state from the raw Colab copy.

## M05_04 restore rule

M05_04 should begin with one consolidated restore/provenance gate that validates:

- M05_03 manifest/receipt semantic identities;
- byte identities of the agent-visible telemetry/KPI/event/case artifacts;
- scenario/case counts and expected schemas;
- absence of private-truth fields;
- authorized next stage.

M05_04 should **not** rebuild incidents and must **not** read `M05_03/private/`.

## DEVELOPMENT/EVAL leakage guardrail

The 24 DEVELOPMENT labels may support later feature/model development. The 8 held-out EVAL answers remain private until formal evaluation.

`scenario_id` and absolute timestamps must not be used as predictive ML features because deterministic scheduling/IDs could become shortcut signals unrelated to telecom causality.

## Runtime

M05_03 is CPU-oriented. It uses Python, Pandas/PyArrow and DuckDB; no GPU, LLM, ML training or Sionna runtime is required.

## Data boundary

All M05_01–M05_03 telemetry is synthetic. No production network or subscriber data is required for reproduction.
