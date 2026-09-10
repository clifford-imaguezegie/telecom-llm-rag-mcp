# Module 5 Artifact Policy

## GitHub artifacts

The Git repository contains curated artifacts required to understand, validate and continue Module 5:

- M05_00 historical/current architecture references
- reviewed M05_01 foundation + healthy telemetry notebook
- reviewed M05_02 formal KPI notebook
- reviewed M05_03 controlled incident benchmark notebook
- architecture, status, artifact and reproducibility documentation
- per-notebook review records
- Module 5 requirements files
- static validators

Large telemetry, KPI Parquets and benchmark datasets remain outside Git.

**Private M05_03 ground truth must not be committed to Git or exposed to M05_04.**

## M05_01 authoritative durable artifacts

```text
Foundation:
/content/drive/MyDrive/Telecom_AI_Engineering_Platform/Module_5/M05_01/foundation/foundation_bundle_v1_2

Healthy telemetry:
/content/drive/MyDrive/Telecom_AI_Engineering_Platform/Module_5/M05_01/telemetry/healthy_baseline_v1_1
```

Key identities:

- M05_01 freeze V1.2 semantic SHA: `4a9f6ecec30613c160b618dfe50e11e63b8f4c8c24d06eac351d5275c744a968`
- canonical telemetry semantic SHA: `c1fb3a49eacd63f45a98986322d536b74d21e585ff8bc49a4649ef11b3b34cd7`
- canonical telemetry manifest artifact SHA: `e856ffe3f7ed97e6ad4592e999e5fd3adf5993f80ac72cdada1f374ab6543411`
- telemetry qualification semantic SHA: `fc3c38f980209b1d5a9504b30f98efa6636ba7eedc153ef4f4d1e7bb49be156a`

## M05_02 formal KPI artifacts

```text
/content/drive/MyDrive/Telecom_AI_Engineering_Platform/Module_5/M05_02/
```

- NRCellCU KPI SHA-256: `709c9883bad799dec3907624a7590f5e44356d9fef7c00f4446d165fd1b2223f`
- SubNetwork KPI SHA-256: `18d5a60ca91139242e85e9f5468346a66bedf70f8736e01507568f2afb9c42ba`
- KPI manifest semantic SHA: `3b0d6271c0aba98d3cf0ac3907ec21fea7fc113ba865ae8f6f0cdf864dd5104e`
- validation receipt semantic SHA: `08d12c9564b3d5dff14f4770a3bfbf0d4853df1a3dcbbfd824511102051b66ae`

## M05_03 agent-visible benchmark artifacts

```text
/content/drive/MyDrive/Telecom_AI_Engineering_Platform/Module_5/M05_03/benchmark/
```

| Artifact | SHA-256 |
|---|---|
| `module5_m05_03_agent_visible_telemetry_v1.parquet` | `e7ecf55940a32dacabe8df9ccc4f133351b5288bf17e352237906155f9231ff4` |
| `module5_m05_03_agent_visible_cell_kpis_v1.parquet` | `9b54d281938bcfdec1d3bea76821d7ca0b160ab80036f3ca2f5e49977a2e85c5` |
| `module5_m05_03_agent_visible_subnetwork_kpis_v1.parquet` | `24d44ce8e8624f96924a4c46773f500bdfbb27a4668456febc9daf76f7eb5e49` |
| `module5_m05_03_agent_visible_events_v1.parquet` | `bb6fbfd244ca4907efea584a76e3d36507a9e7bcf99a694a56634f348d7c8117` |
| `module5_m05_03_benchmark_cases_v1.json` | `419362e1cab7a5f6ec311f8652fc84e8b4307bdb7aacbf346013feaebc77e8b7` |

Public-case semantic SHA: `fde8cfaca098da32a16e01cf277487f331d956a715adcee609433de1e31555fd`

These artifacts are the only M05_03 data layer authorized for future Telemetry MCP exposure.

## M05_03 private evaluation artifacts

```text
/content/drive/MyDrive/Telecom_AI_Engineering_Platform/Module_5/M05_03/private/
```

| Artifact | SHA-256 |
|---|---|
| `module5_m05_03_ground_truth_v1.json` | `9b191551fcdd711f078ea230b308af9c0e5c12a9cf41a14f9406d80e17fa4241` |
| `module5_m05_03_development_labels_v1.parquet` | `99af89d318cac8db46afd1e8a8e3a95650101ce9a28ac56c971892157e696eb1` |
| `module5_m05_03_injection_audit_summary_v1.parquet` | `9ec6a0b5b39fafda79a87b831e7d9fce3a39674c72a052d69b2b892755012b13` |

Private-truth semantic SHA: `2567c2da9c652f61632be0663752ab2d269a656e1d97c70a64b2553be4741482`

These files are retained for controlled development/evaluation only. They are **not agent-visible artifacts** and are deliberately excluded from this Git package.

## M05_03 provenance controls

```text
/content/drive/MyDrive/Telecom_AI_Engineering_Platform/Module_5/M05_03/manifests/
```

- roadmap amendment semantic SHA: `49e934eee8af16281615a923248ee29768e5ca9d282cdd194712a0fcb260b057`
- roadmap amendment persisted file SHA-256: `2ddb590d4129657f46e8a0eec866f6824fb54cd66087ace73f490896e6b5dcd8`
- incident benchmark manifest semantic SHA: `005232cb9326334e9a03f0a751b6eff325ffad4bc13c42caf48df8773193f7e7`
- validation receipt semantic SHA: `59a0658f880fae4f8acea6358ad74702839a46eeb46e4c17e48b6c9013f8daca`
- all M05_03 validation gates passed
- authorized next stage: `M05_04_TELEMETRY_MCP_SERVICE`

## Superseded / deferred lineage

The earlier invalid M05_01 V1 telemetry remains superseded provenance and must not be restored downstream.

The Sionna notebook/plan is **deferred**, not part of the active M05_03 benchmark lineage, and must not be treated as network truth.

Kaggle archival remains deferred; Google Drive is the active durable runtime store.

## Data boundary

All Module 5 telemetry and incident data in M05_01–M05_03 are synthetic. No production operator telemetry, subscriber information or customer network data is included.
