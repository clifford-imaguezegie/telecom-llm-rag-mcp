# M05_03 Notebook Review

## Notebook reviewed

`M05_03_Controlled_Incidents_and_Benchmark_v1.ipynb`

## Review outcome

**PASS — M05_03 is accepted as the authoritative controlled incident benchmark.**

The reviewed notebook contains 77 cells: 19 code cells and 58 markdown cells. All stored code-cell outputs are successful, all code cells pass Python syntax compilation, and the final closeout reports every stage gate as PASS.

Reviewed notebook SHA-256:

`1fce555bf96adc3a8f27b0f08da9717b6ac93345b783e4b57d44336d91e0df7e`

## Final executed evidence

```text
M05_03_UPSTREAM_RESTORE_PASS=True
M05_03_BENCHMARK_CONTRACT_PASS=True
M05_03_TELEMETRY_RUNTIME_PASS=True
M05_03_TOPOLOGY_PASS=True
M05_03_INCIDENT_DESIGN_PASS=True
M05_03_EPISODE_SCHEDULE_PASS=True
M05_03_BASE_SLICE_PASS=True
M05_03_NUMERIC_OVERLAY_PASS=True
M05_03_CONTEXT_OVERLAY_PASS=True
M05_03_LEAKAGE_PASS=True
M05_03_SCENARIO_KPI_PASS=True
M05_03_KPI_VALIDATION_PASS=True
M05_03_CAUSAL_SIGNATURE_PASS=True
M05_03_DIAGNOSABILITY_PASS=True
M05_03_TRUTH_SEPARATION_PASS=True
M05_03_SPLIT_ISOLATION_PASS=True
M05_03_OUTPUT_PERSISTENCE_PASS=True
M05_03_PERSISTENCE_PASS=True
M05_03_CLOSEOUT_PASS=True
```

## Benchmark result space

```text
32 cases
8 case families
7 controlled fault families
1 healthy-control family
24 DEVELOPMENT
8 held-out EVAL
1,091,584 agent-visible telemetry rows
46,080 formal cell/5QI KPI records
12 controlled event rows
```

## Runtime corrections confirmed

Two implementation issues encountered during execution were corrected before final review:

1. Cell 10 no longer references a non-existent flattened `du_id` column; hierarchy is represented by the canonical entity/parent/site/CU-domain fields.
2. Cell 12 uses an explicit private-case join on `k.scenario_id = pc.scenario_id`, eliminating DuckDB's ambiguous `scenario_id` binding.

Both corrected cells executed successfully and their downstream validation gates passed.

## End-to-end integrity findings

The review confirmed:

- M05_01 and M05_02 remain unmodified;
- numeric/state incident overlays are restricted to intended INCIDENT periods;
- HEALTHY_CONTROL remains unchanged;
- formal Accessibility KPIs are recomputed rather than directly injected;
- PRE, RECOVERY and HEALTHY_CONTROL reproduce M05_02 exactly;
- every non-control case has discriminative direct evidence and unchanged exclusion evidence;
- public case definitions and agent-visible telemetry contain no hidden truth;
- 8 EVAL answers are absent from the DEVELOPMENT label artifact;
- future M05_04 access to `M05_03/private/` is explicitly forbidden.

## Cleanup applied

The Git review made non-semantic cleanup only:

- removed transient Colab/DuckDB progress-widget outputs;
- removed orphan widget metadata;
- normalized successful code execution numbering to 1–19;
- finalized concise notebook observations;
- clarified the Cell 03 runtime wording;
- added a DEVELOPMENT/EVAL shortcut guardrail against using `scenario_id` or absolute timestamps as predictive ML features.

No benchmark generation, incident injection, KPI formula, persisted artifact or validation result was changed by this cleanup. A full notebook rerun is therefore not required.

## Frozen handover

```text
Roadmap amendment semantic SHA
49e934eee8af16281615a923248ee29768e5ca9d282cdd194712a0fcb260b057

Benchmark manifest semantic SHA
005232cb9326334e9a03f0a751b6eff325ffad4bc13c42caf48df8773193f7e7

Validation receipt semantic SHA
59a0658f880fae4f8acea6358ad74702839a46eeb46e4c17e48b6c9013f8daca

Authorized next stage
M05_04_TELEMETRY_MCP_SERVICE
```

M05_03 is accepted for Git closeout and downstream M05_04 restoration.
