# EXP:APPA-068 | Game retrospective template preview OKC vs PHX (unpopulated)
- date: 2026-04-19
- date_basis: mtime
- date_issues: file modification time: upper bound only
- date_reliable: no
- design: Template for three temporal windows; intended to use ObservedGameStats and MatchupState. Train sequences listed as 0.
- hypothesis: Pre-game vs halftime vs post-game pipeline runs on OKC-PHX Game 1 can be compared to observed stats.
- knowable_in_advance: yes
- measures: VAR:three_point_attempts_or_luck {record=APPA-068; rule=keyword rule VARIABLE_RULES}
- member_of: FAM:SF-APPA-068 {record=APPA-068; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- notes: Placeholder preview, not a completed retrospective.
- prespecified: unknown
- produced: RES:APPA-068 {record=APPA-068; rule=record fields}
- project: Strategy app
- related_as_recorded: APPA-063
- related_to: EXP:APPA-063 {direction=unknown (date intervals overlap); needs_review=yes; origin=related field; record=APPA-068; rule=date-ordered record link}
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\GAME_RETROSPECTIVE_TEMPLATE_PREVIEW.md
- title: Game retrospective template preview OKC vs PHX (unpopulated)
- uses_method: METH:correlation {record=APPA-068; rule=keyword rule METHOD_RULES}
- uses_method: METH:holdout_backtest_or_replay {record=APPA-068; rule=keyword rule METHOD_RULES}
- uses_method: METH:matched_control {record=APPA-068; rule=keyword rule METHOD_RULES}

# RES:APPA-068 | Result of APPA-068
- failure_evidence: Pipeline runs were never supplied; 0 possession sequences in the train split field.
- failure_type: A_unanswerable
- primary_result: All sections [MODELED pending] / [DELTA pending] / [OBSERVED pending]. Spearman 0.54 and MAE 0.0922 are copied from the holdout rank study, not computed here.
- record_stratum: untestable
- record_substatus: mechanism A_unanswerable with verdict abandoned
- verdict: abandoned
