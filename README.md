# Telecom LLM, RAG & MCP

An experimental telecom AI engineering project exploring the progressive integration of **Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), Model Context Protocol (MCP), AI agents, production AI architecture, and autonomous network operations**.

The project investigates how general-purpose and telecom-domain LLMs can be progressively combined with controlled telecom knowledge, retrieval systems, standardized tool interfaces, reasoning workflows, and network automation to support increasingly capable telecom engineering use cases.

---

# Project Objective

The objective is to evaluate the evolution of telecom AI systems through a controlled sequence of architectural stages:

```text
Standalone LLM
      ↓
RAG
      ↓
Knowledge-Based MCP
      ↓
RAG + MCP Hybrid
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
3. evaluated,
4. diagnostically analyzed,
5. retained as a frozen or controlled baseline,
6. and then extended in the next architectural stage.

The project focuses not only on benchmark performance, but also on:

* technical accuracy,
* engineering reasoning,
* factual reliability,
* evidence grounding,
* retrieval quality,
* tool-use behaviour,
* runtime reliability,
* latency,
* token efficiency,
* architecture design,
* and practical applicability to telecom engineering and operations.

---

# Project Roadmap

| Module       | Architecture                                    | Status      |
| ------------ | ----------------------------------------------- | ----------- |
| **Module 1** | Standalone LLM baseline                         | ✅ Completed |
| **Module 2** | Telecom RAG V1 + expanded multi-model benchmark | ✅ Completed |
| **Module 3** | Knowledge-Based MCP + cross-LLM evaluation      | ✅ Completed |
| **Module 4** | RAG + Knowledge-Based MCP Hybrid                | 🔄 Next     |
| **Module 5** | Agentic Telecom AI                              | ⏳ Planned   |
| **Module 6** | Production Architecture + RAG V2                | ⏳ Planned   |
| **Module 7** | Autonomous Telecom Operations                   | ⏳ Planned   |

---

# Repository Organization

The repository is organized by architecture module so that each stage remains clearly identifiable as the project grows.

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
│   └── module_3/
│       ├── 09_version_a_claude_sonnet.ipynb
│       ├── 10_version_a_claude_haiku.ipynb
│       ├── 11_version_a_gemma4.ipynb
│       ├── 12_version_a_deepseek_v4.ipynb
│       ├── 13_qwen3_8_exclusion_record.ipynb
│       ├── 14_version_b_build.ipynb
│       ├── 15_version_b_claude_sonnet_runtime.ipynb
│       ├── 16_version_b_claude_haiku_runtime.ipynb
│       ├── 17_version_b_gemma4_runtime.ipynb
│       ├── 18_version_b_deepseek_v4_runtime.ipynb
│       └── 19_module3_final_ab_cross_llm_analysis.ipynb
│
├── results/
│   ├── module_1/
│   ├── module_2/
│   └── module_3/
│       ├── frozen_benchmark/
│       └── final_analysis/
│
├── docs/
│   └── module_3/
│
├── scripts/
│   └── module_3/
│       └── validate_module3_notebooks.py
│
├── src/
│   └── llm/
│
├── README.md
└── .gitignore
```

Module-specific `docs/` and `scripts/` directories are added only where actual supporting material exists rather than creating empty folders for symmetry.

---

# Module 1 — Standalone LLM Baseline

Module 1 established the initial telecom LLM benchmark and provided the experimental foundation for the later RAG and MCP work.

## Models Evaluated

* **General LLM:** `EssentialAI/rnj-1-instruct`
* **Telecom LLM / OTel 1.0:** `farbodtavakkoli/OTel-LLM-8.3B-IT`
* **Independent Judge:** `Qwen/Qwen2.5-7B-Instruct`

OTel 1.0 is derived from the `rnj-1-instruct` lineage and underwent telecom-specific post-training, providing a useful controlled comparison of general-purpose versus domain-specialized model behaviour.

## Benchmark Framework

Two benchmark tracks were established.

### Track 1 — Custom Telecom Engineering Benchmark

**20 questions** covering areas including:

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

Module 1 established the standalone baseline and benchmark methodology carried into Module 2.

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
* **Baseline production retrieval:** Top-7 chunks

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

