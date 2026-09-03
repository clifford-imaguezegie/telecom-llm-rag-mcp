# Track 2 — Expert Technical Review

## Evaluation Methodology

The General LLM and OTel 1.0 responses were evaluated against the
frozen 32-question Track 2 industry benchmark and its reference
answers / expected criteria.

The final assessment was based on independent expert technical review
covering:

- Technical accuracy
- Completeness
- Relevance
- Engineering reasoning
- Practical applicability
- Factual reliability
- Overall technical performance
- Correctness of the final answer where objective answers were provided

For multiple-choice, classification and quantitative questions, the
benchmark reference answer was used as the primary correctness
criterion.

No Independent LLM Judge was applied to Track 2. The expert review is
the final evaluation authority.

---

## Expert Scorecard

| ID | Benchmark | G Acc | G Comp | G Rel | G Reason | G Practical | G Reliability | G Overall | O Acc | O Comp | O Rel | O Reason | O Practical | O Reliability | O Overall | Winner | Confidence |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| T2-01 | 3GPP_TSG | 9 | 8 | 9 | 8 | 8 | 9 | 94 | 1 | 1 | 1 | 1 | 1 | 1 | 5 | GENERAL LLM | 100 |
| T2-02 | 3GPP_TSG | 9 | 9 | 9 | 9 | 8 | 9 | 95 | 1 | 1 | 1 | 1 | 1 | 1 | 5 | GENERAL LLM | 100 |
| T2-03 | 3GPP_TSG | 2 | 2 | 8 | 2 | 2 | 2 | 28 | 1 | 1 | 1 | 1 | 1 | 1 | 5 | GENERAL LLM | 100 |
| T2-04 | 3GPP_TSG | 3 | 3 | 7 | 3 | 3 | 3 | 35 | 1 | 1 | 1 | 1 | 1 | 1 | 5 | GENERAL LLM | 100 |
| T2-05 | ORANBENCH | 4 | 5 | 7 | 4 | 4 | 4 | 48 | 1 | 1 | 1 | 1 | 1 | 1 | 5 | GENERAL LLM | 100 |
| T2-06 | ORANBENCH | 7 | 6 | 8 | 7 | 7 | 7 | 78 | 8 | 5 | 8 | 8 | 8 | 8 | 88 | OTEL 1.0 | 90 |
| T2-07 | ORANBENCH | 9 | 8 | 9 | 9 | 8 | 9 | 95 | 9 | 9 | 9 | 9 | 9 | 9 | 96 | OTEL 1.0 | 70 |
| T2-08 | ORANBENCH | 3 | 4 | 7 | 3 | 3 | 3 | 35 | 2 | 3 | 7 | 2 | 2 | 2 | 28 | GENERAL LLM | 70 |
| T2-09 | SIXG_BENCH | 7 | 7 | 8 | 7 | 7 | 7 | 80 | 9 | 8 | 9 | 8 | 8 | 9 | 93 | OTEL 1.0 | 90 |
| T2-10 | SIXG_BENCH | 6 | 6 | 8 | 6 | 6 | 6 | 70 | 1 | 1 | 1 | 1 | 1 | 1 | 5 | GENERAL LLM | 100 |
| T2-11 | SIXG_BENCH | 6 | 6 | 8 | 6 | 6 | 6 | 70 | 1 | 1 | 1 | 1 | 1 | 1 | 5 | GENERAL LLM* | 70 |
| T2-12 | SIXG_BENCH | 9 | 9 | 9 | 9 | 9 | 9 | 96 | 9 | 8 | 9 | 8 | 9 | 9 | 94 | GENERAL LLM | 80 |
| T2-13 | SRSRANBENCH | 9 | 8 | 9 | 8 | 8 | 9 | 94 | 1 | 1 | 1 | 1 | 1 | 1 | 5 | GENERAL LLM | 100 |
| T2-14 | SRSRANBENCH | 10 | 10 | 10 | 9 | 9 | 10 | 99 | 10 | 10 | 10 | 10 | 10 | 10 | 100 | OTEL 1.0 | 60 |
| T2-15 | SRSRANBENCH | 10 | 10 | 10 | 9 | 9 | 10 | 99 | 1 | 1 | 1 | 1 | 1 | 1 | 5 | GENERAL LLM | 100 |
| T2-16 | SRSRANBENCH | 10 | 9 | 10 | 9 | 9 | 10 | 99 | 1 | 1 | 1 | 1 | 1 | 1 | 5 | GENERAL LLM | 100 |
| T2-17 | TELELOGS | 5 | 5 | 7 | 4 | 4 | 5 | 52 | 1 | 1 | 1 | 1 | 1 | 1 | 5 | GENERAL LLM | 100 |
| T2-18 | TELELOGS | 5 | 5 | 7 | 4 | 4 | 5 | 52 | 1 | 1 | 1 | 1 | 1 | 1 | 5 | GENERAL LLM | 100 |
| T2-19 | TELELOGS | 4 | 5 | 7 | 4 | 4 | 4 | 48 | 1 | 1 | 1 | 1 | 1 | 1 | 5 | GENERAL LLM | 100 |
| T2-20 | TELELOGS | 4 | 4 | 7 | 3 | 3 | 4 | 43 | 1 | 1 | 1 | 1 | 1 | 1 | 5 | GENERAL LLM | 100 |
| T2-21 | TELEMATH | 5 | 5 | 7 | 4 | 4 | 4 | 55 | 3 | 3 | 6 | 3 | 3 | 3 | 30 | GENERAL LLM | 90 |
| T2-22 | TELEMATH | 9 | 9 | 10 | 9 | 9 | 9 | 96 | 4 | 1 | 3 | 1 | 1 | 3 | 20 | GENERAL LLM | 100 |
| T2-23 | TELEMATH | 7 | 6 | 8 | 7 | 7 | 7 | 75 | 2 | 2 | 7 | 2 | 2 | 2 | 20 | GENERAL LLM* | 75 |
| T2-24 | TELEMATH | 7 | 6 | 8 | 6 | 6 | 6 | 70 | 3 | 2 | 7 | 2 | 2 | 3 | 25 | GENERAL LLM* | 70 |
| T2-25 | TELEQNA | 8 | 6 | 8 | 7 | 6 | 7 | 78 | 1 | 1 | 1 | 1 | 1 | 1 | 5 | GENERAL LLM | 100 |
| T2-26 | TELEQNA | 10 | 9 | 10 | 9 | 9 | 10 | 98 | 10 | 10 | 10 | 10 | 10 | 10 | 100 | OTEL 1.0 | 55 |
| T2-27 | TELEQNA | 8 | 8 | 9 | 7 | 7 | 7 | 85 | 9 | 8 | 9 | 8 | 8 | 9 | 93 | OTEL 1.0 | 75 |
| T2-28 | TELEQNA | 10 | 9 | 10 | 9 | 9 | 10 | 98 | 1 | 1 | 1 | 1 | 1 | 1 | 5 | GENERAL LLM | 100 |
| T2-29 | TELETABLES | 2 | 2 | 6 | 2 | 2 | 2 | 25 | 2 | 2 | 6 | 2 | 2 | 2 | 25 | TIE | 100 |
| T2-30 | TELETABLES | 8 | 7 | 9 | 7 | 7 | 7 | 82 | 1 | 1 | 1 | 1 | 1 | 1 | 5 | GENERAL LLM | 95 |
| T2-31 | TELETABLES | 4 | 4 | 7 | 3 | 3 | 3 | 40 | 10 | 9 | 10 | 9 | 9 | 10 | 99 | OTEL 1.0 | 100 |
| T2-32 | TELETABLES | 3 | 3 | 7 | 2 | 2 | 3 | 30 | 3 | 3 | 7 | 3 | 3 | 3 | 30 | TIE | 100 |

