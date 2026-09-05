# Module 2 Results

This folder contains the public result artifacts for the frozen Module 2 RAG V1 experiment.

## Public result exports

`public_results/` contains 10 normalized JSON files:

- 5 systems × Track 1
- 5 systems × Track 2

Systems:
- Essential AI Only
- Essential AI + RAG
- OTel 2.0 Only
- Gemma 4 Only
- Gemma 4 + RAG

## Why these exports are normalized

The original experiment files used several slightly different schemas. In particular:
- some files wrapped records under `metadata/results`, while others were raw lists;
- Gemma standalone exports used `id/prompt/response`;
- other exports used `question_id/question/answer`;
- some standalone Gemma files omitted embedded benchmark reference fields;
- RAG result files contained full retrieved source excerpts and Colab-local paths.

The public exports normalize those differences while preserving the original generated answers and experiment status.

For RAG evidence, the public files retain:
- retrieval query and Top-K;
- rank and similarity score;
- vector, chunk and document IDs;
- source and title;
- evidence text character count;
- SHA-256 fingerprint of the evidence text.

They intentionally omit:
- long retrieved source text;
- local filesystem paths.

The original source-file SHA-256 values are recorded in `analysis_manifest.json`, allowing the public exports to remain traceable to the frozen experiment artifacts.

## Benchmark questions

Canonical question templates are stored separately under:

`benchmarks/module_1_2/`

This keeps question definitions separate from generated results.
