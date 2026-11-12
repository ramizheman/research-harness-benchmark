# Experiment cross_model_v1

Tasks: 10. Conditions: A, B, C. Seeds: [1, 2, 3]. Models: openrouter:openai/gpt-oss-20b, openrouter:anthropic/claude-haiku-5.5.

## Summary by condition

| metric | A | B | C |
|---|---|---|---|
| runs | 60 | 60 | 60 |
| valid_outputs | 53 | 58 | 50 |
| P1_balanced_flag_accuracy | 0.567 | 0.547 | 0.618 |
| testability_auc | 0.613 | 0.665 | 0.718 |
| testability_brier | 0.328 | 0.377 | 0.352 |
| outcome_log_loss | 1.856 | 1.652 | 1.739 |
| risk_recall | 0.688 | 0.722 | 0.641 |
| prereg_quality | 0.881 | 0.895 | 0.890 |
| prior_work_recognized | 0.000 | 0.500 | 0.625 |
| false_prior_claim | n/a | 0.391 | 0.500 |
| proposal_max_similarity | 0.162 | 0.176 | 0.185 |
| input_tokens | 4278.962 | 6210.086 | 6456.700 |
| output_tokens | 3183.094 | 4454.983 | 4519.060 |
| n_tool_calls | 1.000 | 1.017 | 1.000 |
| memory_tool_calls | 0.000 | 1.017 | 1.000 |
| cost_usd_total | 0.088 | 0.132 | 0.133 |
| retrieval_attempted_rate | 1.000 | 1.000 | 0.983 |
| retrieval_first_rate | 1.000 | 1.000 | 0.983 |
| retrieval_successful_rate | 0.000 | 0.167 | 0.183 |
| meaningfully_used_rate | 0.000 | 0.150 | 0.167 |
| fabricated_citations_total | 0 | 0 | 0 |
| status_claims_checked_total | 0 | 163 | 178 |
| representation_accuracy | n/a | 1.000 | 1.000 |
| retrieval_latency_mean_s | 0.000 | 0.004 | 0.005 |
| memory_tokens_carried_mean | 9.583 | 1267.083 | 1478.033 |
| repair_turns_total | 15 | 10 | 9 |
| gate_turns_total | 0 | 0 | 0 |
| parse_recoveries_total | 25 | 48 | 35 |
| stop_reasons | final | final | final; unparseable |
| preliminary_answers_total | 0 | 0 | 0 |
| correction_turns_total | 0 | 5 | 2 |
| initial_citation_problems_total | 0 | 6 | 2 |
| pre_n_fabricated_citations_total | 0 | 0 | 0 |

## Primary contrasts (P1, balanced flag accuracy; task-level bootstrap and sign-flip test; Holm across contrasts)

| contrast | tasks | mean difference | 95% interval | p | p (Holm) |
|---|---|---|---|---|---|
| B - A | 10 | -0.028 | (-0.250, 0.236) | 0.906 | 1.000 |
| C - A | 10 | 0.017 | (-0.181, 0.229) | 0.906 | 1.000 |
| C - B | 10 | 0.044 | (-0.085, 0.174) | 0.555 | 1.000 |

## Secondary contrasts (not corrected; descriptive)

| metric | contrast | mean difference | 95% interval | p |
|---|---|---|---|---|
| testability_brier | B - A (sign flipped: positive = better) | -0.052 | (-0.141, 0.033) | 0.293 |
| outcome_log_loss | B - A (sign flipped: positive = better) | 0.196 | (-0.043, 0.464) | 0.203 |
| risk_recall | B - A | 0.056 | (0.000, 0.111) | 0.500 |
| prereg_quality | B - A | 0.057 | (0.005, 0.111) | 0.086 |
| testability_brier | C - A (sign flipped: positive = better) | -0.012 | (-0.089, 0.066) | 0.775 |
| outcome_log_loss | C - A (sign flipped: positive = better) | 0.058 | (-0.210, 0.360) | 0.715 |
| risk_recall | C - A | -0.019 | (-0.100, 0.042) | 1.000 |
| prereg_quality | C - A | -0.000 | (-0.073, 0.079) | 0.990 |
| testability_brier | C - B (sign flipped: positive = better) | 0.040 | (-0.008, 0.092) | 0.176 |
| outcome_log_loss | C - B (sign flipped: positive = better) | -0.138 | (-0.240, -0.030) | 0.041 |
| risk_recall | C - B | -0.075 | (-0.156, 0.014) | 0.250 |
| prereg_quality | C - B | -0.058 | (-0.119, 0.001) | 0.117 |

C versus B equivalence on P1 (margin 0.1): 90% interval (-0.065, 0.156), equivalent: False.

Answer key: automated rule-based adjudication, not independent human adjudication. With 10 tasks the intervals are wide; the pilot checks the pipeline and gives a first effect-size estimate, not a confirmatory test.
