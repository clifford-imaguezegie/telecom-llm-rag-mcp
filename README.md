# Telecom AI Engineering Platform

An experimental telecom AI engineering project exploring the progressive integration of **Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), Model Context Protocol (MCP), adaptive knowledge access, AI agents, production AI architecture, and autonomous network operations**.

The project investigates how general-purpose and telecom-oriented LLMs can be progressively combined with:

* controlled telecom knowledge,
* semantic and lexical retrieval,
* standardized MCP interfaces,
* adaptive evidence acquisition,
* evidence-grounded reasoning,
* independent evaluation,
* agentic workflows,
* network observability,
* controlled network actions,
* and eventually closed-loop telecom automation.

The project is intentionally developed as a sequence of controlled architectural experiments rather than as a single end-state application.

---

# Project Objective

The objective is to evaluate the evolution of telecom AI systems through progressively more capable architectural stages:

```text
Standalone LLM
      ↓
Telecom RAG
      ↓
Knowledge-Based MCP
      ↓
Adaptive RAG + MCP Hybrid
      ↓
Agentic Telecom AI
      ↓
Production Architecture + RAG V2
      ↓
Autonomous Telecom Operations
```

Each major stage is:

1. implemented,
2. benchmarked,
3. independently evaluated where appropriate,
4. diagnostically analyzed,
5. retained as a frozen or controlled baseline,
6. and then extended in the next architectural stage.

The project evaluates more than benchmark accuracy.

Key engineering dimensions include:

* technical correctness,
* requirement coverage,
* engineering reasoning,
* evidence grounding,
* evidence–answer consistency,
* unsupported-claim control,
* retrieval quality,
* retrieval routing,
* evidence sufficiency,
* tool-use behaviour,
* runtime reliability,
* latency,
* token efficiency,
* failure preservation,
* reproducibility,
* architecture design,
* and practical applicability to telecom engineering and operations.

---

# Project Roadmap

| Module       | Architecture                                    | Status      |
| ------------ | ----------------------------------------------- | ----------- |
| **Module 1** | Standalone LLM baseline                         | ✅ Completed |
| **Module 2** | Telecom RAG V1 + expanded multi-model benchmark | ✅ Completed |
| **Module 3** | Knowledge-Based MCP + cross-LLM evaluation      | ✅ Completed |
| **Module 4** | Adaptive RAG + Knowledge-Based MCP Hybrid       | ✅ Completed |
| **Module 5** | Agentic Telecom AI                              | 🔄 Next     |
| **Module 6** | Production Architecture + RAG V2                | ⏳ Planned   |
| **Module 7** | Autonomous Telecom Operations                   | ⏳ Planned   |

---

# Repository Organization

The repository is organized by architectural module so that each experimental stage remains identifiable as the project grows.

```text
.
├── notebooks/
│   ├── module_1/
│   │   └── 01_llm_base.ipynb
│   │
│   ├── module_2/
│   │   ├── 02_rag_stage_1.ipynb
│   │   ├── 03_essentialai_rag_v1.ipynb
│   │   ├── 04_essentialai_only.ipynb
│   │   ├── 05_otel2_only.ipynb
│   │   ├── 06_gemma4_only.ipynb
│   │   ├── 07_gemma4_rag_v1.ipynb
│   │   └── 08_rag_evaluation.ipynb
│   │
│   ├── module_3/
│   │   ├── 09_version_a_claude_sonnet.ipynb
│   │   ├── 10_version_a_claude_haiku.ipynb
│   │   ├── 11_version_a_gemma4.ipynb
│   │   ├── 12_version_a_deepseek_v4.ipynb
│   │   ├── 13_qwen3_8_exclusion_record.ipynb
│   │   ├── 14_version_b_build.ipynb
│   │   ├── 15_version_b_claude_sonnet_runtime.ipynb
│   │   ├── 16_version_b_claude_haiku_runtime.ipynb
│   │   ├── 17_version_b_gemma4_runtime.ipynb
│   │   ├── 18_version_b_deepseek_v4_runtime.ipynb
│   │   └── 19_module3_final_ab_cross_llm_analysis.ipynb
│   │
│   └── module_4/
│       └── 20_rag_mcp_hybrid.ipynb
│
├── docs/
│   ├── module_3/
│   │   ├── ARCHITECTURE.md
│   │   ├── EVALUATION.md
│   │   └── supporting review changelogs
│   │
│   └── module_4/
│       ├── ARCHITECTURE.md
│       ├── EVALUATION.md
│       ├── RESULTS.md
│       ├── ACHIEVEMENTS.md
│       ├── REPRODUCIBILITY.md
│       ├── LIMITATIONS.md
│       ├── ARTIFACTS.md
│       ├── NOTEBOOK_CLEANUP_REPORT.md
│       └── MODULE4_CHANGELOG.md
│
├── results/
│   ├── module_1/
│   ├── module_2/
│   ├── module_3/
│   │   ├── frozen_benchmark/
│   │   └── final_analysis/
│   │
│   └── module_4/
│       ├── README.md
│       ├── artifact_manifest.csv
│       ├── frozen_benchmark/
│       ├── formal_runs/
│       │   ├── gemma4/
│       │   ├── qwen38/
│       │   ├── qwen35/
│       │   └── granite_judge/
│       └── final_analysis/
│
├── requirements/
│   ├── module_4_runtime.txt
│   └── module_4_analysis.txt
│
├── scripts/
│   ├── module_3/
│   │   └── validate_module3_notebooks.py
│   │
│   └── module_4/
│       └── validate_module4_notebook.py
│
├── src/
│   └── llm/
│
├── .gitattributes
├── .gitignore
└── README.md
```

