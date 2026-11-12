# EXP:APPS-039 | Season adapter profiles (BEST-share consistency across seasons)
- date: 2026-05-31
- date_basis: doc
- date_reliable: yes
- design: BEST share of H2 counter possessions; teams with n>=2 seasons. Consistency=stdev of BEST share.
- extends: EXP:APPS-030 {direction=verified by dates; needs_review=no; origin=related field; record=APPS-039; rule=date-ordered record link}
- hypothesis: Teams' post-trigger BEST vs AVOID mix is a stable coaching signature across seasons.
- knowable_in_advance: unclear
- measures: VAR:play_type_share_mix {record=APPS-039; rule=keyword rule VARIABLE_RULES}
- member_of: FAM:SF08 {record=APPS-039; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- prespecified: no
- produced: RES:APPS-039 {record=APPS-039; rule=record fields}
- project: Strategy app
- related_as_recorded: APPS-030; APPS-027
- related_to: EXP:APPS-027 {direction=unknown (date intervals overlap); needs_review=yes; origin=related field; record=APPS-039; rule=date-ordered record link}
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\season_adapter_profiles\season_adapter_profiles_report.md
- title: Season adapter profiles (BEST-share consistency across seasons)
- uses_dataset: DS:NBA_play_by_play_possessions_and_reconstructed_lineups {record=APPS-039; rule=keyword rule DATASET_RULES}

# RES:APPS-039 | Result of APPS-039
- failure_evidence: No inferential test of stability vs noise; win% not identified with BEST share (IND 4.5% BEST, 71% win).
- failure_type: E_unclear
- power_info: 19 teams with n>=2 seasons
- primary_result: Top mean BEST share: BOS 15.7% (10 dirs, win 70%), LAL 15.5%, GSW 13.8%. Bottom: HOU 2.5%, MIL 3.5%, LAC 4.1%. DEN 4.9% BEST / 70.8% INSUFF yet 62% win. ORL AVOID share 59.3%, 0% win.
- record_stratum: not_a_test
- record_substatus: descriptive
- verdict: descriptive