The strongest Track 1 responses were produced by the standalone OTel 2.0 and Gemma 4 systems.

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

This result applies specifically to the investigated degradation cases.

It showed that useful evidence often existed, but the generation layer did not exploit it effectively.

### Module 2 Conclusion

The desired future behaviour became:

> **Evidence-first grounded engineering reasoning rather than strict document extraction.**

RAG V1 is retained as a frozen experimental baseline.

---

# Module 3 — Knowledge-Based MCP + Cross-LLM Evaluation

Module 3 introduced **Model Context Protocol (MCP)** as a standardized interface through which heterogeneous LLMs access telecom knowledge.

Importantly, Module 3 remains a **knowledge-based MCP implementation**.

It does **not yet expose live network KPI retrieval, OSS actions, configuration changes, alarm handling, or operational control functions**.

Those capabilities are intentionally deferred to later agentic and operational modules.

---

# Why MCP Was Introduced

Module 2 showed that embedding-based RAG alone does not solve every telecom knowledge or reasoning problem.

Module 3 therefore investigated whether telecom knowledge retrieval could be exposed through a **provider-neutral tool interface** that different LLMs could consume without embedding retrieval logic directly into the model-specific application.

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

A deterministic router selects:

```text
3GPP Query
    ↓
Dedicated 3GPP Retrieval

TCC / Non-3GPP Query
    ↓
Telecom Common Corpus Retrieval

Mixed Query
    ↓
Hybrid Retrieval
```

Version A established that a common MCP interface could successfully support multiple LLMs.

---

# Module 3 — Version B

## Persistent Knowledge-Base Retrieval

Version B replaces repeated remote query-time retrieval with a persistent normalized and deduplicated telecom knowledge base.

The persistent architecture contains:

* normalized telecom records,
* hash-based deduplication,
* telecom-aware tokenization,
* DuckDB BM25/FTS indexing,
* dedicated 3GPP source-family shards,
* Telecom Common Corpus collection shards,
* and persistent reusable retrieval artifacts.

Version B contains approximately:

* **1.78 million indexed records**
* across **21 persistent search shards**

Both Version A and Version B expose the same public MCP knowledge-search interface.

The principal experimental variable is therefore the retrieval architecture rather than the LLM-facing MCP API.

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

# Cross-LLM Evaluation

The same MCP knowledge service was evaluated largely **out of the box** across:

* **Claude Sonnet 5**
* **Claude Haiku 4.5**
* **Gemma 4 26B A4B IT**
* **DeepSeek V4 Flash 0731**

Qwen3.8 Flash was excluded from the scored comparison because repeated execution was blocked by upstream provider rate limiting through OpenRouter's shared Alibaba capacity.

The exclusion represents an external availability constraint rather than model or MCP failure.

---

# Out-of-the-Box Evaluation Principle

A critical design choice in Module 3 was to evaluate each participating LLM largely **out of the box under common constraints**.

The experiments preserved:

* the same frozen benchmark,
* the same system prompt,
* the same MCP interface,
* the same routing semantics,
* the same retrieval domains,
* the same search budget,
* and common orchestration limits.

No post-hoc model-specific tuning was performed after observing benchmark behaviour.

Therefore, Module 3 answers:

> **How do different LLMs naturally behave when connected to the same telecom MCP knowledge service?**

It does **not** claim to measure the maximum performance achievable after individually optimizing each model.

---

# Module 3 Evaluation Framework

Execution success, retrieval success, answer quality, and evidence grounding were deliberately evaluated as separate dimensions.

The evaluation covered:

* completion / CHECK / error behaviour,
* MCP search frequency,
* query reformulation,
* route adherence,
* source-family accuracy,
* expected-element retrieval coverage,
* evidence authority,
* answer completeness,
* technical correctness,
* relevance,
* engineering quality,
* claim-level grounding,
* retrieval latency,
* non-retrieval latency,
* total end-to-end latency,
* and token usage.

---

# LLM-as-a-Judge Evaluation

An independent **GPT-5.6 Sol Pro** judge was used for two separate evaluation passes.

## Technical Quality

Each of the 64 responses was scored for:

