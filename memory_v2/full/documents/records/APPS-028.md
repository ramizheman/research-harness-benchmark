# EXP:APPS-028 | Live Tab-2 trigger timing, 10 series (rest-of-game BEST vs AVOID)
- date: 2026-05-28
- date_basis: mtime
- date_issues: file modification time: upper bound only
- date_reliable: no
- design: Possession-by-possession replay, 10 2025-26 series. Trigger: H2 PPP drop>=0.25, n>=10 (or n>=5 with eff_n>=300). Counter PPP measured after trigger, not full H2.
- hypothesis: Tab 2's live trigger fires with time to act, and rest-of-game PPP is higher on BEST than AVOID counters.
- knowable_in_advance: unclear
- measures: VAR:PPP_points_per_possession {record=APPS-028; rule=keyword rule VARIABLE_RULES}
- member_of: FAM:SF04 {record=APPS-028; rule=audit/study_family_review.csv or singleton}
- motivates: FOLLOW:APPS-028 {needs_review=yes; record=APPS-028; rule=text pattern motivate/follow-up/next step}
- n_runs: 1
- notes: Follow-up 25-series replay (APPS-029) confirms BEST vs AVOID.
- prespecified: no
- produced: RES:APPS-028 {record=APPS-028; rule=record fields}
- project: Strategy app
- related_as_recorded: APPS-029
- related_to: EXP:APPS-029 {direction=unknown (date intervals overlap); needs_review=yes; origin=related field; record=APPS-028; rule=date-ordered record link}
- related_to: EXP:CHT-038 {direction=unknown (date intervals overlap); needs_review=yes; origin=repeat-run family SF04; record=APPS-028; rule=date-ordered record link}
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\live_trigger_validation\live_trigger_report.md
- title: Live Tab-2 trigger timing, 10 series (rest-of-game BEST vs AVOID)
- uses_dataset: DS:NBA_play_by_play_possessions_and_reconstructed_lineups {record=APPS-028; rule=keyword rule DATASET_RULES}
- uses_dataset: DS:Playoff_series_outcomes {record=APPS-028; rule=keyword rule DATASET_RULES}
- uses_method: METH:correlation {record=APPS-028; rule=keyword rule METHOD_RULES}
- uses_method: METH:holdout_backtest_or_replay {record=APPS-028; rule=keyword rule METHOD_RULES}

# FOLLOW:APPS-028 | Follow-on candidate from APPS-028
- status: candidate from text pattern; not curated
- text: Follow-up 25-series replay (APPS-029) confirms BEST vs AVOID.

# RES:APPS-028 | Result of APPS-028
- failure_evidence: Timing is actionable (100% with >=5 remaining) but BEST vs AVOID ROG PPP p=0.073965 and Spearman p=0.456.
- failure_type: E_unclear
- power_info: 268 counter obs, 101 triggers; BEST n=30
- primary_result: 101 triggers; 100% actionable (>=5 H2 poss remaining); mean remaining 23.4. Spearman tier vs ROG PPP rho=-0.0457, p=0.45616, n=268. MW BEST 1.227 (n=30) vs AVOID 1.037 (n=95), p=0.073965 (not confirmed at 0.05). Early vs late BEST ROG 1.521 vs 1.182.
- record_stratum: uncertain
- record_substatus: inconclusive
- verdict: inconclusive
