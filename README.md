# Telecom LLM, RAG & MCP

An experimental telecom AI project exploring the progressive integration of **Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), Model Context Protocol (MCP), AI agents, and autonomous network operations**.

The project investigates how general-purpose and telecom-domain LLMs can be progressively combined with telecom knowledge, network tools, reasoning workflows, and automation to support increasingly capable telecom engineering and operational use cases.

---

## Project Objective

The objective of this project is to evaluate the evolution of telecom AI systems through a controlled sequence of architectural stages:

**Standalone LLM → RAG → Knowledge Extension + MCP → AI Agents → RAG V2 / Architecture Optimization → Autonomous Telecom Operations**

Each major stage is implemented, benchmarked, analyzed, and retained as a reference baseline before progressing to the next phase.

The focus is not only on benchmark performance, but also on:

* technical accuracy,
* engineering reasoning,
* factual reliability,
* knowledge grounding,
* operational reliability,
* tool integration,
* and practical applicability to telecom network operations.

---

## Project Roadmap

| Module                     | Description                                                                  | Status      |
| -------------------------- | ---------------------------------------------------------------------------- | ----------- |
| **001_llm_base**           | Initial general-purpose vs telecom-domain LLM benchmark                      | ✅ Completed |
| **002_rag_v1**             | Telecom RAG V1, expanded multi-model benchmark and failure analysis          | ✅ Completed |
| **003_mcp**                | Telecom knowledge-base extension and MCP integration with network data/tools | 🔄 Next     |
| **004_agents**             | AI agents for telecom reasoning and operational workflows                    | ⏳ Planned   |
| **005_rag_v2**             | RAG V2 / architecture optimization based on V1 and MCP findings              | ⏳ Planned   |
| **006_autonomous_telecom** | Integrated closed-loop and autonomous telecom operations                     | ⏳ Planned   |

---

# Module 1 — Initial LLM Baseline

Module 1 established the original telecom LLM benchmark and provided the experimental foundation for the subsequent RAG work.

The objective was to compare a general-purpose instruction-tuned LLM with a telecom-domain model derived from the same model lineage.

## Models Evaluated

* **General LLM:** `EssentialAI/rnj-1-instruct`
* **Telecom LLM / OTel 1.0:** `farbodtavakkoli/OTel-LLM-8.3B-IT`
* **Independent Judge:** `Qwen/Qwen2.5-7B-Instruct`

OTel 1.0 is derived from the `rnj-1-instruct` lineage and underwent telecom-specific post-training, providing a useful controlled comparison of the impact of domain specialization.

---

## Shared Benchmark Framework

Module 1 established two benchmark tracks which were subsequently retained in Module 2.

### Track 1 — Custom Telecom Engineering Benchmark

Track 1 contains **20 custom telecom engineering questions** covering conceptual, procedural, troubleshooting, design, and applied engineering scenarios.

Key areas include:

* 5G Core
* 5G RAN
* 5G Standalone procedures
* Open RAN
* cloud-native telecom
* Kubernetes
* capacity and performance
* troubleshooting
* fault isolation
* network architecture
* end-to-end engineering reasoning

### Track 2 — Industry Telecom Benchmark

Track 2 contains **32 industry-oriented telecom questions** covering:

* 3GPP working-group classification
* O-RAN
* 6G reasoning
* srsRAN
* telecom logs
* telecom mathematics
* telecom Q&A
* telecom tables

The same **20 Track 1 questions and 32 Track 2 questions** formed the benchmark foundation reused in Module 2.

This provides continuity between the initial standalone-model experiment and the later RAG V1 evaluation.

---

## Module 1 Evaluation Approach

Track 1 included:

* fixed model inference,
* an independent LLM judge,
* question-level scoring,
* and expert telecom engineering review.

The expert review considered:

* technical accuracy,
* completeness,
* relevance,
* engineering reasoning,
* practical applicability,
* factual reliability,
* technical errors,
* missing important points,
* and question-level winners.

Track 2 was assessed against the benchmark reference answers and expert technical review.

