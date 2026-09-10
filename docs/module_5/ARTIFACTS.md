# Module 5 Artifact Policy

## GitHub artifacts

The Git repository contains the curated artifacts needed to understand, validate and continue Module 5:

- M05_00 historical and current reference notebooks
- reviewed M05_01 and M05_02 implementation notebooks
- architecture, status, artifact and reproducibility documentation
- M05_01 and M05_02 notebook review records
- foundation requirements
- static Module 5 validation script

Large runtime-generated telemetry remains outside Git.

## Authoritative durable working artifacts

### Canonical healthy telemetry V1.1

```text
/content/drive/MyDrive/Telecom_AI_Engineering_Platform/Module_5/M05_01/telemetry/healthy_baseline_v1_1
```

- 92-day healthy baseline
- 92 daily Parquet partitions
- 18,829,824 observations
- 8,832 15-minute intervals
- canonical dataset semantic SHA: `c1fb3a49eacd63f45a98986322d536b74d21e585ff8bc49a4649ef11b3b34cd7`
- canonical manifest artifact SHA: `e856ffe3f7ed97e6ad4592e999e5fd3adf5993f80ac72cdada1f374ab6543411`
- telemetry qualification semantic SHA: `fc3c38f980209b1d5a9504b30f98efa6636ba7eedc153ef4f4d1e7bb49be156a`
- partition, manifest, event-channel and qualification identities verified on Google Drive

### Frozen foundation bundle V1.2

```text
/content/drive/MyDrive/Telecom_AI_Engineering_Platform/Module_5/M05_01/foundation/foundation_bundle_v1_2
```

- 11 authoritative Cells 03–12 foundation artifacts
- 4 authoritative control artifacts
- 1 deterministic bundle index
- 1 foundation persistence receipt
- 17 verified files in total
- no Parquet telemetry duplicated
- no superseded V1 artifacts included
- freeze semantic SHA: `4a9f6ecec30613c160b618dfe50e11e63b8f4c8c24d06eac351d5275c744a968`
- bundle index semantic SHA: `55c8ef51f905945fb825fad3bb35b932ccf7e140f5ffe9d85d3430071ff7143b`
- bundle index artifact SHA: `bdeee58930d9a13334640132e7a12fa9ace6222a19cfc2c8626e1fd430fd9b8f`
- foundation persistence semantic SHA: `936b605cb1ce3c2d2b2977fed537df65c5e61e19e26ff655f89b27b919d62879`


### M05_02 derived Accessibility KPI products

```text
/content/drive/MyDrive/Telecom_AI_Engineering_Platform/Module_5/M05_02/kpi/
```

- `module5_m05_02_nr_cell_cu_accessibility_kpis_v1.parquet`
  - 794,880 NRCellCU × interval × 5QI records
  - SHA-256: `709c9883bad799dec3907624a7590f5e44356d9fef7c00f4446d165fd1b2223f`
- `module5_m05_02_subnetwork_accessibility_kpis_v1.parquet`
  - 26,496 SubNetwork × interval × 5QI records
  - SHA-256: `18d5a60ca91139242e85e9f5468346a66bedf70f8736e01507568f2afb9c42ba`

### M05_02 provenance controls

```text
/content/drive/MyDrive/Telecom_AI_Engineering_Platform/Module_5/M05_02/manifests/
```

- KPI derivation manifest semantic SHA: `3b0d6271c0aba98d3cf0ac3907ec21fea7fc113ba865ae8f6f0cdf864dd5104e`
- validation receipt semantic SHA: `08d12c9564b3d5dff14f4770a3bfbf0d4853df1a3dcbbfd824511102051b66ae`
- all M05_02 validation gates passed
- no fault injection, ML inference or LLM inference introduced

## Superseded historical lineage

The earlier `MODULE5_HEALTHY_TELEMETRY_V1` dataset was invalidated for formal KPI-readiness reasons and must not be restored by M05_02 or any downstream Module 5 stage.

The historical private Kaggle V1 dataset and its dependent freeze/bundle lineage are retained only as superseded provenance. Final Kaggle publication of the corrected Module 5 artifacts is deferred until platform clean-up.

## Provenance rule

`M05_00_Implementation_and_Causal_Observability_Reference_v1.ipynb` is preserved because its exact byte SHA `9c4db1552791510d3237fd8c7ff93cd7ae66d614d42fed0da7a268bf77fa910e` is referenced by M05_01 provenance. The V1.1 M05_00 notebook is a documentation refresh and does not rewrite that historical identity.

All M05_01 telemetry and M05_02 derived KPI products are synthetic and must not be represented as production operator telemetry.
