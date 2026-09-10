# M05_02 Notebook Review

## Notebook reviewed

`M05_02_Runtime_Restore_KPI_Derivation_and_Healthy_Validation_v1.ipynb`

## Review outcome

**PASS — no executable KPI derivation changes are required.**

The executed notebook contains 72 cells: 20 code cells and 52 markdown cells. All stored code-cell outputs are successful, no stored exception output remains, and all code cells pass Python syntax compilation.

## Standards and mathematical alignment

The review confirmed that the implemented calculations are aligned with the frozen M05_01 standards contract and with the corresponding TS 28.554 Accessibility definitions:

- Partial DRB Accessibility uses RRC setup SR × UE-associated NG-connection SR × DRB establishment SR × 100.
- `mo-Signalling` is excluded from the RRC and NG establishment cause sums.
- Total DRB Accessibility combines Initial DRB, Added DRB and Resume paths with the required inverse success-ratio adjustments.
- RRC Resume handling excludes RNA-update causes; the current synthetic V1.1 baseline contains no RNA-update Resume cause.
- SubNetwork KPI values are computed as the average over contributing NRCellCUs.
- all formal KPI values are validated as finite and within 0–100%.

## Final executed evidence

```text
M05_02_FOUNDATION_RESTORE_PASS=True
M05_02_TELEMETRY_RESTORE_PASS=True
M05_02_FORMULA_BINDING_PASS=True
M05_02_PARTIAL_KPI_PASS=True
M05_02_TOTAL_KPI_PASS=True
M05_02_HEALTHY_VALIDATION_PASS=True
M05_02_PERSISTENCE_PASS=True
M05_02_CLOSEOUT_PASS=True
```

Result coverage:

```text
30 NRCellCU × 8,832 intervals × 3 5QI = 794,880 cell-level KPI records
8,832 intervals × 3 5QI = 26,496 SubNetwork KPI records
```

## Documentation-only corrections applied

1. normalized the notebook title/cell heading hierarchy;
2. added the missing Cell 10 anchor;
3. corrected the Introduction completion-gate variable from the unused `M05_02_RESTORE_CONTRACT_PASS` wording to the actual `M05_02_RESTORE_CONTRACT_DEFINED`;
4. added the formal-validation and KPI-persistence terminal gates to the completion description;
5. added the Cell 01 observation gate;
6. clarified that `RRC.ResumeAtt.Cause` / `RRC.ResumeSucc.Cause` are internal canonical telemetry names rather than TS 28.552 measurement spellings;
7. strengthened the final handover with durable M05_02 output hashes and the downstream no-replay rule.

These edits do not alter executable calculations. A full notebook rerun is therefore not required.

## Durable M05_02 identities

```text
NRCellCU KPI SHA-256
709c9883bad799dec3907624a7590f5e44356d9fef7c00f4446d165fd1b2223f

SubNetwork KPI SHA-256
18d5a60ca91139242e85e9f5468346a66bedf70f8736e01507568f2afb9c42ba

KPI derivation manifest semantic SHA
3b0d6271c0aba98d3cf0ac3907ec21fea7fc113ba865ae8f6f0cdf864dd5104e

Validation receipt semantic SHA
08d12c9564b3d5dff14f4770a3bfbf0d4853df1a3dcbbfd824511102051b66ae
```

## Downstream decision

M05_02 is accepted as the frozen deterministic healthy Accessibility KPI baseline.

M05_03 onward should validate the frozen upstream identities in one consolidated bootstrap/provenance cell and then proceed directly to new stage-specific work. Rebuilding M05_01 telemetry, re-hashing all 92 partitions and re-deriving M05_02 Accessibility KPIs are not normal downstream steps.
