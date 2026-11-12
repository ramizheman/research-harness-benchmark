# EXP:APPS-029 | Live Tab-2 trigger timing, 25 series 2025-26
- date: 2026-05-28
- date_basis: mtime
- date_issues: file modification time: upper bound only
- date_reliable: no
- design: Same Tab 2 logic as APPS-028; 228 unique triggers; AVOID_OVERRIDE rule added.
- hypothesis: Same live-trigger rest-of-game test on 25 2025-26 playoff series.
- knowable_in_advance: unclear
- member_of: FAM:SF04 {record=APPS-029; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- notes: Different conclusion from the 10-series live replay; n_runs kept separate because MW went from p=0.074 to p=0.0.
- prespecified: no
- produced: RES:APPS-029 {record=APPS-029; rule=record fields}
- project: Strategy app
- related_as_recorded: APPS-028
- related_to: EXP:CHT-038 {direction=unknown (date intervals overlap); needs_review=yes; origin=repeat-run family SF04; record=APPS-029; rule=date-ordered record link}
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\live_trigger_validation\live_trigger_report_seasons_25_26_clean.md
- title: Live Tab-2 trigger timing, 25 series 2025-26
- uses_dataset: DS:Playoff_series_outcomes {record=APPS-029; rule=keyword rule DATASET_RULES}
- uses_method: METH:correlation {record=APPS-029; rule=keyword rule METHOD_RULES}

# RES:APPS-029 | Result of APPS-029
- failure_evidence: BEST vs AVOID ROG PPP confirmed (p=0.0) and Spearman significant; timing still 100% actionable.
- failure_type: D_positive
- power_info: 557 counter obs, 228 triggers
- primary_result: 228 triggers, 100% actionable, mean remaining 21.0. Spearman rho=-0.2066, p=1e-06, n=557. MW BEST 1.263 (n=57) vs AVOID 0.783 (n=110), p=0.0. Early BEST-AVOID gap 0.701 vs late 0.415.
- record_stratum: supported
- record_substatus: mechanism D_positive
- verdict: supported
