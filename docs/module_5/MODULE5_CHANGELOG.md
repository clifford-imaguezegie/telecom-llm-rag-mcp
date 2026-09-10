# Module 5 Changelog

## 2026-09-10 — M05_02 Formal Accessibility KPI Validation Closeout

### Completed

- independently restored the authoritative M05_01 V1.2/V1.1 lineage
- verified all 92 Parquet partitions and 18,829,824 canonical telemetry observations
- restored the TS 28.554 Partial and Total DRB Accessibility knowledge contract
- bound all 16 formal PM dependencies to canonical telemetry
- derived and validated 794,880 cell-level Accessibility KPI records
- established a 26,496-row SubNetwork healthy KPI baseline
- confirmed zero Added-DRB and Resume/fallback/re-establishment hierarchy violations
- persisted immutable NRCellCU and SubNetwork KPI Parquets to Google Drive
- persisted the M05_02 KPI derivation manifest and validation receipt
- completed `M05_02_CLOSEOUT_PASS=True`

### M05_02 identities

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

### Review correction

The final Git notebook review made documentation-only corrections: normalized notebook heading hierarchy, corrected the completion-gate name, added the missing Cell 10 anchor, clarified standard-vs-internal Resume PM naming, and strengthened the downstream no-replay handover. No executable derivation logic or stored outputs were changed.

### Next

M05_03 — Sionna Radio Reference Validation.

---

## 2026-09-10 — M05_01 V1.1 Telemetry Correction and V1.2 Freeze Closeout

### Corrected

- replaced the earlier healthy telemetry V1 lineage after formal KPI-readiness validation exposed cross-counter inconsistencies
- qualified the revised V1.1 generator on a 7-day pilot
- generated and confirmed the corrected 92-day canonical V1.1 baseline
- moved durable working persistence from Kaggle to Google Drive
- corrected the Cell 03 schema SHA transcription in the control lineage
- added the previously omitted Cell 03 KPI taxonomy to the foundation registry
- reconciled timestamp-driven artifact-byte drift without changing semantic identities
- established the complete 11-artifact Cells 03–12 foundation registry
- established the authoritative M05_01 V1.2 freeze
- persisted and verified the 17-file frozen foundation bundle
- completed `M05_01_CLOSEOUT_PASS=True`

### Authoritative identities

```text
M05_01 freeze V1.2
4a9f6ecec30613c160b618dfe50e11e63b8f4c8c24d06eac351d5275c744a968

Foundation bundle index
55c8ef51f905945fb825fad3bb35b932ccf7e140f5ffe9d85d3430071ff7143b

Foundation persistence
936b605cb1ce3c2d2b2977fed537df65c5e61e19e26ff655f89b27b919d62879

Canonical telemetry V1.1
c1fb3a49eacd63f45a98986322d536b74d21e585ff8bc49a4649ef11b3b34cd7
```

### Preservation decision

The invalidated V1 telemetry, intermediate V1.1 reconciliation/freeze and historical Kaggle artifacts are not deleted. They remain superseded provenance and are not authorized M05_02 restore sources.

Kaggle archival of the corrected final artifacts is deferred to platform clean-up.

### Next

M05_02 — Runtime Restore + Formal KPI Derivation + Healthy Validation.

---

## 2026-09-09 — Initial M05_01 Foundation Milestone

### Added

- Module 5 architecture / causal-observability reference
- post-M05_01 M05_00 V1.1 reference refresh
- initial M05_01 executed foundation + healthy telemetry notebook
- 3GPP-aligned Accessibility KPI/PM foundation
- causal-observability configuration and operational telemetry contract
- deterministic 10-site / 30-cell synthetic topology
- initial 7-day generator-qualification pilot
- initial 92-day healthy telemetry baseline
- initial provenance / freeze / persistence controls
- Module 5 GitHub documentation, requirements and validator

### Historical note

The telemetry and persistence lineage created during this milestone was subsequently superseded by the corrected 2026-09-10 V1.1 telemetry and V1.2 freeze closeout. The historical M05_00 V1 notebook remains preserved because its SHA is embedded in the current M05_01 provenance chain.
