# EXP:APPA-043 | Counter play-type matchup specificity (Rank step)
- date: 2026-06-22
- date_basis: doc
- date_reliable: yes
- design: RS holdout; _counter_specificity.py and _counter_matchup_specificity.py; entropy of BEST counters.
- hypothesis: Given the same defense, different offenses get different BEST counters, and knowing the suppressed PT reduces counter entropy.
- knowable_in_advance: unclear
- measures: VAR:play_type_share_mix {record=APPA-043; rule=keyword rule VARIABLE_RULES}
- member_of: FAM:SF-APPA-043 {record=APPA-043; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- notes: Supports Rank as partly matchup-informed; ~80% of BEST counters are still the generic best (W4).
- prespecified: no
- produced: RES:APPA-043 {record=APPA-043; rule=record fields}
- project: Defensive Suppression
- related_as_recorded: APPA-046
- related_to: EXP:APPA-046 {direction=unknown (date intervals overlap); needs_review=yes; origin=related field; record=APPA-043; rule=date-ordered record link}
- reported_in: PAPER:Detecting_Defensive_Suppression_published {record=APPA-043; rule=project field}
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\FINAL_NUMBERS_SHEET.md
- title: Counter play-type matchup specificity (Rank step)
- uses_dataset: DS:Play_type_initiation_records_Neo4j_INITIATED_edges_play_type_possessions {record=APPA-043; rule=keyword rule DATASET_RULES}
- uses_method: METH:holdout_backtest_or_replay {record=APPA-043; rule=keyword rule METHOD_RULES}
- uses_method: METH:matched_control {record=APPA-043; rule=keyword rule METHOD_RULES}

# RES:APPA-043 | Result of APPA-043
- failure_evidence: No inferential test on the entropy values; mixed identity vs matchup pattern across teams.
- failure_type: E_unclear
- primary_result: Median entropy 1.543 (mostly matchup-specific). Knowing suppressed PT reduces entropy -0.344 (within-PT 1.331). One offense vs different defenses mixed: BOS/MIA/OKC vary; LAL/TOR often one counter.
- record_stratum: not_a_test
- record_substatus: descriptive
- verdict: descriptive
