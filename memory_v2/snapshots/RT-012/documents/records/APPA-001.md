# EXP:APPA-001 | A1 adaptation falsification: asymmetry, confidence and carryover tests
- also_recorded_as: APPS-053
- date: 2026-05-16
- date_basis: mtime
- date_issues: file modification time: upper bound only
- date_reliable: no
- design: Playoff possessions only; game-team cells bucketed adapter/neutral/no_signal/wrong_way; early-to-late third PPP deltas; 430 consecutive (N, N+1) series pairs; one-sided Welch and Mann-Whitney tests.
- hypothesis: If the A1 adapter PPP lift is real coverage response, wrong-way teams should do worse than no-signal teams, the gap should widen with scheme-vote confidence, and adapting in Game N should carry over to Game N+1.
- knowable_in_advance: yes
- measures: VAR:PPP_points_per_possession {record=APPA-001; rule=keyword rule VARIABLE_RULES}
- member_of: FAM:SF-APPA-001 {record=APPA-001; rule=audit/study_family_review.csv or singleton}
- motivates: FOLLOW:APPA-001 {needs_review=yes; record=APPA-001; rule=text pattern motivate/follow-up/next step}
- n_runs: 1
- notes: Scheme labels are only assigned when early-third PT PPP is >=10% hot/cold, which mechanically builds in mean reversion; this selection was knowable from the labeling rule before outcomes.
- prespecified: partial
- produced: RES:APPA-001 {record=APPA-001; rule=record fields}
- project: Team Adaptation
- related_as_recorded: APPA-002; APPA-003
- related_to: EXP:APPA-002 {direction=unknown (date intervals overlap); needs_review=yes; origin=related field; record=APPA-001; rule=date-ordered record link}
- related_to: EXP:APPA-003 {direction=unknown (date intervals overlap); needs_review=yes; origin=related field; record=APPA-001; rule=date-ordered record link}
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\A1_FALSIFICATION_findings.md
- title: A1 adaptation falsification: asymmetry, confidence and carryover tests
- uses_dataset: DS:NBA_play_by_play_possessions_and_reconstructed_lineups {record=APPA-001; rule=keyword rule DATASET_RULES}
- uses_dataset: DS:Playoff_series_outcomes {record=APPA-001; rule=keyword rule DATASET_RULES}

# FOLLOW:APPA-001 | Follow-on candidate from APPA-001
- status: candidate from text pattern; not curated
- text: Scheme labels are only assigned when early-third PT PPP is >=10% hot/cold, which mechanically builds in mean reversion; this selection was knowable from the labeling rule before outcomes.

# RES:APPA-001 | Result of APPA-001
- failure_evidence: no_signal bucket (+0.1260) beats adapters (+0.0667); gap does not widen with confidence; carryover p=0.84; follow-up showed buckets selected on extreme early-third PPP (regression to mean).
- failure_type: C_artifact
- power_info: n=205/50/57/274 cells; 430 pairs
- primary_result: T1 dPPP: adapter +0.0667 (n=205), neutral +0.0248 (n=50), no_signal +0.1260 (n=57), wrong_way +0.0111 (n=274). T2: adapter minus no-signal -0.0361 (1 vote), -0.1170 (2 votes). T3 next-game PPP Welch t=-1.003, p=0.842; MW p=0.863; counter-carry Welch t=-2.163, p=0.985.
- record_stratum: artifact
- record_substatus: mechanism C_artifact with verdict failed_gate
- verdict: failed_gate
