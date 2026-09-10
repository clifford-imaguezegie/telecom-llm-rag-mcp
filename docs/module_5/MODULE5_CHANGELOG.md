# Module 5 Changelog

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