Large runtime logs, checkpoints, redundant intermediate artifacts and complete experiment archives are intentionally retained outside the Git repository.

The GitHub repository contains the curated artifacts required to understand and reproduce the formal analyses.

---

# Module 1 — Standalone LLM Baseline

Module 1 established the initial telecom LLM benchmark and experimental methodology used throughout the later modules.

## Models Evaluated

* **General LLM:** `EssentialAI/rnj-1-instruct`
* **Telecom LLM / OTel 1.0:** `farbodtavakkoli/OTel-LLM-8.3B-IT`
* **Independent Judge:** `Qwen/Qwen2.5-7B-Instruct`

OTel 1.0 is derived from the `rnj-1-instruct` lineage and underwent telecom-specific post-training, providing a useful comparison between general-purpose and domain-specialized model behaviour.

---

## Module 1 Benchmark Framework

Two benchmark tracks were established.

### Track 1 — Custom Telecom Engineering Benchmark

**20 questions** covering topics including:

* 5G Core,
* 5G RAN,
* 5G Standalone procedures,
* Open RAN,
* Kubernetes,
* cloud-native telecom,
* capacity and performance,
* troubleshooting,
* fault isolation,
* network architecture,
* and end-to-end engineering reasoning.

### Track 2 — Industry Telecom Benchmark

**32 questions** covering benchmark families including:

* 3GPP,
* O-RAN,
* 6G,
* srsRAN,
* telecom logs,
* telecom mathematics,
* telecom Q&A,
* and telecom tables.

---

## Module 1 Results

### Track 1

| System                         | Questions Won | Win Rate | Average Expert Score |
| ------------------------------ | ------------: | -------: | -------------------: |
| **EssentialAI/rnj-1-instruct** |   **13 / 20** |  **65%** |       **72.8 / 100** |
| OTel 1.0                       |        7 / 20 |      35% |           60.1 / 100 |

### Track 2

| System                         | Questions Won |  Win Rate | Average Expert Score |
| ------------------------------ | ------------: | --------: | -------------------: |
| **EssentialAI/rnj-1-instruct** |   **23 / 32** | **71.9%** |       **70.1 / 100** |
| OTel 1.0                       |        7 / 32 |     21.9% |           32.1 / 100 |
| Ties                           |        2 / 32 |      6.3% |                    — |

Across the combined **52 questions**, EssentialAI won **36 / 52 (69.2%)**.

### Module 1 Conclusion

> **Technical fluency and concise responses do not guarantee technical correctness.**

The experiment also demonstrated that telecom-domain specialization alone does not automatically guarantee stronger engineering performance.

Module 1 established the standalone baseline carried into Module 2.

---

# Module 2 — Telecom RAG V1

Module 2 expanded the project from standalone LLM evaluation into **Retrieval-Augmented Generation** and multi-model comparison.

## Systems Evaluated

1. Essential AI + RAG
2. Essential AI Only
3. OTel 2.0 Only
4. Gemma 4 Only
5. Gemma 4 + RAG

The module introduced:

* a large telecom knowledge corpus,
* semantic embeddings,
* FAISS vector retrieval,
* RAG generation,
* newer standalone models,
* independent engineering evaluation,
* objective benchmark scoring,
* and detailed RAG failure diagnosis.

---

## RAG V1 Knowledge Architecture

The indexed telecom corpus includes documentation from sources such as:

* 3GPP,
* ETSI,
* ITU-T,
* GSMA,
* O-RAN,
* TM Forum,
* CAMARA,
* open-source telecom documentation,
* and cloud-native/Kubernetes material.

### Retrieval Configuration

* **Embedding model:** `BAAI/bge-m3`
* **Vector store:** FAISS
* **Embedding dimension:** 1024
* **Indexed vectors:** approximately 1.5 million
* **Historical RAG V1 retrieval:** Top-7 chunks

RAG V1 intentionally emphasized strict grounding in retrieved documentation.

---

# Module 2 Evaluation

The benchmark foundation remained:

* **Track 1:** 20 telecom engineering questions
* **Track 2:** 32 industry telecom questions

This preserved continuity with Module 1.

---

## Track 1 — Engineering Evaluation

Responses were evaluated across:

1. Technical Accuracy
2. Completeness
3. Relevance
4. Engineering Reasoning
5. Practical Applicability
6. Factual Reliability
7. Overall Score

### Results

| Rank | System             |    Mean Score |
| ---- | ------------------ | ------------: |
| 1    | **OTel 2.0 Only**  | **9.20 / 10** |
| 2    | **Gemma 4 Only**   | **9.00 / 10** |
| 3    | Gemma 4 + RAG      |     6.75 / 10 |
| 4    | Essential AI Only  |     5.80 / 10 |
| 5    | Essential AI + RAG |     5.65 / 10 |

The strongest Track 1 responses were produced by standalone OTel 2.0 and Gemma 4.

---

## Track 2 — Objective Expected-Answer Evaluation

