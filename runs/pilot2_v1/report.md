# Experiment pilot2_v1

Tasks: 10. Conditions: A, B, C. Seeds: [1]. Models: gemini:gemini-2.5-flash.

## Summary by condition

| metric | A | B | C |
|---|---|---|---|
| runs | 10 | 10 | 10 |
| valid_outputs | 10 | 9 | 10 |
| P1_balanced_flag_accuracy | 0.583 | 0.583 | 0.542 |
| testability_auc | 0.656 | 0.938 | 0.688 |
| testability_brier | 0.239 | 0.152 | 0.236 |
| outcome_log_loss | 2.003 | 1.631 | 1.803 |
| risk_recall | 0.583 | 0.400 | 0.583 |
| prereg_quality | 0.933 | 0.957 | 0.961 |
| prior_work_recognized | 0.000 | 0.000 | 0.000 |
| false_prior_claim | n/a | 0.286 | 0.125 |
| proposal_max_similarity | 0.167 | 0.183 | 0.177 |
| input_tokens | 6240.300 | 8362.889 | 9772.500 |
| output_tokens | 4283.500 | 5461.778 | 5955.200 |
| n_tool_calls | 1.000 | 1.000 | 1.000 |
| memory_tool_calls | 0.000 | 1.000 | 1.000 |
| cost_usd_total | 0.126 | 0.163 | 0.178 |
| retrieval_attempted_rate | 1.000 | 1.000 | 1.000 |
| retrieval_first_rate | 1.000 | 1.000 | 1.000 |
| retrieval_successful_rate | 0.000 | 0.500 | 0.400 |
| meaningfully_used_rate | 0.000 | 0.400 | 0.300 |
| fabricated_citations_total | 0 | 0 | 3 |
| status_claims_checked_total | 0 | 20 | 25 |
| representation_accuracy | n/a | 0.900 | 0.640 |
| retrieval_latency_mean_s | 0.000 | 0.006 | 0.007 |
| memory_tokens_carried_mean | 8.000 | 748.300 | 1171.400 |
| repair_turns_total | 0 | 0 | 0 |
| gate_turns_total | 7 | 9 | 9 |
| parse_recoveries_total | 19 | 25 | 27 |
| stop_reasons | final | final | final |

## Primary contrasts (P1, balanced flag accuracy; task-level bootstrap and sign-flip test; Holm across contrasts)

| contrast | tasks | mean difference | 95% interval | p | p (Holm) |
|---|---|---|---|---|---|
| B - A | 10 | -0.042 | (-0.375, 0.250) | 1.000 | 1.000 |
| C - A | 10 | -0.042 | (-0.375, 0.250) | 1.000 | 1.000 |
| C - B | 10 | 0.000 | (-0.375, 0.375) | 1.000 | 1.000 |

## Secondary contrasts (not corrected; descriptive)

| metric | contrast | mean difference | 95% interval | p |
|---|---|---|---|---|
| testability_brier | B - A (sign flipped: positive = better) | 0.077 | (-0.073, 0.246) | 0.391 |
| outcome_log_loss | B - A (sign flipped: positive = better) | 0.414 | (-0.096, 1.157) | 0.312 |
| risk_recall | B - A | -0.167 | (-0.500, 0.000) | 1.000 |
| prereg_quality | B - A | 0.028 | (-0.022, 0.083) | 0.469 |
| testability_brier | C - A (sign flipped: positive = better) | 0.003 | (-0.130, 0.161) | 0.988 |
| outcome_log_loss | C - A (sign flipped: positive = better) | 0.200 | (-0.339, 0.837) | 0.582 |
| risk_recall | C - A | 0.000 | (0.000, 0.000) | 1.000 |
| prereg_quality | C - A | 0.028 | (-0.000, 0.061) | 0.250 |
| testability_brier | C - B (sign flipped: positive = better) | -0.074 | (-0.153, -0.010) | 0.078 |
| outcome_log_loss | C - B (sign flipped: positive = better) | -0.214 | (-0.585, 0.150) | 0.312 |
| risk_recall | C - B | 0.167 | (0.000, 0.500) | 1.000 |
| prereg_quality | C - B | 0.000 | (-0.050, 0.056) | 1.000 |

C versus B equivalence on P1 (margin 0.1): 90% interval (-0.250, 0.250), equivalent: False.

Answer key: automated rule-based adjudication, not independent human adjudication. With 10 tasks the intervals are wide; the pilot checks the pipeline and gives a first effect-size estimate, not a confirmatory test.
