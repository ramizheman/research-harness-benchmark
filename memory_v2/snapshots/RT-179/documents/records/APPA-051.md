# EXP:APPA-051 | Season adapter profiles: BEST-share vs playoff winning
- date: 2026-06-19
- date_basis: doc
- date_reliable: yes
- design: 55-series, 4 seasons; team BEST%/AVOID% and Win% by series-direction.
- hypothesis: Teams that consistently run more BEST-tier counters across seasons win more playoff series-directions.
- knowable_in_advance: yes
- measures: VAR:play_type_share_mix {record=APPA-051; rule=keyword rule VARIABLE_RULES}
- measures: VAR:win_probability_series_outcome {record=APPA-051; rule=keyword rule VARIABLE_RULES}
- member_of: FAM:SF08 {record=APPA-051; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- notes: OKC called out as third-highest BEST share and 89% win rate; talent confound untested here.
- prespecified: no
- produced: RES:APPA-051 {record=APPA-051; rule=record fields}
- project: Defensive Suppression
- related_as_recorded: APPA-041
- related_to: EXP:APPA-041 {direction=unknown (date intervals overlap); needs_review=yes; origin=related field; record=APPA-051; rule=date-ordered record link}
- reported_in: PAPER:Detecting_Defensive_Suppression_published {record=APPA-051; rule=project field}
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\FINAL_NUMBERS_SHEET.md
- title: Season adapter profiles: BEST-share vs playoff winning
- uses_dataset: DS:Playoff_series_outcomes {record=APPA-051; rule=keyword rule DATASET_RULES}

# RES:APPA-051 | Result of APPA-051
- failure_evidence: Descriptive team table; no test. Alignment vs winning already n.s. at n=110 (APPA-041). ORL n=3 series-dirs.
- failure_type: A_unanswerable
- power_info: 55-series, 4 seasons
- primary_result: Top BEST-share: BOS 15.7%/AVOID 21.4% Win 70% (10 dirs, 4 seasons); LAL 15.5%/23.1% Win 50% (6); OKC 12.3%/18.6% Win 89% (9 dirs, 3 seasons). Chronic AVOID: ORL 8.5%/59.3% Win 0% (3 dirs, 3 seasons).
- record_stratum: untestable
- record_substatus: mechanism A_unanswerable with verdict inconclusive
- verdict: inconclusive