| Rank | System                |     Correct |   Accuracy |
| ---- | --------------------- | ----------: | ---------: |
| 1    | **OTel 2.0 Only**     | **18 / 32** | **56.25%** |
| 2    | **Essential AI Only** | **13 / 32** | **40.62%** |
| 3    | Essential AI + RAG    |      8 / 32 |     25.00% |
| 3    | Gemma 4 + RAG         |      8 / 32 |     25.00% |
| 3    | Gemma 4 Only          |      8 / 32 |     25.00% |

---

# RAG V1 Findings

Module 2 demonstrated that retrieval augmentation is **not automatically beneficial simply because additional telecom context is provided to an LLM**.

Performance depended on:

* model capability,
* retrieved evidence,
* question type,
* evidence sufficiency,
* grounding policy,
* generation behaviour,
* and runtime reliability.

### Essential AI

Track 1:

* Essential AI Only: **5.80**
* Essential AI + RAG: **5.65**
* Delta: **−0.15**

Track 2:

* Essential AI Only: **40.62%**
* Essential AI + RAG: **25.00%**
* Delta: **−15.62 percentage points**

### Gemma 4

Track 1:

* Gemma 4 Only: **9.00**
* Gemma 4 + RAG: **6.75**
* Delta: **−2.25**

Track 2:

* Gemma 4 Only: **25.00%**
* Gemma 4 + RAG: **25.00%**

Identical aggregate accuracy concealed significant question-level changes.

---

# RAG V1 Failure Diagnosis

A targeted analysis was performed on **13 priority Track 1 degradation cases**.

Among those cases:

* **13 / 13** were primarily classified as `STRICT_GROUNDING_ABSTENTION`
* **11 / 13** contained `PARTIAL` retrieved evidence
* **2 / 13** contained `SUFFICIENT` retrieved evidence
* **0 / 13** were primarily classified as retrieval failures
* **13 / 13** were classified as generation or prompting failures

This showed that useful evidence often existed, but the generation layer did not exploit it effectively.

### Module 2 Conclusion

The desired future behaviour became:

> **Evidence-first grounded engineering reasoning rather than strict document extraction.**

RAG V1 is retained as a frozen experimental baseline rather than silently redesigned.

---

# Module 3 — Knowledge-Based MCP + Cross-LLM Evaluation

Module 3 introduced **Model Context Protocol (MCP)** as a standardized interface through which heterogeneous LLMs access telecom knowledge.

Importantly, Module 3 remains a **knowledge-based MCP implementation**.

It does not expose:

* live network KPIs,
* OSS actions,
* configuration changes,
* alarm handling,
* or operational control functions.

Those capabilities are intentionally deferred to the agentic and operational modules.

---

# Why MCP Was Introduced

Module 2 showed that embedding-based RAG alone does not solve every telecom knowledge or reasoning problem.

Module 3 therefore investigated whether telecom knowledge retrieval could be exposed through a **provider-neutral tool interface** that different LLMs could consume without embedding knowledge-access logic directly into model-specific applications.

The high-level architecture became:

```text
LLM
 │
 ▼
Unified MCP Knowledge Tool
 │
 ▼
Telecom Knowledge Retrieval
 │
 ├── 3GPP
 ├── Telecom Common Corpus
 └── Hybrid
 │
 ▼
Retrieved Evidence
 │
 ▼
LLM Response
```

---

# Module 3 — Version A

## Direct Query-Time Remote Retrieval

Version A performs retrieval directly from remote knowledge sources when the LLM invokes the MCP tool.

Knowledge paths include:

* dedicated 3GPP documentation,
* GSMA Telecom Common Corpus collections,
* and hybrid retrieval.

A deterministic router selects the appropriate retrieval family.

Version A established that a common MCP interface could successfully support multiple LLMs.

---

# Module 3 — Version B

## Persistent Knowledge-Base Retrieval

Version B replaced repeated remote query-time retrieval with a persistent normalized and deduplicated telecom knowledge base.

The persistent architecture contains:

* normalized telecom records,
* hash-based deduplication,
* telecom-aware tokenization,
* DuckDB BM25 / full-text search,
* dedicated 3GPP source-family shards,
* Telecom Common Corpus collection shards,
* and persistent reusable retrieval artifacts.

Version B contains approximately:

* **1.78 million indexed records**
* across **21 persistent search shards**

Both Version A and Version B expose the same public MCP knowledge-search interface.

The primary experimental variable is therefore the retrieval architecture rather than the LLM-facing MCP API.

---

# Module 3 Benchmark v2

The final controlled benchmark contains **8 telecom knowledge questions**:

* 5 focused primarily on 3GPP,
* 2 focused primarily on Telecom Common Corpus knowledge,
* 1 requiring Hybrid retrieval.

Topics include:

* AMF registration and mobility,
* inter-gNB handover,
* radio-link failure,
* QoS flows and 5QI,
* 5G authentication,
* QUIC,
* AI/ML traffic prediction,
* and HTTP/TLS mechanisms in the 5G Service-Based Architecture.

---

# Module 3 Cross-LLM Evaluation

The same MCP knowledge service was evaluated largely **out of the box** across:

* **Claude Sonnet 5**
* **Claude Haiku 4.5**
* **Gemma 4 26B A4B IT**
* **DeepSeek V4 Flash 0731**

Qwen3.8 Flash was excluded from the scored comparison because execution was blocked by upstream provider rate limiting through shared capacity.

The exclusion represents an external availability constraint rather than model or MCP failure.

---

