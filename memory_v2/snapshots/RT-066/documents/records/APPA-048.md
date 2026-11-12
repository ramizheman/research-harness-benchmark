# EXP:APPA-048 | Player-level BEST vs AVOID H2 PPP gaps (exploratory)
- date: 2026-05-31
- date_basis: doc
- date_reliable: yes
- design: 55-series graph; each player BEST-tier vs AVOID-tier H2 PPP; min 5 rows per tier; N=78 players.
- hypothesis: Players score more on BEST-ranked counters than AVOID-ranked counters in the 55-series playsheets.
- knowable_in_advance: yes
- measures: VAR:PPP_points_per_possession {record=APPA-048; rule=keyword rule VARIABLE_RULES}
- measures: VAR:play_type_share_mix {record=APPA-048; rule=keyword rule VARIABLE_RULES}
- member_of: FAM:SF-APPA-048 {record=APPA-048; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- notes: Exploratory; sheet says n is small for most players.
- prespecified: no
- produced: RES:APPA-048 {record=APPA-048; rule=record fields}
- project: Defensive Suppression
- related_as_recorded: APPA-036
- reported_in: PAPER:Detecting_Defensive_Suppression_published {record=APPA-048; rule=project field}
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\FINAL_NUMBERS_SHEET.md
- title: Player-level BEST vs AVOID H2 PPP gaps (exploratory)
- uses_dataset: DS:Playoff_series_outcomes {record=APPA-048; rule=keyword rule DATASET_RULES}

# RES:APPA-048 | Result of APPA-048
- failure_evidence: n is small for most players (single-game playsheets); no multiplicity or clustered test.
- failure_type: A_unanswerable
- power_info: 78 players; min 5 rows/tier
- primary_result: 78 players with >=5 BEST and >=5 AVOID rows. Top gaps D. Lively II +1.833 (n=6/6), M. Brogdon +1.831 (7/11); some reverse (N. Jokic -0.333 n=8/18; L. Doncic -0.190 n=6/14). Stars mixed (D. White +0.864 n=49/42; SGA +0.333 n=5/60).
- record_stratum: not_a_test
- record_substatus: descriptive
- verdict: descriptive
