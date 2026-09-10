# Module 5 — Agentic Telecom AI

Module 5 extends the Telecom AI Engineering Platform from adaptive knowledge access into controlled, tool-driven network investigation.

## Current milestone

**M05_02 — Runtime Restore + Formal KPI Derivation + Healthy Validation: complete.**

M05_01 established deterministic network truth. M05_02 independently restored that frozen lineage, derived formal TS 28.554 Partial and Total DRB Accessibility from standardized PM observations, validated the complete 92-day healthy baseline, and persisted reusable KPI products for downstream stages.

## Core principle

> **The LLM orchestrates. Deterministic telemetry supplies network truth. Standards knowledge provides grounding. ML supplies probabilistic evidence. Policy controls actions. Verification closes the loop.**

## Current durable working state

Authoritative upstream M05_01 sources:

```text
Foundation
/content/drive/MyDrive/Telecom_AI_Engineering_Platform/Module_5/M05_01/foundation/foundation_bundle_v1_2

Telemetry
/content/drive/MyDrive/Telecom_AI_Engineering_Platform/Module_5/M05_01/telemetry/healthy_baseline_v1_1
```

Validated M05_02 outputs:

```text
NRCellCU KPI
/content/drive/MyDrive/Telecom_AI_Engineering_Platform/Module_5/M05_02/kpi/module5_m05_02_nr_cell_cu_accessibility_kpis_v1.parquet

SubNetwork KPI
/content/drive/MyDrive/Telecom_AI_Engineering_Platform/Module_5/M05_02/kpi/module5_m05_02_subnetwork_accessibility_kpis_v1.parquet

KPI derivation manifest
/content/drive/MyDrive/Telecom_AI_Engineering_Platform/Module_5/M05_02/manifests/module5_m05_02_kpi_derivation_manifest_v1.json

Validation receipt
/content/drive/MyDrive/Telecom_AI_Engineering_Platform/Module_5/M05_02/manifests/module5_m05_02_validation_receipt_v1.json
```

Key M05_02 identities:

```text
NRCellCU KPI SHA-256
709c9883bad799dec3907624a7590f5e44356d9fef7c00f4446d165fd1b2223f

SubNetwork KPI SHA-256
18d5a60ca91139242e85e9f5468346a66bedf70f8736e01507568f2afb9c42ba

KPI manifest semantic SHA
3b0d6271c0aba98d3cf0ac3907ec21fea7fc113ba865ae8f6f0cdf864dd5104e

Validation receipt semantic SHA
08d12c9564b3d5dff14f4770a3bfbf0d4853df1a3dcbbfd824511102051b66ae
```

Kaggle publication remains deferred until final Module 5 clean-up.

## Documents

- `ARCHITECTURE.md` — Module 5 architecture and staged implementation.
- `STATUS.md` — current closeout state and next stage.
- `ARTIFACTS.md` — GitHub vs durable runtime artifact boundary and frozen identities.
- `REPRODUCIBILITY.md` — rebuild, restore and provenance policy.
- `M05_01_NOTEBOOK_REVIEW.md` — M05_01 end-to-end review and clean-up record.
- `M05_02_NOTEBOOK_REVIEW.md` — M05_02 end-to-end review and standards-alignment record.
- `MODULE5_CHANGELOG.md` — Git-visible milestone history.

## Notebooks

- `M05_00_Implementation_and_Causal_Observability_Reference_v1.ipynb` — historical architectural parent preserved because its SHA remains referenced by M05_01 provenance.
- `M05_00_Implementation_and_Causal_Observability_Reference_v1_1.ipynb` — post-M05_01 documentation refresh.
- `M05_01_Foundation_and_Healthy_Telemetry_v1.ipynb` — reviewed Git copy of the completed M05_01 implementation.
- `M05_02_Runtime_Restore_KPI_Derivation_and_Healthy_Validation_v1.ipynb` — reviewed executed notebook establishing the formal healthy Accessibility KPI baseline.

## Next

**M05_03 — Sionna Radio Reference Validation.**

M05_03 should use a lean upstream restore/provenance gate and consume the frozen M05_01/M05_02 identities rather than replaying the full M05_02 derivation workflow.