# Module 3 Evaluation Principle

A critical design choice was to evaluate each participating LLM largely **out of the box under common constraints**.

The experiments preserved:

* the same frozen benchmark,
* the same system prompt,
* the same MCP interface,
* the same routing semantics,
* the same retrieval domains,
* the same search budget,
* and common orchestration limits.

No post-hoc model-specific tuning was performed after observing benchmark behaviour.

Module 3 therefore answers:

> **How do different LLMs naturally behave when connected to the same telecom MCP knowledge service?**

It does not claim to measure the maximum performance achievable after individually optimizing every model.

---

# Module 3 Key Findings

## 1. MCP Successfully Standardized Knowledge Access

All scored models successfully interacted with the same provider-neutral MCP knowledge tool.

Formal route accuracy reached **100% across the completed experiments**.

However, subsequent search behaviour differed materially by model.

---

## 2. Model-Agnostic MCP Did Not Produce Model-Agnostic Behaviour

Different models showed different tool-use patterns despite using the same interface.

### Claude Sonnet 5

* strongest overall technical-quality performance,
* high answer completeness,
* moderate iterative-search behaviour.

### Gemma 4

* strongest runtime efficiency,
* one MCP search per benchmark question,
* high relevance,
* strong preservation of discriminative query terms.

### Claude Haiku 4.5

* stronger iterative-search tendency,
* higher search and token consumption in Version B.

### DeepSeek V4 Flash 0731

* improved execution reliability and structural behaviour under Version B,
* but significant model/provider-side latency.

---

## 3. Retrieval Architecture Did Not Uniformly Determine Answer Quality

Version B improved:

* persistent indexing,
* source-family consistency,
* routing consistency,
* execution reliability,
* and reduced dependence on query-time remote availability.

However, those improvements did not automatically improve every downstream answer metric.

> **Better retrieval infrastructure does not guarantee better final answers unless the model retrieves and uses sufficiently complete evidence.**

---

## 4. Search-Query Generation Is a Model Capability

The effectiveness of MCP retrieval depends partly on the LLM's ability to formulate discriminative tool queries.

This became an important precursor to the adaptive retrieval behaviour evaluated in Module 4.

---

## 5. Technical Quality and Grounding Are Different Dimensions

Module 3 reinforced that:

```text
Technical correctness
        ≠
Completeness
        ≠
Relevance
        ≠
Evidence grounding
```

Each should be evaluated independently.

---

## 6. Runtime Performance Is Strongly Model/Provider Dependent

Slow LLM + MCP execution should not automatically be diagnosed as slow retrieval.

Retrieval latency and model/provider execution latency must be measured separately.

---

## 7. There Is No Single Best Model

Different models showed different strengths across:

* technical quality,
* grounding,
* latency,
* token efficiency,
* search discipline,
* and execution reliability.

Production model selection is therefore a **multi-objective engineering decision**.

---

# Module 3 Final Conclusion

> **A model-agnostic MCP interface successfully standardizes access to telecom knowledge, but model behaviour remains strongly model-specific.**

Module 3 established both the value and limitation of knowledge-based MCP:

> **MCP standardizes knowledge access, but does not by itself optimize how individual LLMs search for, interpret, and use that knowledge.**

This question became the starting point for Module 4.

---

# Module 4 — Adaptive RAG + Knowledge-Based MCP Hybrid

Module 4 investigated whether a telecom LLM can dynamically combine the two knowledge mechanisms established in earlier modules:

* **semantic RAG retrieval**, and
* **standardized MCP knowledge access**.

The central research question was:

> **Can a telecom LLM combine semantic RAG retrieval with a standardized MCP knowledge service more effectively than either mechanism independently?**

Rather than forcing a fixed architecture for every question, each generator was allowed to naturally select:

```text
RAG_ONLY
MCP_ONLY
HYBRID
```

The hidden benchmark expectations were not provided to the generator.

---

# Module 4 Architecture

```text
                        User Question
                              │
                              ▼
                       LLM Route Planner
                              │
                  ┌───────────┼───────────┐
                  │           │           │
                  ▼           ▼           ▼
              RAG_ONLY    MCP_ONLY     HYBRID
                  │           │           │
                  │           │      ┌────┴────┐
                  │           │      │         │
                  ▼           ▼      ▼         ▼
             BGE-M3 +      MCP KB   RAG       MCP
               FAISS        Search   │         │
                  │           │      └────┬────┘
                  │           │           │
                  │           │      Dedup + RRF
                  │           │           │
                  └───────────┴───────────┘
                              │
                              ▼
                     Evidence Sufficiency
                              │
                  ┌───────────┴───────────┐
                  │                       │
              Sufficient              Insufficient
                  │                       │
                  │                  Next retrieval
                  │                     round
                  │                       │
                  └───────────┬───────────┘
                              │
                              ▼
                       Evidence Synthesis
                              │
                              ▼
                         Final Answer
```

---

# Module 4 Retrieval Controls

The formal experiment standardized several controls across the retrieval mechanisms:

* **RAG top-k:** 5
* **MCP top-k:** 5
* **Maximum retrieval rounds:** 3
* **Maximum presented evidence items:** 5
* **Maximum context size:** approximately 12,500 characters
* **Hybrid execution:** concurrent RAG + MCP
* **Hybrid query policy:** same query sent to both retrievers
* **Fusion:** Reciprocal Rank Fusion
* **RRF k:** 60
* **Near-duplicate threshold:** 0.88

