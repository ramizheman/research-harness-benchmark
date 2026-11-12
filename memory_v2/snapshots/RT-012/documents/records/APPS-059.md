# EXP:APPS-059 | Sequence-memory horizon test (per-lag vs aggregated window)
- date: 2026-06-13
- date_basis: mtime
- date_issues: file modification time: upper bound only
- date_reliable: no
- design: 1024980 possessions with >=8 priors; TRAIN 22-24, VAL 24-25, TEST 2025-26. Per-lag vs aggregated window; GBT/logit/ridge.
- hypothesis: Increasing prior-possession history changes the opponent's next-possession outcome after controlling for game state.
- knowable_in_advance: unclear
- measures: VAR:win_probability_series_outcome {record=APPS-059; rule=keyword rule VARIABLE_RULES}
- member_of: FAM:SF-APPS-059 {record=APPS-059; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- notes: Aggregated-window decline was dilution of lag-1, not absence of memory.
- prespecified: partial
- produced: RES:APPS-059 {record=APPS-059; rule=record fields}
- project: Strategy app
- related_as_recorded: APPS-070; APPS-080
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\sequence_memory\output\sequence_memory_report.md
- title: Sequence-memory horizon test (per-lag vs aggregated window)
- uses_dataset: DS:NBA_play_by_play_possessions_and_reconstructed_lineups {record=APPS-059; rule=keyword rule DATASET_RULES}
- uses_method: METH:regression {record=APPS-059; rule=keyword rule METHOD_RULES}
- uses_method: METH:ridge_or_RAPM_ratings {record=APPS-059; rule=keyword rule METHOD_RULES}

# RES:APPS-059 | Result of APPS-059
- failure_evidence: Short-memory horizon is stable OOS; almost all gain is lag-1, plateau by lag 4. Absolute AUC still only ~0.591.
- failure_type: D_positive
- power_info: n=1,024,980 possessions; time-split test 2025-26
- primary_result: Per-lag GBT AUC N=0 0.5621 -> N=1 0.5863 (d+0.0242) -> N=3 0.5907 -> N=8 0.5911. R2 0.0051 -> 0.0133. Aggregated window declines after N=1 (AUC 0.5868 -> 0.5687 at N=8). Effective horizon ~2-3 possessions.
- record_stratum: supported
- record_substatus: mechanism D_positive
- verdict: supported