---

## Module 1 — Track 1 Results

| System                         | Questions Won | Win Rate | Average Expert Score |
| ------------------------------ | ------------: | -------: | -------------------: |
| **EssentialAI/rnj-1-instruct** |   **13 / 20** |  **65%** |       **72.8 / 100** |
| OTel 1.0                       |        7 / 20 |      35% |           60.1 / 100 |

The General LLM showed particular strength in:

* troubleshooting,
* cloud-native telecom,
* Kubernetes,
* complex architecture,
* and broader engineering reasoning.

OTel 1.0 performed competitively on selected:

* 5G Core,
* RAN,
* Open RAN,
* and focused DL/UL engineering questions.

A notable difference in model behaviour was observed:

* the General LLM provided broader engineering reasoning but could produce confident telecom-specific inaccuracies;
* OTel 1.0 was generally more concise and focused but showed greater capability gaps on complex open-ended tasks.

---

## Module 1 — Track 2 Results

| System                         | Questions Won |  Win Rate | Average Expert Score |
| ------------------------------ | ------------: | --------: | -------------------: |
| **EssentialAI/rnj-1-instruct** |   **23 / 32** | **71.9%** |       **70.1 / 100** |
| OTel 1.0                       |        7 / 32 |     21.9% |           32.1 / 100 |
| Ties                           |        2 / 32 |      6.3% |                    — |

The General LLM demonstrated broader capability across:

* 3GPP classification,
* software/code-oriented questions,
* quantitative reasoning,
* and telecom troubleshooting.

OTel 1.0 performed well on selected focused O-RAN, 6G, and telecom-table questions, but produced more non-responsive outputs on detailed source-dependent and analytical tasks.

---

## Module 1 — Cross-Track Outcome

Across the combined **52 benchmark questions**:

| Metric                        | EssentialAI/rnj-1-instruct |        OTel 1.0 |
| ----------------------------- | -------------------------: | --------------: |
| Combined Questions Won        |        **36 / 52 (69.2%)** | 14 / 52 (26.9%) |
| Combined Average Expert Score |             **71.1 / 100** |      42.8 / 100 |
| Overall Result                |                 **Winner** |               — |

The principal Module 1 conclusion was:

> **Technical fluency and concise responses do not guarantee technical correctness.**

The experiment also showed that telecom-domain specialization alone does not automatically guarantee stronger engineering performance.

Module 1 therefore established both the initial standalone baseline and the benchmark methodology used for subsequent experimentation.

---

# Module 2 — Telecom RAG V1 and Expanded Multi-Model Benchmark

Module 2 reused the established **Track 1 and Track 2 benchmark framework** and expanded the experiment from two systems to five configurations.

## Systems Evaluated

1. **Essential AI + RAG**
2. **Essential AI Only**
3. **Otel 2.0 Only**
4. **Gemma 4 Only**
5. **Gemma 4 + RAG**

This phase introduced:

* a large telecom knowledge corpus,
* semantic embeddings,
* FAISS vector retrieval,
* RAG generation,
* newer standalone models,
* expanded independent evaluation,
* objective Track 2 scoring,
* and detailed RAG failure diagnosis.

---

## RAG V1 Knowledge Architecture

The telecom corpus combines documentation from sources including:

* 3GPP
* ETSI
* ITU-T
* GSMA
* O-RAN
* TM Forum
* CAMARA
* telecom common-corpus material

The RAG V1 retriever uses:

* **Embedding model:** `BAAI/bge-m3`
* **Vector store:** FAISS
* **Embedding dimension:** 1024
* **Indexed vectors:** approximately 1.5 million
* **Production retrieval:** Top-7 chunks

The V1 design intentionally emphasized strict grounding in retrieved documentation.

---

# Module 2 Evaluation

The benchmark question foundation remained unchanged from Module 1:

* **Track 1:** 20 telecom engineering questions
* **Track 2:** 32 industry telecom questions

This continuity allows comparison across successive architecture generations.

