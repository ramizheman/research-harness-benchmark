# Experiment reasoning_models_v1

Tasks: 10. Conditions: A, B, C. Seeds: [1, 2, 3]. Models: openrouter:anthropic/claude-sonnet-5.5, openrouter:deepseek/deepseek-v4-pro.

## Summary by condition

| metric | A | B | C |
|---|---|---|---|
| runs | 60 | 60 | 60 |
| valid_outputs | 60 | 53 | 56 |
| P1_balanced_flag_accuracy | 0.625 | 0.670 | 0.725 |
| testability_auc | 0.595 | 0.695 | 0.664 |
| testability_brier | 0.297 | 0.284 | 0.278 |
| outcome_log_loss | 1.565 | 1.512 | 1.459 |
| risk_recall | 0.819 | 0.887 | 0.833 |
| prereg_quality | 0.960 | 0.971 | 0.974 |
| prior_work_recognized | 0.000 | 0.400 | 0.583 |
| false_prior_claim | n/a | 0.442 | 0.591 |
| proposal_max_similarity | 0.171 | 0.179 | 0.180 |
| input_tokens | 5421.183 | 11423.981 | 12621.161 |
| output_tokens | 5252.983 | 7156.377 | 7252.214 |
| n_tool_calls | 1.533 | 2.057 | 2.125 |
| memory_tool_calls | 0.000 | 1.623 | 1.661 |
| cost_usd_total | 2.137 | 2.884 | 2.670 |
| retrieval_attempted_rate | 1.000 | 1.000 | 1.000 |
| retrieval_first_rate | 1.000 | 1.000 | 1.000 |
| retrieval_successful_rate | 0.000 | 0.217 | 0.217 |
| meaningfully_used_rate | 0.000 | 0.200 | 0.217 |
| fabricated_citations_total | 0 | 0 | 0 |
| status_claims_checked_total | 0 | 190 | 200 |
| representation_accuracy | n/a | 1.000 | 1.000 |
| retrieval_latency_mean_s | 0.000 | 0.007 | 0.007 |
| memory_tokens_carried_mean | 12.250 | 3217.083 | 4213.767 |
| repair_turns_total | 1 | 0 | 2 |
| gate_turns_total | 0 | 0 | 1 |
| parse_recoveries_total | 14 | 8 | 9 |
| stop_reasons | final | final | final |
| preliminary_answers_total | 0 | 0 | 0 |
| correction_turns_total | 0 | 1 | 0 |
| initial_citation_problems_total | 0 | 1 | 0 |
| pre_n_fabricated_citations_total | 0 | 0 | 0 |

## Primary contrasts (P1, balanced flag accuracy; task-level bootstrap and sign-flip test; Holm across contrasts)

| contrast | tasks | mean difference | 95% interval | p | p (Holm) |
|---|---|---|---|---|---|
| B - A | 10 | 0.042 | (-0.118, 0.208) | 0.711 | 1.000 |
| C - A | 10 | 0.097 | (0.035, 0.167) | 0.062 | 0.188 |
| C - B | 10 | 0.056 | (-0.097, 0.194) | 0.531 | 1.000 |

## Secondary contrasts (not corrected; descriptive)

| metric | contrast | mean difference | 95% interval | p |
|---|---|---|---|---|
| testability_brier | B - A (sign flipped: positive = better) | 0.018 | (-0.035, 0.066) | 0.525 |
| outcome_log_loss | B - A (sign flipped: positive = better) | 0.042 | (-0.148, 0.259) | 0.721 |
| risk_recall | B - A | -0.056 | (-0.194, 0.083) | 0.750 |
| prereg_quality | B - A | -0.086 | (-0.156, -0.023) | 0.047 |
| testability_brier | C - A (sign flipped: positive = better) | 0.014 | (-0.024, 0.052) | 0.498 |
| outcome_log_loss | C - A (sign flipped: positive = better) | 0.085 | (-0.104, 0.310) | 0.514 |
| risk_recall | C - A | -0.028 | (-0.083, 0.000) | 1.000 |
| prereg_quality | C - A | -0.036 | (-0.093, 0.012) | 0.244 |
| testability_brier | C - B (sign flipped: positive = better) | -0.004 | (-0.067, 0.060) | 0.904 |
| outcome_log_loss | C - B (sign flipped: positive = better) | 0.043 | (-0.148, 0.254) | 0.654 |
| risk_recall | C - B | 0.028 | (-0.083, 0.139) | 1.000 |
| prereg_quality | C - B | 0.050 | (-0.014, 0.112) | 0.188 |

C versus B equivalence on P1 (margin 0.1): 90% interval (-0.069, 0.174), equivalent: False.

Answer key: automated rule-based adjudication, not independent human adjudication. With 10 tasks the intervals are wide; the pilot checks the pipeline and gives a first effect-size estimate, not a confirmatory test.