The existing Module 2 RAG V1 and Module 3 Version B MCP knowledge systems were reused rather than silently redesigned.

---

# Module 4 Benchmark

The frozen Module 4 benchmark contains **16 questions**.

It extends the Module 3 benchmark while adding stress cases designed to exercise different knowledge-access behaviours.

The benchmark includes:

* **8 continuity questions**
* **7 retrieval stress questions**
* **1 unsupported proprietary-knowledge negative control**

Domains include:

* 5G Core,
* mobility,
* RAN,
* QoS,
* security,
* internet transport,
* telecom AI research,
* O-RAN,
* Kubernetes/cloud-native 5G,
* 5G SBA,
* cross-layer fault isolation,
* and unsupported proprietary knowledge.

---

# Module 4 Generator Models

Three open-weight generators were evaluated:

### Gemma 4

* `google/gemma-4-12B-it-qat-w4a16-ct`
* QAT W4A16 / compressed-tensors
* local vLLM inference

### Qwen3.8 27B

* `Qwen/Qwen3.8-27B`
* official BF16 checkpoint
* runtime BitsAndBytes INT4
* local vLLM inference

### Qwen3.5 9B

* `Qwen/Qwen3.5-9B`
* runtime BitsAndBytes INT4
* local vLLM inference

Model revisions and runtime configurations were preserved in formal manifests.

---

# Module 4 Independent Evaluation

A separate **IBM Granite 4.2 8B** model was used as the independent semantic judge.

The judge did not receive:

* generator identity,
* route labels,
* prior pass/fail results,
* latency,
* token usage,
* or model ranking.

For each case, the judge received only:

* the question,
* final retrieved evidence context,
* and generated answer.

Six frozen evaluation dimensions were used:

1. Technical Correctness
2. Requirement Coverage
3. Evidence Grounding
4. Evidence–Answer Consistency
5. Technical Synthesis
6. Unsupported Claims Control

The weighted composite was calculated deterministically in Python rather than by the judge.

---

# Module 4 Evaluation Integrity

Planned independent evaluations:

**48**

Successfully validated judgments:

**47 / 48 — 97.92%**

The single unresolved case was:

```text
gemma4_12b::Q16
```

Granite completed generation normally, but one required negative-control field failed Boolean schema validation.

The result was therefore preserved as:

> **NOT EVALUATED — no imputation and no manual score substitution**

For fair cross-model comparison, the primary semantic comparison uses:

> **Q1–Q15 × 3 models = 45 directly comparable judgments**

---

# Module 4 Headline Results

## Independent Technical Quality — Q1 to Q15

| Generator       | Mean Quality |      Median | Minimum | Maximum |
| --------------- | -----------: | ----------: | ------: | ------: |
| **Gemma 4 12B** |   **92.50%** | **100.00%** |  68.75% | 100.00% |
| **Qwen3.8 27B** |   **85.08%** |      88.75% |  55.00% | 100.00% |
| **Qwen3.5 9B**  |   **72.92%** |      77.50% |  46.25% | 100.00% |

Gemma led every evaluated quality dimension.

---

## Generation Reliability

| Generator       | Formal Generation Validation |
| --------------- | ---------------------------: |
| **Gemma 4 12B** |                  **100.00%** |
| Qwen3.8 27B     |                       12.50% |
| Qwen3.5 9B      |                       31.25% |

The Qwen generators frequently reached the configured generation-token boundary.

Importantly, truncated answers often retained significant semantic value.

This reinforced a central Module 4 methodology:

> **Semantic quality and operational reliability must be evaluated separately.**

---

## Major Errors and Unsupported Claims

On the fair Q1–Q15 set:

| Generator       | Major Error Rate | Unsupported-Claim Cases |
| --------------- | ---------------: | ----------------------: |
| **Gemma 4 12B** |        **0.00%** |                  40.00% |
| Qwen3.8 27B     |            6.67% |                  66.67% |
| Qwen3.5 9B      |           20.00% |                  86.67% |

Retrieved evidence alone therefore does not eliminate unsupported technical extrapolation.

---

# Module 4 Natural Route Selection

The models naturally selected different architectures:

| Generator   | RAG Only | MCP Only | Hybrid |
| ----------- | -------: | -------: | -----: |
| Gemma 4 12B |        0 |        7 |      9 |
| Qwen3.8 27B |        2 |       10 |      4 |
| Qwen3.5 9B  |        0 |        9 |      7 |

This demonstrates that different models interpret the same knowledge-access problem differently.

---

# Module 4 Route-Alignment Finding

For the frozen stress questions:

| Generator   | Favoured-Route Alignment | Mean Stress Quality |
| ----------- | -----------------------: | ------------------: |
| Gemma 4 12B |                   57.14% |          **91.25%** |
| Qwen3.8 27B |               **85.71%** |              85.18% |
| Qwen3.5 9B  |                   71.43% |              81.43% |

The strongest route alignment did **not** produce the highest answer quality.

This demonstrates:

> **Selecting the nominally favoured retrieval architecture is not sufficient to guarantee the best answer.**

Routing, evidence quality, sufficiency assessment, evidence synthesis, and generator capability interact.

---

# Module 4 Hybrid Finding

All three generators selected Hybrid on the central Hybrid stress cases.

However, technical quality still varied substantially between generators.

