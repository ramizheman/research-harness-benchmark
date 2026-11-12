# EXP:APPA-035 | Relative-structure single-game validation BOS vs OKC
- date: 2026-04-17
- date_basis: mtime
- date_issues: file modification time: upper bound only; 12 records share this modification date (possible bulk edit or sync)
- date_reliable: no
- design: One holdout game 0022400946; Spearman of predicted vs actual PT PPP (PTs >=3 poss); top-3/bottom-3 hits.
- hypothesis: Model's top-ranked play types score above team average in a held-out game.
- knowable_in_advance: yes
- measures: VAR:PPP_points_per_possession {record=APPA-035; rule=keyword rule VARIABLE_RULES}
- member_of: FAM:SF-APPA-035 {record=APPA-035; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- prespecified: partial
- produced: RES:APPA-035 {record=APPA-035; rule=record fields}
- project: Strategy app
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\HISTORICAL_VALIDATION_BOS_OKC.md
- title: Relative-structure single-game validation BOS vs OKC
- uses_dataset: DS:Play_type_initiation_records_Neo4j_INITIATED_edges_play_type_possessions {record=APPA-035; rule=keyword rule DATASET_RULES}
- uses_method: METH:correlation {record=APPA-035; rule=keyword rule METHOD_RULES}
- uses_method: METH:holdout_backtest_or_replay {record=APPA-035; rule=keyword rule METHOD_RULES}

# RES:APPA-035 | Result of APPA-035
- failure_evidence: One game; 5-6 PTs per team with 4-35 possessions.
- failure_type: A_unanswerable
- power_info: 1 game
- primary_result: BOS rho 0.200, top-3 n/a, bottom-3 1/3; OKC rho 0.543, top-3 2/2, lift +0.308, bottom-3 1/3.
- record_stratum: untestable
- record_substatus: mechanism A_unanswerable with verdict inconclusive
- verdict: inconclusive