* technical correctness,
* completeness,
* relevance,
* engineering quality.

## Evidence Grounding

Material claims were separately classified as:

* Supported,
* Partially Supported,
* Unsupported,
* Contradicted.

This produced:

* **64 technical-quality assessments**
* **64 grounding assessments**
* **844 material claims**

Technical quality and grounding were intentionally kept separate.

---

# Module 3 Key Findings

## 1. MCP Successfully Standardized Knowledge Access

All scored models successfully interacted with the same provider-neutral MCP knowledge tool.

Formal route accuracy reached **100% across the completed experiments**.

However, subsequent search behaviour still differed by model.

---

## 2. Model-Agnostic MCP Did Not Produce Model-Agnostic Behaviour

Different models showed materially different tool-use patterns despite using the same interface.

### Claude Sonnet 5

* strongest overall technical-quality performance,
* high answer completeness,
* moderate iterative search behaviour.

### Gemma 4

* strongest runtime efficiency,
* exactly **one MCP search per benchmark question**,
* highest relevance scores,
* strongest preservation of discriminative query terms such as the IEEE/research qualifier in Q7.

### Claude Haiku 4.5

* stronger iterative-search tendency,
* higher search and token consumption in Version B.

### DeepSeek V4 Flash 0731

* improved execution reliability and structural behaviour under Version B,
* but significant model/provider-side latency.

---

## 3. Retrieval Architecture Did Not Uniformly Determine Answer Quality

Version B improved important structural properties including:

* persistent indexing,
* source-family consistency,
* strict routing for some models,
* execution reliability,
* and reduced dependence on query-time remote availability.

However, those improvements did not automatically improve every downstream answer metric.

This demonstrates that:

> **Better retrieval infrastructure does not guarantee better final answers unless the model retrieves and uses sufficiently complete evidence.**

---

## 4. Search-Query Generation Is a Model Capability

The AI/ML traffic-prediction question provided a useful controlled example.

Only Gemma preserved enough of the **IEEE/research** selector to retrieve from both:

* IEEE-Access,
* OpenAlex.

Other models generalized the generated tool query and retrieved broader sources instead.

The effectiveness of MCP retrieval therefore depends partly on the LLM's ability to formulate discriminative tool queries.

---

## 5. Technical Quality and Grounding Are Different Dimensions

Claude Sonnet produced the highest overall judged technical quality.

Grounding leadership varied by architecture and model.

Gemma Version B produced highly relevant and technically capable answers while exhibiting substantially weaker claim-level evidence support.

This demonstrates that:

```text
Technical correctness
        ≠
Completeness
        ≠
Relevance
        ≠
Evidence grounding
```

Each should be measured independently.

---

## 6. Runtime Performance Is Strongly Model/Provider Dependent

DeepSeek Version B provides the strongest example.

Only approximately **4.26%** of its mean end-to-end latency was attributable to retrieval.

Approximately **95.74%** occurred outside the retrieval path.

Therefore:

> **Slow LLM+MCP execution should not automatically be diagnosed as slow retrieval.**

Retrieval latency and model/provider execution latency must be measured separately.

---

## 7. There Is No Single Best Model

Module 3 intentionally does not calculate a universal composite winner.

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

The out-of-the-box evaluation demonstrates that different LLMs require different runtime and orchestration settings to achieve the desired balance of:

* technical quality,
* grounding,
* latency,
* search discipline,
* token consumption,
* and operational cost.

Module 3 therefore establishes both the value and limitation of knowledge-based MCP:

> **MCP standardizes knowledge access, but does not by itself optimize how individual LLMs search for, interpret, and use that knowledge.**

---

# Module 4 — RAG + Knowledge-Based MCP Hybrid

Module 4 will combine two complementary knowledge mechanisms.

```text
                     User Query
                         │
                         ▼
                 LLM / Orchestrator
                         │
              ┌──────────┴──────────┐
              │                     │
              ▼                     ▼
             RAG                   MCP
              │                     │
   Semantic retrieval       Standardized knowledge
   Controlled corpus        service / tool access
              │                     │
              └──────────┬──────────┘
                         │
                         ▼
                  Evidence Synthesis
                         │
                         ▼
                    LLM Response
```