Module 2 introduced a revised evaluation methodology appropriate to the expanded experiment.

---

## Track 1 — Independent Engineering Judge

Track 1 responses were evaluated using an independent judge across:

1. Technical Accuracy
2. Completeness
3. Relevance
4. Engineering Reasoning
5. Practical Applicability
6. Factual Reliability
7. Overall Score

### Track 1 Overall Results

| Rank | System             |    Mean Score |
| ---- | ------------------ | ------------: |
| 1    | **Otel 2.0 Only**  | **9.20 / 10** |
| 2    | **Gemma 4 Only**   | **9.00 / 10** |
| 3    | Gemma 4 + RAG      |     6.75 / 10 |
| 4    | Essential AI Only  |     5.80 / 10 |
| 5    | Essential AI + RAG |     5.65 / 10 |

### Question-Level Wins

Because ties were allowed:

| System             | Question Wins |
| ------------------ | ------------: |
| Otel 2.0 Only      |        **17** |
| Gemma 4 Only       |        **14** |
| Gemma 4 + RAG      |             3 |
| Essential AI + RAG |             1 |
| Essential AI Only  |             0 |

The strongest Track 1 responses were therefore produced by the standalone Otel 2.0 and Gemma 4 systems.

---

## Track 2 — Objective Expected-Answer Evaluation

Track 2 contains authoritative expected answers and was therefore scored using deterministic answer correctness rather than an LLM judge.

The 32 questions cover eight benchmark families:

* `3gpp_tsg`
* `oranbench`
* `sixg_bench`
* `srsranbench`
* `telelogs`
* `telemath`
* `teleqna`
* `teletables`

### Track 2 Overall Results

| Rank | System                |     Correct |   Accuracy |
| ---- | --------------------- | ----------: | ---------: |
| 1    | **Otel 2.0 Only**     | **18 / 32** | **56.25%** |
| 2    | **Essential AI Only** | **13 / 32** | **40.62%** |
| 3    | Essential AI + RAG    |      8 / 32 |     25.00% |
| 3    | Gemma 4 + RAG         |      8 / 32 |     25.00% |
| 3    | Gemma 4 Only          |      8 / 32 |     25.00% |

Otel 2.0 demonstrated the strongest objective benchmark performance.

---

# RAG V1 Findings

Module 2 demonstrated that retrieval augmentation is **not automatically beneficial simply because additional telecom context is provided to a model**.

The effect of RAG depended strongly on:

* model capability,
* question type,
* retrieved evidence,
* grounding policy,
* generation behaviour,
* and runtime reliability.

---

## Essential AI RAG Impact

### Track 1

* Essential AI Only: **5.80**
* Essential AI + RAG: **5.65**
* Mean delta: **-0.15**

Question-level movement:

* RAG better: **9**
* Same: **4**
* RAG worse: **7**

The relatively small average difference concealed substantial question-level movement.

### Track 2

* Essential AI Only: **40.62%**
* Essential AI + RAG: **25.00%**
* Delta: **-15.62 percentage points**

Essential AI + RAG also experienced **9 generation failures out of 32 questions**.

Conditional accuracy among successfully generated responses was **34.78%**, still below the standalone model's **40.62%**.

Runtime instability therefore explains part, but not all, of the observed degradation.

---

## Gemma 4 RAG Impact

### Track 1

* Gemma 4 Only: **9.00**
* Gemma 4 + RAG: **6.75**
* Mean delta: **-2.25**

Question-level movement:

* RAG better: **0**
* Same: **6**
* RAG worse: **14**

This provided the clearest evidence of the current RAG implementation interfering with an already strong standalone model.

### Track 2

* Gemma 4 Only: **25.00%**
* Gemma 4 + RAG: **25.00%**

However:

* RAG better: **7**
* Same: **18**
* RAG worse: **7**

Identical overall accuracy therefore concealed substantial question-level changes.

---

# RAG V1 Failure Diagnosis

A targeted diagnostic was performed on **13 priority Track 1 RAG degradation cases**.

Among those cases:

