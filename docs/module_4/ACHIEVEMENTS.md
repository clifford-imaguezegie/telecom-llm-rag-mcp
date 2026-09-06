# Achievements

Module 4 moved the project from isolated retrieval experiments to a reproducible, multi-retriever, multi-model telecom knowledge architecture.

## Technical achievements

### 1. Reused frozen RAG without rebuilding it

- restored BGE-M3 + FAISS;
- retained frozen chunking, embeddings and metadata;
- prevented post-hoc RAG tuning against the Module 4 benchmark.

### 2. Reused the Version B Knowledge-Based MCP service

- restored the persistent 21-shard DuckDB BM25/FTS knowledge base;
- exposed the specialized knowledge service through FastMCP;
- retained source-aware standards and technical-literature provenance.

### 3. Built a true RAG + MCP Hybrid path

- concurrent RAG and MCP execution;
- same-query fairness control;
- normalized evidence schema;
- exact and near-duplicate handling;
- Reciprocal Rank Fusion;
- bounded evidence/context presentation.

### 4. Implemented natural retrieval routing

The generator selects `RAG_ONLY`, `MCP_ONLY` or `HYBRID` without seeing the hidden stress-route label.

This turns retrieval selection into a model behaviour that can be evaluated rather than a hard-coded benchmark answer.

### 5. Implemented adaptive evidence acquisition

- explicit answer requirements;
- evidence-sufficiency assessment;
- refined queries;
- up to three rounds;
- preserved `MAX_RETRIEVAL_ROUNDS` as a diagnostic outcome.

This becomes a direct precursor to the investigation loop in Module 5 Agentic Telecom AI.

### 6. Executed three local open-weight generator families

- Gemma 4 12B QAT W4A16
- Qwen3.8 27B runtime INT4
- Qwen3.5 9B runtime INT4
- vLLM-based serving
- pinned revisions and runtime manifests

### 7. Added independent blind LLM-as-a-judge evaluation

IBM Granite 4.2 8B was qualified on synthetic controls and then used as a separate evaluator.

The judge is blind to generator identity and operational metadata.

### 8. Separated semantic quality from operational reliability

The experiment preserves both:

- answer meaning / grounding quality;
- generation completion / validation behaviour.

This exposed an important practical finding: truncated outputs may remain semantically useful but are still operationally unreliable.

### 9. Added formal negative-control testing

The fictional proprietary alarm case tests whether the system abstains rather than inventing unavailable vendor-specific knowledge.

### 10. Built a fault-tolerant formal judge harness

- per-case checkpointing;
- failure preservation;
- incompatible-checkpoint archival;
- continuation after individual errors;
- no silent coercion of invalid judge outputs.

### 11. Established reproducibility controls

- frozen benchmark SHA;
- frozen rubric SHA;
- exact model revisions;
- config hashes;
- formal result manifests;
- preserved failure artifact;
- deterministic composite scoring.

### 12. Separated expensive inference from CPU analysis

The final Cell 12D/13 analysis runs only on persisted artifacts using Pandas/NumPy/Matplotlib.

This allows analysis to continue even after the original GPU runtime is lost.

### 13. Persisted the complete experimental record externally

- complete Google Drive archive;
- versioned Kaggle dataset;
- GitHub-curated formal/analysis subset;
- no need to repeat a >12-hour execution simply to inspect or publish results.

## Quantitative achievements

- **48 / 48 formal generator cases completed**
- **47 / 48 valid independent judgments preserved**
- **97.92% independent-evaluation completeness**
- **Gemma 4: 92.50% mean quality on the fair Q1–Q15 set**
- **Gemma 4: 0 major errors on the common set**
- **Qwen3.8: 85.08% mean quality**
- **Qwen3.5: 72.92% mean quality**
- **Both successfully judged Qwen Q16 responses abstained correctly**

## Research achievement

Module 4 provides empirical support for an adaptive knowledge-access design:

> Do not treat Hybrid retrieval as automatically superior. Give the system access to complementary RAG and MCP mechanisms, measure evidence sufficiency, and let orchestration decide which mechanism is necessary for the current evidence need.
