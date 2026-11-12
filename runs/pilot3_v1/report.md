# Experiment pilot3_v1

Tasks: 10. Conditions: A, B, C. Seeds: [1, 2, 3]. Models: gemini:gemini-2.5-flash.

## Summary by condition

| metric | A | B | C |
|---|---|---|---|
| runs | 30 | 30 | 30 |
| valid_outputs | 30 | 29 | 29 |
| P1_balanced_flag_accuracy | 0.639 | 0.669 | 0.574 |
| testability_auc | 0.653 | 0.679 | 0.804 |
| testability_brier | 0.232 | 0.336 | 0.254 |
| outcome_log_loss | 1.879 | 1.757 | 1.567 |
| risk_recall | 0.639 | 0.647 | 0.472 |
| prereg_quality | 0.967 | 0.960 | 0.971 |
| prior_work_recognized | 0.000 | 0.500 | 0.400 |
| false_prior_claim | n/a | 0.261 | 0.542 |
| proposal_max_similarity | 0.175 | 0.182 | 0.193 |
| input_tokens | 3044.733 | 5076.448 | 5539.793 |
| output_tokens | 4661.000 | 6188.897 | 6427.724 |
| n_tool_calls | 1.000 | 1.000 | 1.000 |
| memory_tool_calls | 0.000 | 1.000 | 1.000 |
| cost_usd_total | 0.377 | 0.510 | 0.547 |
| retrieval_attempted_rate | 1.000 | 1.000 | 1.000 |
| retrieval_first_rate | 1.000 | 1.000 | 1.000 |
| retrieval_successful_rate | 0.000 | 0.200 | 0.267 |
| meaningfully_used_rate | 0.000 | 0.200 | 0.267 |
| fabricated_citations_total | 0 | 0 | 0 |
| status_claims_checked_total | 0 | 70 | 97 |
| representation_accuracy | n/a | 1.000 | 1.000 |
| retrieval_latency_mean_s | 0.000 | 0.004 | 0.006 |
| memory_tokens_carried_mean | 8.000 | 1202.933 | 1504.233 |
| repair_turns_total | 0 | 2 | 1 |
| gate_turns_total | 0 | 0 | 0 |
| parse_recoveries_total | 30 | 35 | 35 |
| stop_reasons | final | final | final |
| preliminary_answers_total | 0 | 0 | 0 |
| correction_turns_total | 0 | 0 | 2 |
| initial_citation_problems_total | 0 | 0 | 2 |
| pre_n_fabricated_citations_total | 0 | 0 | 0 |

## Primary contrasts (P1, balanced flag accuracy; task-level bootstrap and sign-flip test; Holm across contrasts)

| contrast | tasks | mean difference | 95% interval | p | p (Holm) |
|---|---|---|---|---|---|
| B - A | 10 | 0.042 | (-0.264, 0.389) | 0.906 | 1.000 |
| C - A | 10 | -0.056 | (-0.361, 0.292) | 0.844 | 1.000 |
| C - B | 10 | -0.097 | (-0.278, 0.083) | 0.367 | 1.000 |

## Secondary contrasts (not corrected; descriptive)

| metric | contrast | mean difference | 95% interval | p |
|---|---|---|---|---|
| testability_brier | B - A (sign flipped: positive = better) | -0.093 | (-0.245, 0.071) | 0.305 |
| outcome_log_loss | B - A (sign flipped: positive = better) | 0.154 | (-0.391, 0.672) | 0.605 |
| risk_recall | B - A | -0.028 | (-0.333, 0.306) | 1.000 |
| prereg_quality | B - A | -0.007 | (-0.048, 0.032) | 0.781 |
| testability_brier | C - A (sign flipped: positive = better) | -0.019 | (-0.143, 0.128) | 0.812 |
| outcome_log_loss | C - A (sign flipped: positive = better) | 0.324 | (-0.179, 0.910) | 0.344 |
| risk_recall | C - A | -0.167 | (-0.500, 0.000) | 1.000 |
| prereg_quality | C - A | 0.006 | (-0.030, 0.039) | 0.750 |
| testability_brier | C - B (sign flipped: positive = better) | 0.074 | (-0.033, 0.185) | 0.230 |
| outcome_log_loss | C - B (sign flipped: positive = better) | 0.171 | (-0.301, 0.723) | 0.586 |
| risk_recall | C - B | -0.139 | (-0.389, 0.056) | 0.500 |
| prereg_quality | C - B | 0.013 | (-0.009, 0.039) | 0.438 |

C versus B equivalence on P1 (margin 0.1): 90% interval (-0.250, 0.056), equivalent: False.

Answer key: automated rule-based adjudication, not independent human adjudication. With 10 tasks the intervals are wide; the pilot checks the pipeline and gives a first effect-size estimate, not a confirmatory test.
