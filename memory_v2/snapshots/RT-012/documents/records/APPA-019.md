# EXP:APPA-019 | Usage-curve constrained optimizer (A2) vs baseline
- date: 2026-04-14
- date_basis: mtime
- date_issues: file modification time: upper bound only
- date_reliable: no
- design: Same 23,922 holdout possessions; per-possession and distribution-level evaluation.
- hypothesis: Diminishing-returns usage curves improve recommendations over static argmax and baseline.
- knowable_in_advance: no
- measures: VAR:play_type_share_mix {record=APPA-019; rule=keyword rule VARIABLE_RULES}
- member_of: FAM:SF-APPA-019 {record=APPA-019; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- notes: Doc labels -6.84 as an 'improvement'; number and wording disagree.
- prespecified: no
- produced: RES:APPA-019 {record=APPA-019; rule=record fields}
- project: Strategy app
- related_as_recorded: APPA-018
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\EVAL_REPORT_v3.md
- title: Usage-curve constrained optimizer (A2) vs baseline
- uses_dataset: DS:Box_score_and_traditional_stats {record=APPA-019; rule=keyword rule DATASET_RULES}
- uses_dataset: DS:NBA_play_by_play_possessions_and_reconstructed_lineups {record=APPA-019; rule=keyword rule DATASET_RULES}
- uses_method: METH:holdout_backtest_or_replay {record=APPA-019; rule=keyword rule METHOD_RULES}

# RES:APPA-019 | Result of APPA-019
- failure_evidence: -8.32 pts/100 vs baseline on 23,922 possessions.
- failure_type: B_powered_null
- power_info: 23,922 possessions
- primary_result: A2 -8.32 pts/100 vs baseline; A2 vs A -6.84; A2 outperforms baseline 47/240. Distribution: A2 mix +13.40 pts/100 vs actual (beats 217/240) but -24.85 vs B argmax.
- record_stratum: rejected
- record_substatus: verdict null, powered null with power information
- verdict: null