* **13 / 13** were classified primarily as `STRICT_GROUNDING_ABSTENTION`
* **11 / 13** contained `PARTIAL` retrieved evidence
* **2 / 13** contained `SUFFICIENT` retrieved evidence
* **0 / 13** were classified primarily as retrieval failures
* **13 / 13** were classified as generation or prompting failures

This finding applies specifically to the investigated degradation cases and should not be generalized to every RAG response.

It indicates that in these priority cases, useful retrieved information generally existed, but the generator did not exploit it effectively.

---

# Grounding Insight

RAG V1 intentionally prioritized responses grounded in controlled telecom documentation.

This remains an important design principle.

However, the evaluation showed that strict binary grounding can become overly restrictive when:

* evidence is partial,
* evidence is distributed across several chunks,
* questions require engineering synthesis,
* or the standalone model possesses useful domain knowledge.

The desired future architecture is therefore:

> **Evidence-first grounded engineering reasoning rather than strict document extraction.**

---

# Task-Dependent RAG Behaviour

The benchmark also demonstrated that different telecom tasks require different AI strategies.

RAG is naturally suited to:

* standards lookup,
* specification lookup,
* document-grounded technical questions.

Broader engineering tasks may require:

* retrieved knowledge,
* engineering reasoning,
* multi-domain synthesis,
* and external tools.

Numerical and structured tasks may benefit from:

* Python,
* calculators,
* structured-data processing,
* and specialized analytical tools.

This motivates a future **task-aware routing architecture**.

---

# RAG V2 / Architecture Optimization Roadmap

RAG V1 is now treated as a **frozen experimental baseline**.

A future RAG V2 or broader architecture-optimization phase will investigate improvements including:

* graded grounding,
* explicit evidence-sufficiency classification,
* controlled engineering inference,
* improved multi-chunk evidence synthesis,
* task-aware routing,
* runtime stabilization,
* and selective use of external tools.

The relationship between RAG and MCP may also evolve during subsequent development.

Possible future directions include:

* retaining RAG as an independent retrieval layer,
* integrating retrieval functions with MCP,
* exposing selected knowledge-retrieval capabilities as tools,
* or migrating parts of the current RAG workflow into a broader tool-based architecture.

No final migration approach is assumed at this stage.

---

# Module 3 — Knowledge-Base Extension and MCP

The immediate next phase expands the project in two complementary directions:

1. **Extend the telecom knowledge base**
2. **Introduce Model Context Protocol integration**

---

## Telecom Knowledge-Base Extension

A confirmed objective of Module 3 is to extend the existing telecom corpus with important knowledge sources that were not included during RAG V1.

The current corpus already contains material from:

* 3GPP
* ETSI
* ITU-T
* GSMA
* O-RAN
* TM Forum
* CAMARA
* telecom common-corpus material

Module 3 will review corpus coverage, identify important gaps, and progressively add missing telecom knowledge.

The extension will focus on improving:

* standards coverage,
* technology coverage,
* implementation knowledge,
* operational documentation,
* troubleshooting knowledge,
* and support for future network-engineering workflows.

Knowledge-base extension will initially be treated separately from RAG V2 optimization so that corpus improvements and architecture changes can be evaluated independently where practical.

---

## Model Context Protocol Integration

Module 3 will also investigate how LLMs can interact with controlled telecom data and operational capabilities through MCP.

Potential MCP-accessible capabilities include:

* network KPI retrieval
* PM-counter queries
* alarm inspection
* network topology lookup
* configuration retrieval
* simulated OSS functions
* diagnostic tools
* network health checks
* structured network-data queries
* controlled operational actions

The objective is to evolve from:

> **AI that primarily answers telecom questions**

towards:

> **AI that can combine telecom knowledge with network state, invoke controlled tools, interpret results, and support telecom operational workflows.**

---

## Module 3 Architecture Evolution

The relationship between the expanded knowledge base, RAG, and MCP will be evaluated progressively.

The initial priorities are:

