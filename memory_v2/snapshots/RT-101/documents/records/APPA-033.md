# EXP:APPA-033 | Opener recommendations vs personnel feasibility
- date: 2026-04-20
- date_basis: mtime
- date_issues: file modification time: upper bound only; 11 records share this modification date (possible bulk edit or sync)
- date_reliable: no
- design: 8 team-games from 4 playoff games; opener target share vs personnel capacity x1.25.
- hypothesis: Rank-1 openers are within what the top-8 rotation can sustain.
- knowable_in_advance: yes
- measures: VAR:play_type_share_mix {record=APPA-033; rule=keyword rule VARIABLE_RULES}
- member_of: FAM:SF32 {record=APPA-033; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- notes: Explains the degenerate CUT-heavy recommendations seen in eval reports.
- prespecified: no
- produced: RES:APPA-033 {record=APPA-033; rule=record fields}
- project: Strategy app
- related_as_recorded: APPA-018
- related_to: EXP:APPA-018 {direction=unknown (date intervals overlap); needs_review=yes; origin=related field; record=APPA-033; rule=date-ordered record link}
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\FEASIBILITY_VS_OPENERS.md
- title: Opener recommendations vs personnel feasibility
- uses_dataset: DS:Playoff_series_outcomes {record=APPA-033; rule=keyword rule DATASET_RULES}

# RES:APPA-033 | Result of APPA-033
- failure_evidence: Optimizer ignores personnel; CUT target 3-10x stretch ceiling in every team-game.
- failure_type: C_artifact
- power_info: 8 team-games
- primary_result: 8/8 rank-1 openers CUT-centered and INFEASIBLE; worst gaps +9.6 to +15.9pp; CUT target 14-18% vs ceiling 2-6%.
- record_stratum: artifact
- record_substatus: verdict artifact_found
- verdict: artifact_found