Therefore:

> **Hybrid retrieval expands evidence access, but does not guarantee higher answer quality.**

Hybrid retrieval remains an evidence-access capability rather than a substitute for model capability.

---

# Module 4 Retrieval-Round Finding

For Gemma:

| Retrieval Rounds | Mean Quality |
| ---------------- | -----------: |
| 1                |      100.00% |
| 2                |       94.25% |
| 3                |       89.53% |

For Qwen3.8:

| Retrieval Rounds | Mean Quality |
| ---------------- | -----------: |
| 1                |       97.25% |
| 2                |       85.62% |
| 3                |       69.06% |

This does not demonstrate that additional retrieval causes poorer answers.

More difficult questions naturally tend to require more retrieval.

Instead:

> **Repeated retrieval and exhaustion of the maximum retrieval-round budget are useful signals of unresolved evidence requirements.**

This becomes particularly important for Module 5 agent investigation loops.

---

# Module 4 Negative Control

Q16 requested unsupported proprietary vendor information for a fictional alarm.

The correct behaviour was to avoid inventing:

* an exact vendor root cause,
* proprietary severity classifications,
* or vendor-prescribed remediation procedures.

Successfully judged results:

| Generator   |       Quality |              Correct Abstention |
| ----------- | ------------: | ------------------------------: |
| Qwen3.8 27B |        98.75% |                             Yes |
| Qwen3.5 9B  |       100.00% |                             Yes |
| Gemma 4 12B | Not Evaluated | Judge schema-validation failure |

No replacement Gemma score was inferred.

---

# Module 4 Technologies and Processes Achieved

Module 4 progressed the project from isolated retrieval systems into a reproducible **multi-retriever, multi-model telecom knowledge architecture**.

Key technologies and processes demonstrated include:

## Semantic Retrieval

* BGE-M3 embeddings
* FAISS
* telecom/cloud-native semantic retrieval
* controlled top-k evidence selection
* source metadata preservation

## Knowledge-Based MCP

* FastMCP
* persistent DuckDB knowledge base
* BM25 / full-text search
* structured telecom knowledge access
* source-aware retrieval

## Hybrid Retrieval

* `RAG_ONLY`
* `MCP_ONLY`
* `HYBRID`
* concurrent dual-retriever execution
* near-duplicate removal
* Reciprocal Rank Fusion
* evidence representation controls

## Adaptive Retrieval

* natural LLM route planning
* query generation
* answer-requirement generation
* up to three retrieval rounds
* evidence-sufficiency assessment
* bounded stopping behaviour

## Local LLM Infrastructure

* vLLM
* compressed Gemma inference
* BitsAndBytes INT4 runtime quantization
* BF16 computation
* controlled GPU allocation
* CPU/GPU embedding placement

## Independent Evaluation

* IBM Granite 4.2 8B
* blinded generator evaluation
* six-dimension semantic rubric
* judge qualification before formal execution
* deterministic composite scoring

## Experimental Reliability

* frozen benchmark
* exact model revisions
* SHA-256 fingerprints
* configuration hashes
* runtime manifests
* per-case checkpointing
* failure preservation
* schema validation
* no post-hoc answer repair

## Post-Hoc Analysis

* Python
* Pandas
* NumPy
* Matplotlib
* model-level scorecards
* route analysis
* quality–latency analysis
* retrieval-round analysis
* reliability analysis
* unsupported-claim analysis
* negative-control analysis

## Artifact Management

* portable experiment artifacts
* Google Drive archival
* Kaggle dataset versioning
* CPU-only recovery after GPU/runtime loss
* curated GitHub reproducibility artifacts

Module 4 therefore established the project's first complete:

> **knowledge-access → adaptive retrieval → evidence synthesis → generation → independent evaluation → reproducible analysis pipeline**

---

# Module 4 Final Conclusion

Module 4 demonstrates that **semantic RAG and Knowledge-Based MCP are complementary retrieval/access mechanisms**.

The experiment does not support applying Hybrid retrieval universally.

Instead, the strongest architectural direction is an **adaptive evidence-access system** capable of selecting RAG, MCP, or both according to the evidence needs of a problem.

System performance depends on four interacting capabilities:

1. **Retrieval selection**
   Choosing the appropriate knowledge mechanism.

2. **Evidence acquisition**
   Retrieving technically relevant material.

3. **Evidence sufficiency assessment**
   Determining when enough information has been collected.

4. **Grounded synthesis**
   Producing a technically correct answer without unsupported extrapolation.

Among the tested generators, Gemma 4 demonstrated the strongest overall combination of:

* technical quality,
* grounding,
* synthesis,
* unsupported-claim control,
* and generation reliability.

The central conclusion of Module 4 is:

> **RAG provides controlled semantic retrieval; MCP provides standardized access to a specialized knowledge service. They are complementary retrieval/access mechanisms. Their combined value is greatest when an intelligent orchestrator selects and sequences them according to the evidence needs of the problem rather than applying Hybrid retrieval universally.**

Detailed Module 4 results are available in:

```text
docs/module_4/RESULTS.md
```

Architecture and evaluation methodology are documented in:

```text
docs/module_4/ARCHITECTURE.md
docs/module_4/EVALUATION.md
```

---

# Module 5 — Agentic Telecom AI

Module 4 answered:

> **How should a telecom LLM access complementary knowledge sources?**

