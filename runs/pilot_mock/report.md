# Experiment pilot_mock

**MOCK RUN.** Every output was produced by the scripted mock client. The numbers test the pipeline only and carry no information about memory or models.

Tasks: 10. Conditions: A, B, C. Seeds: [1]. Models: mock:scripted.

## Summary by condition

| metric | A | B | C |
|---|---|---|---|
| runs | 10 | 10 | 10 |
| valid_outputs | 10 | 10 | 10 |
| P1_balanced_flag_accuracy | 0.458 | 0.583 | 0.458 |
| testability_auc | 0.125 | 0.125 | 0.125 |
| testability_brier | 0.265 | 0.265 | 0.265 |
| outcome_log_loss | 1.620 | 1.622 | 1.620 |
| risk_recall | 0.083 | 0.083 | 0.083 |
| prereg_quality | 1.000 | 1.000 | 1.000 |
| prior_work_recognized | 0.000 | 0.500 | 1.000 |
| false_prior_claim | n/a | 1.000 | 1.000 |
| proposal_max_similarity | 0.141 | 0.141 | 0.141 |
| input_tokens | 2889.700 | 2875.600 | 2605.900 |
| output_tokens | 230.000 | 262.000 | 270.200 |
| n_tool_calls | 1.000 | 1.000 | 1.000 |
| memory_tool_calls | 0.000 | 1.000 | 1.000 |
| cost_usd_total | 0.000 | 0.000 | 0.000 |

## Primary contrasts (P1, balanced flag accuracy; task-level bootstrap and sign-flip test; Holm across contrasts)

| contrast | tasks | mean difference | 95% interval | p | p (Holm) |
|---|---|---|---|---|---|
| B - A | 10 | 0.125 | (0.000, 0.375) | 1.000 | 1.000 |
| C - A | 10 | 0.000 | (0.000, 0.000) | 1.000 | 1.000 |
| C - B | 10 | -0.125 | (-0.375, 0.000) | 1.000 | 1.000 |

## Secondary contrasts (not corrected; descriptive)

| metric | contrast | mean difference | 95% interval | p |
|---|---|---|---|---|
| testability_brier | B - A (sign flipped: positive = better) | 0.000 | (0.000, 0.000) | 1.000 |
| outcome_log_loss | B - A (sign flipped: positive = better) | -0.003 | (-0.080, 0.088) | 1.000 |
| risk_recall | B - A | 0.000 | (0.000, 0.000) | 1.000 |
| prereg_quality | B - A | 0.000 | (0.000, 0.000) | 1.000 |
| testability_brier | C - A (sign flipped: positive = better) | 0.000 | (0.000, 0.000) | 1.000 |
| outcome_log_loss | C - A (sign flipped: positive = better) | 0.000 | (0.000, 0.000) | 1.000 |
| risk_recall | C - A | 0.000 | (0.000, 0.000) | 1.000 |
| prereg_quality | C - A | 0.000 | (0.000, 0.000) | 1.000 |
| testability_brier | C - B (sign flipped: positive = better) | 0.000 | (0.000, 0.000) | 1.000 |
| outcome_log_loss | C - B (sign flipped: positive = better) | 0.003 | (-0.088, 0.080) | 1.000 |
| risk_recall | C - B | 0.000 | (0.000, 0.000) | 1.000 |
| prereg_quality | C - B | 0.000 | (0.000, 0.000) | 1.000 |

C versus B equivalence on P1 (margin 0.1): 90% interval (-0.375, 0.000), equivalent: False.

Answer key: automated rule-based adjudication, not independent human adjudication. With 10 tasks the intervals are wide; the pilot checks the pipeline and gives a first effect-size estimate, not a confirmatory test.
