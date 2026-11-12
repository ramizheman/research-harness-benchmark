# Experiment pilot_v1

Tasks: 10. Conditions: A, B, C. Seeds: [1]. Models: gemini:gemini-2.5-flash.

## Summary by condition

| metric | A | B | C |
|---|---|---|---|
| runs | 10 | 10 | 10 |
| valid_outputs | 7 | 9 | 10 |
| P1_balanced_flag_accuracy | 0.417 | 0.583 | 0.583 |
| testability_auc | 0.450 | 0.938 | 0.719 |
| testability_brier | 0.337 | 0.269 | 0.259 |
| outcome_log_loss | 2.021 | 1.688 | 1.761 |
| risk_recall | 0.300 | 0.300 | 0.417 |
| prereg_quality | 0.937 | 0.957 | 0.961 |
| prior_work_recognized | 0.000 | 1.000 | 0.000 |
| false_prior_claim | n/a | 0.500 | 0.375 |
| proposal_max_similarity | 0.180 | 0.183 | 0.163 |
| input_tokens | 5778.857 | 9771.778 | 8370.200 |
| output_tokens | 5345.000 | 7401.667 | 6348.400 |
| n_tool_calls | 0.857 | 1.778 | 1.100 |
| memory_tool_calls | 0.000 | 0.889 | 0.500 |
| cost_usd_total | 0.181 | 0.209 | 0.184 |

## Primary contrasts (P1, balanced flag accuracy; task-level bootstrap and sign-flip test; Holm across contrasts)

| contrast | tasks | mean difference | 95% interval | p | p (Holm) |
|---|---|---|---|---|---|
| B - A | 6 | 0.208 | (0.000, 0.625) | 1.000 | 1.000 |
| C - A | 7 | 0.000 | (0.000, 0.000) | 1.000 | 1.000 |
| C - B | 9 | -0.046 | (-0.417, 0.278) | 1.000 | 1.000 |

## Secondary contrasts (not corrected; descriptive)

| metric | contrast | mean difference | 95% interval | p |
|---|---|---|---|---|
| testability_brier | B - A (sign flipped: positive = better) | 0.063 | (-0.057, 0.203) | 0.500 |
| outcome_log_loss | B - A (sign flipped: positive = better) | 0.294 | (-0.462, 1.177) | 0.625 |
| risk_recall | B - A | 0.000 | (0.000, 0.000) | 1.000 |
| prereg_quality | B - A | 0.018 | (-0.093, 0.120) | 0.750 |
| testability_brier | C - A (sign flipped: positive = better) | -0.013 | (-0.099, 0.083) | 0.812 |
| outcome_log_loss | C - A (sign flipped: positive = better) | 0.204 | (-0.229, 0.748) | 0.625 |
| risk_recall | C - A | 0.000 | (0.000, 0.000) | 1.000 |
| prereg_quality | C - A | 0.023 | (-0.024, 0.079) | 0.688 |
| testability_brier | C - B (sign flipped: positive = better) | -0.015 | (-0.134, 0.131) | 0.906 |
| outcome_log_loss | C - B (sign flipped: positive = better) | -0.212 | (-0.601, 0.143) | 0.406 |
| risk_recall | C - B | 0.000 | (0.000, 0.000) | 1.000 |
| prereg_quality | C - B | 0.006 | (-0.037, 0.055) | 1.000 |

C versus B equivalence on P1 (margin 0.1): 90% interval (-0.324, 0.185), equivalent: False.

Answer key: automated rule-based adjudication, not independent human adjudication. With 10 tasks the intervals are wide; the pilot checks the pipeline and gives a first effect-size estimate, not a confirmatory test.
