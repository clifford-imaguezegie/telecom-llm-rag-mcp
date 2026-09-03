# Track 1 — Expert Technical Review

## Evaluation Methodology

The General LLM and OTel 1.0 responses were evaluated against the
custom 20-question telecom benchmark and its expected technical
criteria.

The final assessment was based on independent expert technical
review covering:

- Technical accuracy
- Completeness
- Relevance
- Engineering reasoning
- Practical applicability
- Factual reliability
- Overall technical performance

The Independent LLM Judge used during Track 1 is retained as a
supplementary evaluation layer only. The expert review is the final
evaluation authority.

## Expert Scorecard

| ID | Category | G Acc | G Comp | G Rel | G Reason | G Practical | G Reliability | G Overall | O Acc | O Comp | O Rel | O Reason | O Practical | O Reliability | O Overall | Winner | Confidence |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| Q01 | 5G Core | 6 | 6 | 8 | 6 | 6 | 6 | 68 | 8 | 7 | 8 | 7 | 7 | 8 | 80 | OTEL 1.0 | 90 |
| Q02 | 5G Core | 4 | 3 | 7 | 4 | 4 | 4 | 48 | 7 | 7 | 8 | 7 | 7 | 7 | 73 | OTEL 1.0 | 90 |
| Q03 | 5G RAN | 3 | 4 | 6 | 4 | 4 | 3 | 42 | 7 | 7 | 8 | 7 | 7 | 7 | 74 | OTEL 1.0 | 95 |
| Q04 | 5G RAN | 7 | 7 | 8 | 7 | 7 | 7 | 82 | 7 | 6 | 7 | 6 | 6 | 7 | 72 | GENERAL LLM | 85 |
| Q05 | 5G SA Procedures | 4 | 4 | 7 | 4 | 5 | 4 | 55 | 5 | 5 | 7 | 5 | 5 | 5 | 58 | OTEL 1.0 | 70 |
| Q06 | 5G SA Procedures | 6 | 5 | 7 | 5 | 5 | 5 | 62 | 5 | 4 | 6 | 4 | 4 | 5 | 50 | GENERAL LLM | 80 |
| Q07 | Open RAN | 2 | 3 | 5 | 3 | 3 | 2 | 32 | 6 | 6 | 7 | 6 | 6 | 6 | 64 | OTEL 1.0 | 95 |
| Q08 | Open RAN | 7 | 6 | 8 | 7 | 7 | 7 | 78 | 7 | 7 | 8 | 7 | 7 | 7 | 76 | GENERAL LLM | 60 |
| Q09 | Cloud-Native Telecom | 8 | 8 | 9 | 8 | 8 | 8 | 89 | 7 | 7 | 8 | 7 | 7 | 7 | 79 | GENERAL LLM | 85 |
| Q10 | Cloud-Native Telecom | 9 | 9 | 9 | 9 | 9 | 9 | 94 | 7 | 7 | 8 | 7 | 7 | 7 | 78 | GENERAL LLM | 90 |
| Q11 | Applied Telecom Engineering | 5 | 5 | 7 | 5 | 5 | 4 | 55 | 4 | 4 | 6 | 4 | 4 | 4 | 45 | GENERAL LLM | 80 |
| Q12 | Applied Telecom Engineering | 8 | 8 | 9 | 8 | 8 | 8 | 89 | 6 | 6 | 7 | 6 | 6 | 6 | 66 | GENERAL LLM | 90 |
| Q13 | 5G Capacity Planning | 3 | 4 | 7 | 2 | 3 | 3 | 42 | 4 | 5 | 7 | 4 | 4 | 4 | 48 | OTEL 1.0 | 85 |
| Q14 | 5G UL/DL Trade-off | 5 | 5 | 7 | 5 | 5 | 5 | 58 | 7 | 7 | 8 | 7 | 7 | 7 | 74 | OTEL 1.0 | 90 |
| Q15 | 5G Throughput Troubleshooting | 7 | 7 | 8 | 7 | 7 | 6 | 78 | 5 | 5 | 7 | 5 | 5 | 5 | 58 | GENERAL LLM | 90 |
| Q16 | Open RAN Deployment | 6 | 6 | 7 | 6 | 6 | 6 | 72 | 1 | 1 | 1 | 1 | 1 | 1 | 10 | GENERAL LLM | 100 |
| Q17 | Cloud-Native Telecom | 8 | 8 | 8 | 8 | 8 | 8 | 87 | 7 | 7 | 7 | 7 | 7 | 7 | 74 | GENERAL LLM | 90 |
| Q18 | RAN Capacity Expansion | 8 | 8 | 8 | 8 | 8 | 8 | 87 | 7 | 7 | 8 | 7 | 7 | 7 | 78 | GENERAL LLM | 80 |
| Q19 | Network Failure Isolation | 8 | 8 | 9 | 9 | 8 | 8 | 92 | 1 | 1 | 1 | 1 | 1 | 1 | 10 | GENERAL LLM | 100 |
| Q20 | End-to-End Network Design | 5 | 5 | 7 | 5 | 5 | 5 | 61 | 1 | 1 | 1 | 1 | 1 | 1 | 10 | GENERAL LLM | 100 |

## Expert Review Summary

### General LLM

The General LLM demonstrates broader engineering coverage and is
particularly strong in cloud-native telecom, troubleshooting,
capacity expansion and complex architecture.

Its principal weakness is confident telecom-specific hallucination,
including incorrect 5G Core responsibilities, RAN/O-RAN functional
allocation, SA procedure terminology and quantitative engineering
assumptions.

### OTel 1.0

OTel 1.0 performs comparatively well on selected 5G Core, RAN,
Open RAN and focused engineering questions.

Its principal weakness is limited performance on complex,
open-ended engineering tasks, including outright non-responsive
answers on several questions.

## Final Track 1 Benchmark Comment

The expert review shows that the **General LLM is the stronger overall
performer in Track 1**, winning **13 of 20 questions (65%)**.

**OTel 1.0 wins 7 questions (35%)**, with strengths in selected 5G
Core, RAN, Open RAN and engineering trade-off questions.

Overall, the **General LLM provides broader engineering capability**,
while **OTel 1.0 is more concise and competitive on selected
telecom-specific fundamentals**. Both models remain susceptible to
technical inaccuracies, confirming the importance of independent
expert validation.
