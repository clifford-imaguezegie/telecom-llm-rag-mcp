# Module 5 Status

## Current state

**Module 5 is in progress. M05_02 — Runtime Restore + Formal KPI Derivation + Healthy Validation is complete and validated.**

### Completed M05_02 outcomes

- restored the authoritative M05_01 V1.2 foundation bundle and V1.1 canonical telemetry
- verified all 92 canonical Parquet partitions and the full 18,829,824-row observation inventory
- restored the frozen TS 28.554 Accessibility KPI knowledge contract
- bound all 16 formal dependencies to canonical telemetry
- validated three configured 5QI values: 1, 5 and 9
- aggregated 264,960 NRCellCU × interval control-plane records
- aggregated 794,880 NRCellCU × interval × 5QI DRB records
- derived Partial DRB Accessibility for all 794,880 records
- derived Total-RRC and RRC Resume supporting ratios with zero hierarchy violations
- derived Total DRB Accessibility for all 794,880 records
- completed formal coverage, denominator, hierarchy and 0–100% range validation
- established healthy cell-level and SubNetwork descriptive baselines
- created 26,496 SubNetwork × interval × 5QI KPI records with all 30 cells contributing to every point
- persisted immutable NRCellCU and SubNetwork KPI Parquet products to Google Drive
- persisted KPI derivation manifest and validation receipt
- `M05_02_CLOSEOUT_PASS=True`

### Healthy baseline summary

```text
Partial DRB Accessibility
mean: 99.323222%
min : 92.044707%
max : 100.000000%

Total DRB Accessibility
mean: 99.525220%
min : 94.326606%
max : 100.000000%

SubNetwork Partial mean: 99.323222%
SubNetwork Total mean  : 99.525220%
```

These values describe the synthetic healthy baseline; they are not asserted as universal 3GPP operational thresholds.

### Authoritative identities

```text
M05_01 freeze V1.2 semantic SHA
4a9f6ecec30613c160b618dfe50e11e63b8f4c8c24d06eac351d5275c744a968

Canonical telemetry semantic SHA
c1fb3a49eacd63f45a98986322d536b74d21e585ff8bc49a4649ef11b3b34cd7

NRCellCU KPI SHA-256
709c9883bad799dec3907624a7590f5e44356d9fef7c00f4446d165fd1b2223f

SubNetwork KPI SHA-256
18d5a60ca91139242e85e9f5468346a66bedf70f8736e01507568f2afb9c42ba

M05_02 KPI manifest semantic SHA
3b0d6271c0aba98d3cf0ac3907ec21fea7fc113ba865ae8f6f0cdf864dd5104e

M05_02 validation receipt semantic SHA
08d12c9564b3d5dff14f4770a3bfbf0d4853df1a3dcbbfd824511102051b66ae
```

## Downstream restore rule

M05_03 onward should verify the frozen upstream identities in a consolidated bootstrap/provenance cell and then begin new work. The full M05_02 physical verification and KPI derivation workflow is not repeated unless the authoritative upstream lineage changes.

## Next stage

**M05_03 — Sionna Radio Reference Validation**

M05_03 will introduce an independent radio-reference layer while preserving M05_01/M05_02 as immutable network-truth and KPI-truth baselines.
