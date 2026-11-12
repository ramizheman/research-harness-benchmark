# Experiment pilot_v1

Tasks: 10. Conditions: A, B, C. Seeds: [1]. Models: gemini:gemini-2.5-flash.

## Summary by condition

| metric | A | B | C |
|---|---|---|---|
| runs | 10 | 10 | 10 |
| valid_outputs | 10 | 10 | 10 |
| P1_balanced_flag_accuracy | 0.583 | 0.625 | 0.583 |
| testability_auc | 0.625 | 0.812 | 0.719 |
| testability_brier | 0.260 | 0.251 | 0.259 |
| outcome_log_loss | 1.897 | 1.589 | 1.761 |
| risk_recall | 0.417 | 0.417 | 0.417 |
| prereg_quality | 0.956 | 0.955 | 0.961 |
| prior_work_recognized | 0.000 | 0.500 | 0.000 |
| false_prior_claim | n/a | 0.500 | 0.375 |
| proposal_max_similarity | 0.166 | 0.182 | 0.163 |
| input_tokens | 7226.500 | 9596.000 | 8370.200 |
| output_tokens | 6356.400 | 7201.200 | 6348.400 |
| n_tool_calls | 0.800 | 1.600 | 1.100 |
| memory_tool_calls | 0.000 | 0.800 | 0.500 |
| cost_usd_total | 0.181 | 0.209 | 0.184 |

## Primary contrasts (P1, balanced flag accuracy; task-level bootstrap and sign-flip test; Holm across contrasts)

| contrast | tasks | mean difference | 95% interval | p | p (Holm) |
|---|---|---|---|---|---|
| B - A | 10 | 0.042 | (-0.250, 0.375) | 1.000 | 1.000 |
| C - A | 10 | 0.000 | (0.000, 0.000) | 1.000 | 1.000 |
| C - B | 10 | -0.042 | (-0.375, 0.250) | 1.000 | 1.000 |

## Secondary contrasts (not corrected; descriptive)

| metric | contrast | mean difference | 95% interval | p |
|---|---|---|---|---|
| testability_brier | B - A (sign flipped: positive = better) | 0.009 | (-0.126, 0.130) | 0.898 |
| outcome_log_loss | B - A (sign flipped: positive = better) | 0.309 | (-0.156, 0.852) | 0.344 |
| risk_recall | B - A | 0.000 | (0.000, 0.000) | 1.000 |
| prereg_quality | B - A | -0.000 | (-0.067, 0.066) | 0.875 |
| testability_brier | C - A (sign flipped: positive = better) | 0.001 | (-0.066, 0.072) | 1.000 |
| outcome_log_loss | C - A (sign flipped: positive = better) | 0.136 | (-0.349, 0.603) | 0.617 |
| risk_recall | C - A | 0.000 | (0.000, 0.000) | 1.000 |
| prereg_quality | C - A | 0.005 | (-0.034, 0.050) | 1.000 |
| testability_brier | C - B (sign flipped: positive = better) | -0.008 | (-0.118, 0.122) | 0.938 |
| outcome_log_loss | C - B (sign flipped: positive = better) | -0.172 | (-0.532, 0.150) | 0.453 |
| risk_recall | C - B | 0.000 | (0.000, 0.000) | 1.000 |
| prereg_quality | C - B | 0.005 | (-0.033, 0.050) | 1.000 |

C versus B equivalence on P1 (margin 0.1): 90% interval (-0.292, 0.167), equivalent: False.

Answer key: automated rule-based adjudication, not independent human adjudication. With 10 tasks the intervals are wide; the pilot checks the pipeline and gives a first effect-size estimate, not a confirmatory test.