The objective is not to replace MCP with RAG or RAG with MCP.

Instead:

> **RAG provides controlled semantic retrieval while MCP provides standardized access to specialized knowledge services.**

Module 4 will investigate:

* RAG-only routing,
* MCP-only routing,
* hybrid RAG+MCP retrieval,
* evidence fusion,
* provenance preservation,
* retrieval conflict handling,
* query-specific routing,
* grounding improvement,
* and latency/token trade-offs.

---

# Module 5 — Agentic Telecom AI

Once the hybrid knowledge architecture is established, an agent layer can coordinate:

* LLM reasoning,
* RAG retrieval,
* MCP knowledge services,
* diagnostic tools,
* workflow state,
* and controlled telecom functions.

Potential workflows include:

* fault isolation,
* congestion analysis,
* configuration validation,
* KPI anomaly investigation,
* root-cause analysis,
* recommendation generation,
* and multi-step troubleshooting.

This is the stage where MCP may progressively expand beyond knowledge retrieval into controlled operational tooling.

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
                  ┌─────────────┴─────────────┐
                  │                           │
                 RAG                    MCP Services
                  │                           │
          Semantic Knowledge          Knowledge + Tools
                  │                           │
                  └─────────────┬─────────────┘
                                │
                                ▼
                        Agentic Reasoning
                                │
                                ▼
                       Operational Workflow
                                │
                                ▼
                      Network State / Tools
                                │
                                ▼
                     Controlled Action Layer
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
* validation,
* rollback mechanisms,
* human oversight where appropriate,
* and explicit safety boundaries.

---

# Development Methodology

The project follows an incremental experimental methodology.

Each architecture is evaluated before the next architectural layer is introduced.

```text
Module 1
Standalone LLM
      ↓
Module 2
RAG V1
      ↓
Module 3
Knowledge-Based MCP
      ↓
Module 4
RAG + MCP Hybrid
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

This provides clear experimental baselines and reduces the risk of attributing improvements or failures to the wrong architectural component.

---

# Current Project Status

## Completed

### Module 1

* standalone general-purpose vs telecom-domain LLM benchmark,
* 20-question custom telecom benchmark,
* 32-question industry benchmark,
* independent evaluation,
* expert technical review,
* cross-track analysis.

### Module 2

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

### Module 3

* knowledge-based MCP architecture,
* Version A direct remote retrieval,
* Version B persistent BM25/FTS knowledge base,
* deterministic 3GPP/TCC/Hybrid routing,
* unified provider-neutral MCP knowledge tool,
* Claude Sonnet evaluation,
* Claude Haiku evaluation,
* Gemma 4 evaluation,
* DeepSeek evaluation,
* Qwen provider-availability exclusion record,
* frozen Benchmark v2,
* paired Version A/B analysis,
* cross-model evaluation,
* claim-level evidence grounding,
* technical-quality LLM-as-a-Judge evaluation,
* runtime and latency analysis,
* final integrated Module 3 scorecard.

---

## Next

### Module 4 — RAG + Knowledge-Based MCP Hybrid

* define RAG-only / MCP-only / Hybrid routing,
* integrate semantic RAG retrieval with MCP knowledge access,
* preserve evidence provenance,
* evaluate evidence fusion,
* measure quality/grounding improvements,
* evaluate latency and token trade-offs.

---

## Later

* Agentic Telecom AI,
* controlled telecom operational tools,
* RAG V2,
* production architecture,
* network-state integration,
* closed-loop workflows,
* post-action validation,
* autonomous telecom operations.

---

# Key Project Principle

The project has progressively reinforced a central lesson:

> **Telecom AI performance depends on more than model fluency or the presence of retrieved context. Reliable engineering systems require the correct combination of domain capability, retrieval quality, factual grounding, reasoning, task selection, tool use, runtime control, and engineering validation.**

---

# Disclaimer

This project is an independent technical experiment and is not affiliated with or endorsed by any telecom vendor, standards organization, dataset provider, or model provider.

Datasets, documentation, model outputs, and examples used in the project should respect applicable licensing, copyright, confidentiality, and data-protection requirements.
