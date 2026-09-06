# Artifact Guide

## GitHub-curated artifacts

This package keeps the files that are most useful for peer review, result inspection and reproducibility without duplicating every transient runtime file.

### `results/module_4/formal_runs/`

Contains:

- three formal generator result JSONs;
- generator summary CSVs;
- generator manifests;
- Granite runtime manifest;
- Granite rubric qualification results;
- Granite formal judgment results;
- Granite summary CSV;
- Granite formal manifest;
- Granite failure record.

### `results/module_4/final_analysis/`

Contains all persisted outputs from:

- **Cell 12D** — technical quality + evidence grounding analysis;
- **Cell 13** — consolidated RAG vs MCP vs Hybrid analysis.

This includes the final metric JSON, case-level CSVs and plots.

### `results/module_4/frozen_benchmark/`

Contains:

- frozen Module 4 benchmark;
- frozen experiment configuration.

## Intentionally excluded from GitHub package

The following classes of files are retained in the external full archive but excluded here to reduce duplication/noise:

- duplicate result files;
- per-model checkpoints that duplicate completed result payloads;
- archived/incompatible judge checkpoints;
- vLLM server logs;
- intermediate diagnostic CSV/JSON files not required to interpret the final result;
- the complete archive ZIP itself.

## External complete archive

The complete experiment bundle was archived to:

- Google Drive as `module4_complete_artifacts_20260905_121301.zip`;
- Kaggle dataset: `cliffordimaguezegie/telecom-ai-module-4-outputs`.

The Kaggle dataset was private at the time of archival.

## Integrity

A SHA-256 manifest for every file included in this GitHub-ready package is written to:

`results/module_4/artifact_manifest.csv`