1. identify missing telecom knowledge,
2. extend the knowledge base,
3. establish MCP connectivity,
4. expose controlled telecom tools and data sources,
5. evaluate the resulting architecture,
6. and then determine whether changes to the RAG integration are justified.

This avoids committing prematurely to a specific RAG-to-MCP migration pattern.

---

# Future Agent Layer

Following MCP integration, an agent layer can coordinate combinations of:

* LLM reasoning,
* RAG retrieval,
* MCP tools,
* diagnostic functions,
* network state,
* and workflow logic.

Potential workflows include:

* fault isolation,
* congestion analysis,
* configuration validation,
* KPI anomaly investigation,
* root-cause analysis,
* recommendation generation,
* action execution,
* and post-action verification.

---

# Target Architecture

```text
                         Telecom AI System
                                |
                +---------------+---------------+
                |                               |
               RAG                             MCP
                |                               |
       Telecom Knowledge                Network / OSS Tools
                |                               |
                +---------------+---------------+
                                |
                          AI Reasoning
                                |
                           Agent Layer
                                |
                      Operational Workflow
                                |
                       Simulated Network
                                |
                        AI Network Ops
                                |
                    Autonomous Operations
```

---

# Repository Structure

```text
.
├── notebooks/
│   ├── 01_llm_base.ipynb
│   ├── 02_rag_stage_1.ipynb
│   ├── 03_essentialai_rag_v1.ipynb
│   ├── 04_essentialai_only.ipynb
│   ├── 05_otel2_only.ipynb
│   ├── 06_gemma4_only.ipynb
│   ├── 07_gemma4_rag_v1.ipynb
│   └── 08_rag_evaluation.ipynb
│
├── results/
│   ├── 001_llm_base/
│   └── 002_rag_v1/
│
├── src/
│
├── README.md
└── .gitignore
```

---

# Development Methodology

The project follows an incremental experimental approach.

Each architecture phase is:

1. implemented,
2. benchmarked,
3. evaluated,
4. diagnostically analyzed,
5. retained as a baseline,
6. and extended in a subsequent phase.

Current development sequence:

```text
Standalone LLM Baseline
        |
        v
      RAG V1
        |
        v
Knowledge Extension + MCP
        |
        v
    AI Agents
        |
        v
RAG V2 / Architecture Optimization
        |
        v
Integrated Telecom AI
        |
        v
Autonomous Telecom Operations
```

This approach allows each capability to be assessed independently before multiple architectural layers are combined.

---

# Current Project Status

## Completed

* Initial general-purpose vs telecom-domain LLM baseline
* 20-question Track 1 benchmark
* 32-question Track 2 benchmark
* expert baseline assessment
* telecom corpus preparation
* RAG V1 implementation
* BGE-M3 / FAISS retrieval
* Essential AI standalone evaluation
* Essential AI + RAG evaluation
* Otel 2.0 standalone evaluation
* Gemma 4 standalone evaluation
* Gemma 4 + RAG evaluation
* independent Track 1 judge evaluation
* objective Track 2 scoring
* RAG vs standalone analysis
* RAG grounding diagnostics
* consolidated cross-track analysis
* RAG V2 design recommendations

## Next

* identify and add missing telecom knowledge sources
* extend the telecom knowledge base
* implement MCP connectivity
* expose telecom/network data and operational tools through MCP

## Later

* AI agent workflows
* evaluate RAG/MCP architecture evolution
* RAG V2 controlled optimization
* integrated telecom operational workflows
* closed-loop network actions
* autonomous telecom operations

---

## Key Project Principle

The project has progressively reinforced a central lesson:

> **Telecom AI performance depends on more than model fluency or the presence of retrieved context. Reliability requires the correct combination of domain capability, factual grounding, reasoning, task selection, tool use, and engineering validation.**

---

## Disclaimer

This project is an independent technical experiment and is not affiliated with or endorsed by any telecom vendor, standards organization, or model provider.

Datasets, documentation, model outputs, and examples used in the project should respect applicable licensing, copyright, confidentiality, and data-protection requirements.
