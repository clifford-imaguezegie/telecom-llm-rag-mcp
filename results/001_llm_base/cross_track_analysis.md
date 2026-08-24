# Cross-Track Analysis — Module 1 Baseline

## Cross-Track Performance Overview

The two benchmark tracks provide complementary views of General LLM
and OTel 1.0 performance:

- **Track 1:** Custom Telecom Benchmark — 20 telecom-focused
  conceptual, procedural and engineering questions.
- **Track 2:** Industry / GSMA Open-Telco Benchmark — 32 questions
  covering 3GPP classification, O-RAN, 6G reasoning, srsRAN,
  telecom mathematics, standards Q&A and drive-test analysis.

Both tracks ultimately use **expert technical review as the final
evaluation authority**.

Track 1 also included an Independent LLM Judge as a supplementary
evaluation layer. Track 2 was evaluated directly against benchmark
reference answers and expected criteria and did not use an Independent
LLM Judge.

## Overall Cross-Track Result

| Metric | General LLM | OTel 1.0 |
|---|---:|---:|
| Track 1 Questions Won | **13 / 20 (65%)** | 7 / 20 (35%) |
| Track 1 Average Expert Score | **72.8 / 100** | 60.1 / 100 |
| Track 2 Questions Won | **23 / 32 (71.9%)** | 7 / 32 (21.9%) |
| Track 2 Ties | 2 | 2 |
| Track 2 Average Expert Score | **70.1 / 100** | 32.1 / 100 |
| **Overall Winner** | **GENERAL LLM** | |

The expert assessment therefore identifies the **General LLM as the
stronger overall baseline model across both tracks**.

## Performance by Question Type

### General LLM — Strengths

The General LLM demonstrates its strongest performance in:

- Cloud-native telecom and Kubernetes.
- Applied troubleshooting and fault isolation.
- Complex network architecture and engineering design.
- 3GPP working-group classification.
- Software/code-oriented benchmark questions.
- Broad telecom reasoning across multiple technical domains.

### OTel 1.0 — Strengths

OTel 1.0 performs comparatively well on:

- Selected 5G Core and RAN fundamentals.
- Focused Open RAN questions.
- Selected 6G decision-making scenarios.
- Narrow multiple-choice technical questions.
- Selected standards and TELETABLES questions.

OTel 1.0 is generally more concise and targeted when it has enough
context to answer the question.

## Conceptual vs Applied Engineering

The **OTel 1.0** responses are competitive on focused conceptual
questions where the expected technical scope is narrow and clearly
defined.

The **General LLM** has a stronger advantage as questions become more
open-ended and require:

- Multi-layer troubleshooting.
- Engineering trade-offs.
- Quantitative reasoning.
- System architecture.
- Evidence-based fault isolation.
- End-to-end telecom design.

This suggests that the General LLM has greater breadth of engineering
reasoning, while OTel 1.0 shows stronger performance in selected
focused telecom tasks.

## Recurring Technical Errors

### General LLM

The most significant recurring weakness is **confident technical
inaccuracy**.

Observed examples include:

- Incorrect 5G Core function assignments.
- Incorrect CU/DU/O-RAN functional allocation.
- Mixing 4G EPC concepts into 5G SA procedures.
- Incorrect NR/TDD terminology.
- Unrealistic MIMO assumptions.
- Incorrect quantitative calculations.
- Unsupported or overly specific engineering claims.

The General LLM therefore often produces technically fluent answers
that require expert validation.

### OTel 1.0

The dominant weakness is **limited response coverage and reasoning
depth**.

Observed patterns include:

- Non-responsive answers.
- Refusal to answer context-dependent questions.
- Incomplete technical explanations.
- Limited engineering reasoning.
- Incorrect quantitative calculations in some cases.
- Difficulty handling complex architecture and troubleshooting tasks.

When OTel 1.0 answers successfully, it is often concise and focused,
but its coverage is less consistent across difficult tasks.

## Non-Responsive and Insufficient Responses

A significant difference between the two models is their response
coverage.

The **General LLM** generally attempts the task, even when the answer
may contain technical errors.

The **OTel 1.0** produces a number of explicit non-responsive answers,
particularly in Track 2 across 3GPP classification, TELELOGS,
srsRANBench, TELETABLES and complex decision/reasoning questions.

This materially affects its overall benchmark performance.

## Benchmark Limitations

The following limitations should be considered when interpreting the
results:

1. **Track composition differs.** Track 1 is a custom telecom
   engineering benchmark, while Track 2 contains specialised industry
   benchmark subsets.

2. **Some questions are source-dependent.** Questions involving
   specific YANG elements, source code functions or standards tables
   may depend on access to the underlying technical source.

3. **Some inference outputs were truncated.** Where the final model
   answer was not visible, the expert assessment was based only on the
   available response and treated conservatively.

4. **Reference answers are not treated as infallible.** Expert review
   was used to identify cases where an answer or explanation required
   additional technical validation.

5. **Overall scores hide different failure modes.** The models do not
   simply differ in quality; they exhibit different patterns of
   technical error, reasoning depth and response coverage.

## Final Module 1 Baseline Conclusion

The **General LLM is the stronger overall baseline**, with broader
coverage and better performance across applied engineering,
troubleshooting, cloud-native architecture and complex telecom
reasoning.

**OTel 1.0** demonstrates useful strengths on selected focused
telecom questions and can outperform the General LLM on some
standards-oriented and narrow technical tasks. However, its higher
rate of non-responsive answers and weaker performance on complex
open-ended tasks limit its overall effectiveness.

The central finding of Module 1 is:

> **Technical fluency does not guarantee technical correctness.**

The baseline therefore establishes a strong reference point for the
subsequent modules, where additional capabilities such as RAG, MCP
and agent-based workflows can be evaluated against the standalone LLM
baseline.