Module 5 extends the research question to:

> **Can an LLM-driven telecom agent autonomously select and sequence MCP-accessible knowledge, network-observation and controlled-action tools to diagnose realistic 5G network incidents accurately, efficiently and safely?**

The planned architecture moves from knowledge retrieval into tool-driven network investigation.

---

## Module 5 Target Architecture

```text
Incident / Engineering Task
           │
           ▼
      LangGraph Agent
           │
     ┌─────┼───────────────┐
     │     │               │
     ▼     ▼               ▼
Semantic  Knowledge     Telemetry
  RAG       MCP            MCP
     │       │               │
     └───────┴───────┬───────┘
                     │
                     ▼
             Evidence / State
                     │
                     ▼
              Agent Diagnosis
                     │
                Action needed?
                  /       \
                No         Yes
                │           │
                │           ▼
                │     Policy Engine
                │      /    |    \
                │   Allow Approval Deny
                │      │
                │      ▼
                │    Action MCP
                │      │
                │      ▼
                │   Verification
                │
                ▼
          Final Diagnosis
```

---

## Module 5 Planned Technologies

The planned stack includes:

* **LangGraph** — explicit agent state and workflow orchestration
* **LangSmith** — required trajectory observability
* **Model Context Protocol** — standardized knowledge, telemetry and action tools
* **Pydantic** — typed agent/tool schemas
* **OpenTelemetry** — framework-neutral observability
* **Prometheus / Grafana** — later network telemetry visualization
* **Granite 4.2 8B** — primary locally controlled agent model
* **synthetic standards-shaped 5G telemetry** — controlled V1 environment
* **open-source executable 5G environment** — later V2 validation

Module 5 will initially remain controlled and simulation-oriented.

Unrestricted production autonomy is intentionally outside its scope.

---

# Module 6 — Production Architecture + RAG V2

RAG V1 remains frozen as an experimental baseline.

Module 6 will use evidence accumulated across Modules 2–5 to investigate production-oriented improvements including:

* graded grounding,
* evidence-sufficiency classification,
* controlled engineering inference,
* multi-source evidence synthesis,
* task-aware routing,
* hybrid retrieval optimization,
* runtime stabilization,
* model-specific orchestration,
* observability,
* evaluation pipelines,
* production deployment architecture,
* and RAG V2.

---

# Module 7 — Autonomous Telecom Operations

The final stage will investigate how the preceding capabilities can be combined into increasingly autonomous operational workflows.

The long-term architecture is:

```text
                    Telecom AI System
                           │
               ┌───────────┴───────────┐
               │                       │
            Knowledge              Network State
               │                       │
        ┌──────┴──────┐          Observation MCP
        │             │                 │
       RAG       Knowledge MCP          │
        │             │                 │
        └─────────────┴────────┬────────┘
                               │
                               ▼
                        Agentic Reasoning
                               │
                               ▼
                        Policy / Safety
                               │
                               ▼
                        Controlled Action
                               │
                               ▼
                     Post-Action Verification
                               │
                               ▼
                  Autonomous Telecom Operations
```

Any progression toward autonomous actions should preserve:

* controlled permissions,
* observability,
* deterministic policy enforcement,
* validation,
* rollback mechanisms,
* human oversight where appropriate,
* and explicit safety boundaries.

---

# Development Methodology

The project follows an incremental experimental methodology.

Each architectural stage is evaluated before the next layer is introduced.

```text
Module 1
Standalone LLM
      ↓
Module 2
Telecom RAG V1
      ↓
Module 3
Knowledge-Based MCP
      ↓
Module 4
Adaptive RAG + MCP Hybrid
      ↓
Module 5
Agentic Telecom AI
      ↓
Module 6
Production Architecture + RAG V2
      ↓
Module 7
Autonomous Telecom Operations
```

This provides clear experimental baselines and reduces the risk of incorrectly attributing improvements or failures to the wrong architectural component.

Several principles are retained across modules:

* freeze benchmarks before formal evaluation,
* preserve failures rather than repair them post hoc,
* separate retrieval from generation quality,
* separate semantic quality from runtime reliability,
* preserve exact model revisions where possible,
* validate evaluation methodology before formal use,
* checkpoint expensive experiments,
* use independent evaluation where appropriate,
* avoid tuning against formal benchmark results,
* and retain portable experiment artifacts.

---

# Current Project Status

## Completed

### Module 1 — Standalone LLM

* standalone general-purpose vs telecom-domain LLM benchmark,
* 20-question custom telecom benchmark,
* 32-question industry benchmark,
* independent evaluation,
* expert technical review,
* cross-track analysis.

### Module 2 — Telecom RAG V1

* telecom RAG V1,
* BGE-M3 embeddings,
* FAISS retrieval,
* approximately 1.5 million indexed chunks,
* Essential AI standalone and RAG evaluation,
* OTel 2.0 standalone evaluation,
* Gemma 4 standalone and RAG evaluation,
* RAG versus standalone analysis,
* grounding diagnostics,
* RAG V1 failure analysis,
* RAG V2 design recommendations.

### Module 3 — Knowledge-Based MCP

