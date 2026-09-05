# Notebook Cleanup Report

## Source

Original master notebook:

`telecom_ai_module_4_llm_rag_mcp_knowledge_base (1).ipynb (original uploaded master)`

Original SHA-256:

`a3b958559dc72b0496361cec70605b41d1f02e2bd46421d3a7a80da09dbfc855`

Cleaned GitHub notebook:

`notebooks/module_4/20_rag_mcp_hybrid.ipynb` (published GitHub filename)

Cleaned SHA-256:

`a385f446d59bd8d77daeead8b4873105d4807a7de2818449be0d668f1c9f7e2e`

## Preservation guarantee

The cleanup was performed **without re-running or deleting any executed code cell**.

Validation result:

- original notebook cells: **97**
- cleaned notebook cells: **122**
- executed/code cells: **39**
- code-cell source preserved: **YES**
- code-cell execution counts preserved: **YES**
- code-cell metadata preserved: **YES**
- code-cell outputs preserved: **YES**
- code-cell fingerprint sequence identical before/after cleanup: **YES**
- code cells deleted: **0**
- code outputs deleted: **0**

The extra cells are Markdown documentation inserted around previously undocumented execution stages.

## Existing Markdown updated

**32 existing Markdown cells** were revised for naming, numbering, factual accuracy or GitHub readability.

Key corrections include:

- replaced the obsolete two-generator / OTel design in the opening blueprint;
- documented the actual three generators;
- replaced OTel with the actual independent judge: IBM Granite 4.2 8B;
- corrected `IMB` → `IBM`;
- corrected old judge context/output limits to the final formal `20,480 / 12,288` configuration;
- corrected Gemma runtime wording from “both T4 GPUs” to the actual NVIDIA L4 deployment;
- corrected Qwen3.8/Qwen3.5 naming and natural-routing labels;
- corrected the obsolete Cell 12D two-pass description;
- clarified that formal generation used one naturally selected route per question rather than a forced 3-route answer matrix;
- normalized section/cell headings and repaired typos such as `Rettrieval`, `Routinf`, and `Pathces`;
- restructured the final technologies/processes section under the final research findings.

## Markdown added around undocumented executed cells

New documentation was inserted around:

- Section 0 initialization completion;
- Version B restore validation;
- MCP service validation;
- requirement-bounded sufficiency patch/hotfix;
- Cell 8A/8B pilot outcomes;
- Qwen3.8 load-recovery cleanup;
- Qwen3.5 release/resource/load/qualification/formal stages;
- Cell 12C 47/48 formal judge outcome;
- Cell 12D Kaggle artifact restoration and deterministic analysis;
- final artifact archival to Google Drive;
- final Kaggle dataset publication.

## Why outputs were retained

The notebook contains an expensive multi-model execution trace that required more than a normal interactive rerun. The preserved outputs are part of the experimental evidence and allow GitHub reviewers to inspect:

- model loading;
- retrieval diagnostics;
- formal generation;
- independent judging;
- fault handling;
- CPU post-hoc analysis;
- artifact archival.

Cleaning therefore focused on **documentation and structure**, not on making the notebook appear as if it had been executed once without engineering iteration.


## Legacy executed-label note

One non-functional description string inside the preserved Cell 12A code says `Qwen3 8B`. It is intentionally not edited because the code/output execution record is preserved exactly. The surrounding Markdown now clarifies that the actual formal model was **Qwen3.8 27B** and the formal artifacts carry the correct model ID and revision.
