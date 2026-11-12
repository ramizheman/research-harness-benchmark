# EXP:APPM-027 | Upset test: app-alignment vs game upsets
- date: 2026-06-19
- date_basis: mtime
- date_issues: file modification time: upper bound only
- date_reliable: no
- design: 2025-26: 13 upsets vs 30 non-upset wins; 2024-25: 17 vs 36; compare smart share.
- hypothesis: Upset winners ran more BEST + AVOID_OVERRIDE plays.
- knowable_in_advance: yes
- measures: VAR:play_type_share_mix {record=APPM-027; rule=keyword rule VARIABLE_RULES}
- measures: VAR:win_probability_series_outcome {record=APPM-027; rule=keyword rule VARIABLE_RULES}
- member_of: FAM:SF-APPM-027 {record=APPM-027; rule=audit/study_family_review.csv or singleton}
- n_runs: 2
- notes: Smart share includes outcome-defined AVOID_OVERRIDE.
- prespecified: no
- produced: RES:APPM-027 {record=APPM-027; rule=record fields}
- project: Strategy app
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\OVERNIGHT_SUMMARY.md
- title: Upset test: app-alignment vs game upsets
- uses_dataset: DS:Playoff_series_outcomes {record=APPM-027; rule=keyword rule DATASET_RULES}

# RES:APPM-027 | Result of APPM-027
- failure_evidence: Winner had higher smart share in only 50%/48% of upset games; n=13/17 upsets.
- failure_type: A_unanswerable
- power_info: n=13 and 17 upsets
- primary_result: Smart-share edge +0.0307 (winner higher in 50% of upsets); 2024-25 +0.0616 (48%).
- record_stratum: untestable
- record_substatus: mechanism A_unanswerable with verdict null
- verdict: null
