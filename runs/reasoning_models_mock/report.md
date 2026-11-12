# Experiment reasoning_models_mock

**MOCK RUN.** Every output was produced by the scripted mock client. The numbers test the pipeline only and carry no information about memory or models.

Tasks: 10. Conditions: A, B, C. Seeds: [1, 2, 3]. Models: mock:anthropic/claude-sonnet-5.5, mock:deepseek/deepseek-v4-pro.

## Summary by condition

| metric | A | B | C |
|---|---|---|---|
| runs | 60 | 60 | 60 |
| valid_outputs | 60 | 60 | 60 |
| P1_balanced_flag_accuracy | 0.500 | 0.500 | 0.500 |
| testability_auc | 0.142 | 0.142 | 0.142 |
| testability_brier | 0.259 | 0.259 | 0.259 |
| outcome_log_loss | 1.656 | 1.656 | 1.656 |
| risk_recall | 0.083 | 0.083 | 0.083 |
| prereg_quality | 1.000 | 1.000 | 1.000 |
| prior_work_recognized | 0.000 | 1.000 | 1.000 |
| false_prior_claim | n/a | 1.000 | 1.000 |
| proposal_max_similarity | 0.141 | 0.141 | 0.141 |
| input_tokens | 2907.100 | 7616.700 | 7368.800 |
| output_tokens | 399.033 | 762.900 | 691.467 |
| n_tool_calls | 1.000 | 1.000 | 1.000 |
| memory_tool_calls | 0.000 | 1.000 | 1.000 |
| cost_usd_total | 0.000 | 0.000 | 0.000 |
| retrieval_attempted_rate | 1.000 | 1.000 | 1.000 |
| retrieval_first_rate | 1.000 | 1.000 | 1.000 |
| retrieval_successful_rate | 0.000 | 0.100 | 0.100 |
| meaningfully_used_rate | 0.000 | 0.000 | 0.000 |
| fabricated_citations_total | 0 | 0 | 0 |
| status_claims_checked_total | 0 | 24 | 48 |
| representation_accuracy | n/a | 1.000 | 1.000 |
| retrieval_latency_mean_s | 0.000 | 0.002 | 0.003 |
| memory_tokens_carried_mean | 8.000 | 2252.900 | 2452.800 |
| repair_turns_total | 0 | 0 | 0 |
| gate_turns_total | 0 | 0 | 0 |
| parse_recoveries_total | 0 | 0 | 0 |
| stop_reasons | final | final | final |
| preliminary_answers_total | 0 | 0 | 0 |
| correction_turns_total | 0 | 60 | 48 |
| initial_citation_problems_total | 0 | 60 | 48 |
| pre_n_fabricated_citations_total | 0 | 0 | 0 |

## Primary contrasts (P1, balanced flag accuracy; task-level bootstrap and sign-flip test; Holm across contrasts)

| contrast | tasks | mean difference | 95% interval | p | p (Holm) |
|---|---|---|---|---|---|
| B - A | 10 | 0.000 | (0.000, 0.000) | 1.000 | 1.000 |
| C - A | 10 | 0.000 | (0.000, 0.000) | 1.000 | 1.000 |
| C - B | 10 | 0.000 | (0.000, 0.000) | 1.000 | 1.000 |

## Secondary contrasts (not corrected; descriptive)

| metric | contrast | mean difference | 95% interval | p |
|---|---|---|---|---|
| testability_brier | B - A (sign flipped: positive = better) | 0.000 | (0.000, 0.000) | 1.000 |
| outcome_log_loss | B - A (sign flipped: positive = better) | 0.000 | (0.000, 0.000) | 1.000 |
| risk_recall | B - A | 0.000 | (0.000, 0.000) | 1.000 |
| prereg_quality | B - A | 0.000 | (0.000, 0.000) | 1.000 |
| testability_brier | C - A (sign flipped: positive = better) | 0.000 | (0.000, 0.000) | 1.000 |
| outcome_log_loss | C - A (sign flipped: positive = better) | 0.000 | (0.000, 0.000) | 1.000 |
| risk_recall | C - A | 0.000 | (0.000, 0.000) | 1.000 |
| prereg_quality | C - A | 0.000 | (0.000, 0.000) | 1.000 |
| testability_brier | C - B (sign flipped: positive = better) | 0.000 | (0.000, 0.000) | 1.000 |
| outcome_log_loss | C - B (sign flipped: positive = better) | 0.000 | (0.000, 0.000) | 1.000 |
| risk_recall | C - B | 0.000 | (0.000, 0.000) | 1.000 |
| prereg_quality | C - B | 0.000 | (0.000, 0.000) | 1.000 |

C versus B equivalence on P1 (margin 0.1): 90% interval (0.000, 0.000), equivalent: True.

Answer key: automated rule-based adjudication, not independent human adjudication. With 10 tasks the intervals are wide; the pilot checks the pipeline and gives a first effect-size estimate, not a confirmatory test.
