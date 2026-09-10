# Module 5 Reproducibility

## M05_01 execution model

M05_01 now uses a gated pilot-to-canonical workflow rather than the earlier two-pass Cell 13 procedure.

A clean rebuild should execute:

1. Cells 01–12 — standards, graph, topology and observation foundation.
2. Cell 13 — generate the 7-day V1.1 pilot.
3. Cell 14 — structural/basic integrity qualification; require `DATA_OVERVIEW_PASS=True`.
4. Cell 15 — telecom semantic and KPI-readiness validation; require `PILOT_QUALIFICATION_PASS=True`.
5. Cell 16 — generate the 92-day canonical healthy baseline.
6. Cell 17 — persisted canonical confirmation; require `CANONICAL_CONFIRMATION_PASS=True`.
7. Cell 18 — persist the telemetry qualification receipt.
8. Cell 19 — persist and independently verify canonical telemetry on Google Drive.
9. Cell 20 then Cell 21 — preserve the intermediate V1.1 supersession/freeze control lineage.
10. Cell 20A then Cell 21A — reconcile the complete 11-artifact foundation registry and establish the authoritative V1.2 freeze.
11. Cell 22 — persist the frozen foundation bundle and require `M05_01_CLOSEOUT_PASS=True`.

The Cell 20A / Cell 21A correction changes control metadata only. It does not regenerate or modify the foundation semantic state or V1.1 telemetry.

## Why the V1.2 correction exists

The final foundation audit identified:

- a 63-character transcription of the Cell 03 schema SHA in the intermediate control record,
- omission of the Cell 03 KPI taxonomy from the frozen foundation inventory,
- byte-SHA drift for timestamp-bearing Cells 04 and 06 while their deterministic semantic SHAs remained unchanged.

The corrected V1.2 registry freezes the exact current bytes and verified semantic identities of all 11 foundation artifacts.

## Preferred M05_02 workflow

M05_02 should **restore rather than rebuild** M05_01:

1. mount Google Drive;
2. load the frozen foundation bundle V1.2;
3. verify the bundle index, persistence receipt and V1.2 freeze;
4. reconstruct and verify all 11 foundation artifacts;
5. load the canonical telemetry V1.1;
6. verify the canonical manifest and dataset semantic identity;
7. derive formal TS 28.554 KPI values deterministically;
8. validate the healthy KPI baseline.

## Root-of-trust identities

- M05_01 freeze V1.2 semantic SHA: `4a9f6ecec30613c160b618dfe50e11e63b8f4c8c24d06eac351d5275c744a968`
- foundation identity reconciliation semantic SHA: `8366a6e8bee9ddfdbcc665a668caac50e1bba86c02730f48277250206279e4d9`
- foundation bundle index semantic SHA: `55c8ef51f905945fb825fad3bb35b932ccf7e140f5ffe9d85d3430071ff7143b`
- foundation persistence semantic SHA: `936b605cb1ce3c2d2b2977fed537df65c5e61e19e26ff655f89b27b919d62879`
- telemetry qualification semantic SHA: `fc3c38f980209b1d5a9504b30f98efa6636ba7eedc153ef4f4d1e7bb49be156a`
- canonical dataset semantic SHA: `c1fb3a49eacd63f45a98986322d536b74d21e585ff8bc49a4649ef11b3b34cd7`
- canonical manifest artifact SHA: `e856ffe3f7ed97e6ad4592e999e5fd3adf5993f80ac72cdada1f374ab6543411`

## Data boundary

All M05_01 telemetry is synthetic. No production operator data, subscriber information or customer network telemetry is included.