\* The supplied inference output was truncated before the General LLM
response reached a confirmed final answer. These comparisons should
therefore be regarded as provisional.

---

# Expert Review Comments

## 3GPP Working-Group Classification

**T2-01:** The **General LLM** correctly classifies the document as
**RAN1**. The **OTel 1.0** response is non-responsive.

**T2-02:** The **General LLM** correctly classifies the document as
**RAN4**, consistent with RF, spectrum and receiver-performance work.
The **OTel 1.0** response is non-responsive.

**T2-03:** The **General LLM** incorrectly classifies the document as
**SA1**. The text concerns closed-loop power control and physical-layer
behaviour, making **RAN1** the appropriate working group. The
**OTel 1.0** response is non-responsive.

**T2-04:** The **General LLM** incorrectly classifies the document as
**SA2**. The text concerns PCC/PCEF bearer binding and explicitly
references SA2 requirements being implemented by CT3. **CT3** is the
appropriate working group. The **OTel 1.0** response is
non-responsive.

## O-RAN

**T2-05:** The **General LLM** selects **"All of the above"**, but the
specific Handover Preparation procedures described correspond to the
Xn/X2, NG and inter-RAT conditional handover scenario. The appropriate
answer is **option 3**. The **OTel 1.0** response is non-responsive.

**T2-06:** Both the **General LLM** and **OTel 1.0** select the correct
**option 2**. The OTel 1.0 answer is more direct and avoids unnecessary
additional claims.

**T2-07:** Both the **General LLM** and **OTel 1.0** correctly select
**option 3, perceivedSeverity**. OTel 1.0 provides the cleaner
standards-oriented mapping.

**T2-08:** Both the **General LLM** and **OTel 1.0** are incorrect.
The correct answer is **option 3, `ctiConnProfileRef`**. Neither model
correctly identifies the CTI connection-profile reference.

## 6G / Decision-Reasoning

**T2-09:** Both models provide a decision-oriented response, but
**OTel 1.0** more directly aligns its choice with the supplied
worst-case risk criteria. The conservative URLLC continuation is the
appropriate decision.

**T2-10:** The **General LLM** provides a substantive worst-case
analysis, but the supplied response is truncated before the final
decision. The **OTel 1.0** response is non-responsive.

**T2-11:** The **General LLM** response is truncated before its final
decision. The **OTel 1.0** response is non-responsive. The comparison
is therefore provisional.

