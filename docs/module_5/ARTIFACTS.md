# Module 5 Artifact Policy

## GitHub artifacts

The Git repository contains the curated artifacts needed to understand, validate and continue Module 5:

- M05_00 historical and current reference notebooks
- executed / cleaned M05_01 notebook
- architecture, status and reproducibility documentation
- foundation requirements
- static validation script

## Private durable artifacts

Large or runtime-generated datasets are intentionally not committed to Git.

### Canonical healthy telemetry

```text
cliffordimaguezegie/module5-5g-ran-healthy-telemetry-v1
```

- 92-day healthy baseline
- 92 daily Parquet partitions
- 18,829,824 observations
- dataset semantic SHA: `d6b75444faf53d602edf952f4620fe02f2f3a4ea68431a4889e4829adf008f4d`

### Frozen foundation bundle

```text
cliffordimaguezegie/module5-m05-01-foundation-artifacts-v1
```

- 23 frozen JSON foundation artifacts
- one deterministic bundle index
- 24 verified remote files
- bundle index semantic SHA: `a24c052f9f79ccbd1d8b246765b0506bc817b14d89038239fea4ca58d19c8305`
- persistence semantic SHA: `fb4815ad27a88951b4b5f4d14a942510e07191aeb366929fcfec3701fee20413`

## Provenance rule

`M05_00_..._v1.ipynb` is preserved because its exact byte SHA is referenced by M05_01 provenance. `M05_00_..._v1_1.ipynb` is a post-M05_01 documentation refresh and does not rewrite that historical identity.

Private Kaggle datasets are not public data sources and must not be presented as production/operator telemetry. The M05_01 telemetry is synthetic.