* knowledge-based MCP architecture,
* Version A direct remote retrieval,
* Version B persistent BM25/FTS knowledge base,
* approximately 1.78 million records across 21 shards,
* deterministic source routing,
* unified provider-neutral MCP knowledge tool,
* Claude Sonnet evaluation,
* Claude Haiku evaluation,
* Gemma evaluation,
* DeepSeek evaluation,
* Qwen provider-availability exclusion record,
* frozen Benchmark v2,
* paired Version A/B analysis,
* cross-model evaluation,
* claim-level grounding evaluation,
* independent technical-quality evaluation,
* runtime and latency analysis,
* final integrated Module 3 scorecard.

### Module 4 — Adaptive RAG + Knowledge MCP Hybrid

* restoration and reuse of frozen RAG V1,
* restoration and reuse of Version B Knowledge MCP,
* natural RAG / MCP / Hybrid route selection,
* adaptive multi-round retrieval,
* evidence-sufficiency assessment,
* concurrent Hybrid retrieval,
* Reciprocal Rank Fusion,
* evidence deduplication,
* multi-model local vLLM execution,
* Gemma 4 12B formal evaluation,
* Qwen3.8 27B formal evaluation,
* Qwen3.5 9B formal evaluation,
* frozen 16-question benchmark,
* independent Granite 4.2 8B judge,
* judge qualification before formal evaluation,
* deterministic six-dimension scoring,
* 47 / 48 valid formal judge results,
* fair Q1–Q15 cross-model analysis,
* routing analysis,
* retrieval-depth analysis,
* generation-reliability analysis,
* unsupported-claims analysis,
* negative-control evaluation,
* fault-tolerant checkpointing,
* CPU-only post-hoc analysis,
* portable experiment archival,
* cleaned executed notebook,
* curated GitHub reproducibility package.

---

## Next

### Module 5 — Agentic Telecom AI

Planned work includes:

* knowledge tools exposed consistently through MCP,
* telemetry MCP,
* controlled action MCP,
* 5G KPI taxonomy,
* standards-shaped synthetic telemetry,
* deterministic fault injection,
* LangGraph agent state and orchestration,
* LangSmith trajectory observability,
* OpenTelemetry instrumentation,
* agent tool-use qualification,
* bounded investigation loops,
* deterministic action policy engine,
* human approval for service-affecting actions,
* trajectory-level evaluation,
* safety evaluation,
* Granite 4.2 8B primary agent,
* Granite 3B efficiency baseline,
* and later transfer testing against an executable open-source 5G environment.

---

## Later

* Production Architecture + RAG V2
* production-grade observability
* network-state integration
* improved retrieval architecture
* closed-loop workflows
* post-action validation
* increasingly autonomous telecom operations

---

# Key Project Lessons So Far

The first four modules have progressively reinforced several architectural lessons.

## 1. Domain specialization alone does not guarantee technical superiority

Module 1 demonstrated that a telecom-specialized model can still underperform a stronger general-purpose model.

## 2. Retrieval augmentation alone does not guarantee better answers

Module 2 showed that retrieved evidence may exist while restrictive prompting or weak evidence synthesis still reduces performance.

## 3. Standardized tool access does not standardize model behaviour

Module 3 showed that MCP can provide a common interface while different models still search, reformulate and consume evidence differently.

## 4. Hybrid retrieval is not universally superior

Module 4 showed that the ability to use both RAG and MCP is valuable, but blindly selecting both does not guarantee better technical quality.

## 5. Evidence sufficiency matters more than retrieval quantity

More retrieval is not automatically better.

A system must determine whether additional evidence materially reduces uncertainty.

## 6. Grounded reasoning remains a separate capability

Successful retrieval does not prevent an LLM from introducing unsupported claims.

## 7. Semantic quality and operational reliability must be measured independently

An answer can be technically valuable while still failing structural or generation-completion requirements.

## 8. Retrieval architecture and model capability are separate contributors

Strong retrieval cannot fully compensate for weak synthesis, and strong models cannot always compensate for insufficient evidence.

---

# Key Project Principle

The project has progressively reinforced a central engineering principle:

> **Reliable telecom AI requires more than a capable language model or the presence of retrieved context. It requires the correct combination of model capability, knowledge architecture, evidence retrieval, grounding, adaptive tool selection, runtime control, independent evaluation, safety constraints, and engineering validation.**

The architectural progression can therefore be summarized as:

```text
Model Capability
      +
Controlled Knowledge
      +
Adaptive Retrieval
      +
Standardized Tools
      +
Evidence Sufficiency
      +
Grounded Reasoning
      +
Agentic Orchestration
      +
Operational Safety
      ↓
Reliable Telecom AI
```

---

# Reproducibility and Artifact Policy

Formal experiments preserve, where applicable:

* frozen benchmark definitions,
* benchmark SHA-256 hashes,
* exact model IDs,
* exact model revisions,
* runtime manifests,
* retrieval configuration,
* evaluation rubrics,
* configuration hashes,
* checkpoints,
* failure records,
* result JSON,
* summary CSV files,
* deterministic post-hoc analyses.

GitHub contains curated reproducibility artifacts.

Large runtime logs, redundant checkpoints and complete experiment archives are retained separately to avoid turning the repository into a runtime dump.

---

# Disclaimer

This project is an independent technical experiment and is not affiliated with or endorsed by any telecom vendor, standards organization, dataset provider, cloud provider, or model provider.

Datasets, documentation, model outputs and examples used in the project should respect applicable licensing, copyright, confidentiality, security and data-protection requirements.

No Module 5 or later controlled-action architecture should be interpreted as authorization for unrestricted production network automation.