**T2-12:** Both the **General LLM** and **OTel 1.0** correctly select
**option 3**. The General LLM provides the more complete risk analysis,
while OTel 1.0 provides a concise and technically aligned justification.

## srsRANBench

**T2-13:** The **General LLM** correctly selects **option 1** for the
`lower_phy_controller` class. The **OTel 1.0** response is
non-responsive.

**T2-14:** Both the **General LLM** and **OTel 1.0** correctly select
**option 3**. This is a strong agreement case.

**T2-15:** The **General LLM** correctly selects **option 1** for
`specific_init()`. The **OTel 1.0** response is non-responsive.

**T2-16:** The **General LLM** correctly selects **option 1** for the
`SetUp()` method. The **OTel 1.0** response is non-responsive.

This subset demonstrates stronger source-oriented response capability
from the **General LLM**, while **OTel 1.0** frequently declines when
the required context is not available.

## TELELOGS

**T2-17 to T2-20:** The **OTel 1.0** responses are all
non-responsive, representing a significant capability gap on
data-driven telecom fault-isolation tasks.

The **General LLM** attempts detailed drive-test analysis across these
questions, but the responses are incomplete and contain incorrect or
unsupported engineering interpretations.

These questions require correlation of throughput degradation with
specific KPIs and engineering parameters such as scheduled RBs,
handover behaviour, interference, overshooting and vehicle speed.

The **General LLM** therefore demonstrates greater analytical coverage,
but its conclusions still require technical validation.

## TELEMATH

**T2-21:** Both the **General LLM** and **OTel 1.0** produce incorrect
numerical results. The reference result is approximately **16.31 km**,
rather than the values produced by either model.

**T2-22:** The **General LLM** correctly calculates the source-coding
efficiency as **1.0** for the uniform quaternary source using a
two-bit fixed-length code. The **OTel 1.0** response simply states
"True" and does not answer the numerical question.

**T2-23:** The **OTel 1.0** response incorrectly calculates the
unavailability as **0.3** by adding \(p\) and \(q\). The correct
steady-state result is approximately **0.3333**. The **General LLM**
shows substantially better understanding of the stochastic process,
although the supplied response is truncated before its final result.

**T2-24:** The **OTel 1.0** response incorrectly calculates the
normalized throughput as **1.6667**. The reference result is
approximately **0.60625**. The **General LLM** begins a more
appropriate derivation, but the supplied response is truncated before
completion.

## TELEQNA

**T2-25:** The **General LLM** identifies the correct qualitative
answer, **less than 0.5 °C**. The **OTel 1.0** response does not provide
an answer.

**T2-26:** Both the **General LLM** and **OTel 1.0** correctly select
**option 2**. Both responses are substantively aligned with the
reference.

**T2-27:** Both the **General LLM** and **OTel 1.0** correctly identify
**option 1**, pulsed-wave 2450 MHz fields. OTel 1.0 gives the cleaner
and more concise response.

**T2-28:** The **General LLM** correctly selects **option 2**. The
**OTel 1.0** response is non-responsive.

## TELETABLES

**T2-29:** Both the **General LLM** and **OTel 1.0** give incorrect
answers. The correct answer is **option 3, 1.0 dB**.

**T2-30:** The **General LLM** selects **option 4** and provides a
plausible interpretation. The **OTel 1.0** response is non-responsive.

**T2-31:** The **OTel 1.0** correctly selects **Index 6**, matching the
benchmark reference. The **General LLM** does not resolve the specific
index and remains speculative.

**T2-32:** Both the **General LLM** and **OTel 1.0** are incorrect.
The correct answer is **option 1, 8%**. Both models reason incorrectly
from channel/subcarrier relationships rather than the benchmark's
standard-defined transmission-bandwidth values.

---

# Overall Track 2 Assessment

## General LLM

The **General LLM** demonstrates broader coverage across the industry
benchmark and is substantially more capable of attempting complex,
source-dependent and engineering-analysis tasks.

Its major weakness is **confident technical error**. Several responses
are fluent and detailed but contain incorrect standards
classifications, unsupported engineering assumptions or incorrect
quantitative reasoning.

## OTel 1.0

**OTel 1.0** performs well on selected focused technical questions,
particularly when the required answer is explicit and narrowly scoped.

Its major weakness is **limited response coverage**, with numerous
non-responsive answers across 3GPP classification, TELELOGS,
srsRANBench and TELETABLES. When it does answer, it can still produce
incorrect quantitative or standards-based results.

## Final Track 2 Benchmark Comment

The expert review shows that the **General LLM is the stronger overall
performer in Track 2**, demonstrating broader capability across 3GPP
classification, software/code-oriented questions, quantitative
reasoning and telecom troubleshooting.

**OTel 1.0** performs well on selected focused questions, particularly
some O-RAN, 6G decision-making and standards-oriented tasks. However,
it has a significant weakness in source-dependent and detailed
analytical tasks, with numerous non-responsive responses.

Overall, the **General LLM is the Track 2 winner**. The benchmark also
reinforces that **technical fluency does not guarantee technical
correctness**, making expert validation important for standards-based,
quantitative and engineering tasks.
