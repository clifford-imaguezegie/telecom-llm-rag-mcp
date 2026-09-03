# Module 3 Results

## `frozen_benchmark/`
Contains the canonical Version A and Version B experiment artifacts used by Notebook 19: eight detailed JSON files plus eight CSV summaries.

These are the **source-of-truth frozen benchmark inputs** for post-hoc analysis.

## `final_analysis/`
Contains GitHub-friendly CSV and JSON exports reconstructed from the executed Notebook 19 display outputs. They include:

- judge experiment summary and judge usage;
- paired Version A/B comparisons;
- cross-model scorecards;
- runtime characteristics and latency outliers;
- integrated evaluation scorecard;
- evidence-backed key findings;
- Qwen exclusion record;
- analysis provenance manifest.

### Raw judge checkpoint note
Notebook 19 originally wrote two Colab runtime checkpoints:

- `module3_llm_judge_quality_results.jsonl`
- `module3_llm_judge_grounding_results.jsonl`

Those runtime files were not downloaded. The executed notebook retains their validated aggregate results, but not every raw justification/metadata field, so the JSONL files are intentionally **not reconstructed or fabricated**. Exact regeneration would require rerunning the judge cells.
