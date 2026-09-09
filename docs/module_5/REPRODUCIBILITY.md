# Module 5 Reproducibility

## M05_01 execution model

M05_01 intentionally uses a two-pass generator workflow. A clean rebuild is therefore not a simple one-pass Run All.

1. Execute Cells 01–12.
2. Run Cell 13 as `PILOT_7D`.
3. Run Cell 14 and require pilot qualification to pass.
4. Return to Cell 13 and rerun the unchanged generator as `CANONICAL_92D`.
5. Run Cells 15–18 for canonical persistence, provenance reconciliation, foundation freeze and durable foundation persistence.

## Preferred M05_02 workflow

M05_02 should **restore rather than rebuild** M05_01:

1. retrieve the frozen foundation bundle,
2. validate the M05_01 freeze semantic identity,
3. retrieve/load canonical telemetry,
4. validate the canonical dataset semantic identity,
5. derive formal KPI values deterministically,
6. perform healthy-state validation.

## Root-of-trust identities

- M05_01 freeze semantic SHA: `3a519602da5e211df684786441c41669fbfdaac1c0d13254d18187ad5ce874e8`
- canonical dataset semantic SHA: `d6b75444faf53d602edf952f4620fe02f2f3a4ea68431a4889e4829adf008f4d`
- provenance reconciliation semantic SHA: `16aaefc2282a0d43caec53a3aee33d0b12aa02e2b2d64b3a2d408d99e86cd521`
- foundation persistence semantic SHA: `fb4815ad27a88951b4b5f4d14a942510e07191aeb366929fcfec3701fee20413`

## Data boundary

All M05_01 telemetry is synthetic. No production operator data, subscriber information or customer network telemetry is included.
