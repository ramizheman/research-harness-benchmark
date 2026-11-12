# EXP:APPA-047 | Live H2 trigger timing: remaining possessions window
- date: 2026-05-25
- date_basis: doc
- date_reliable: yes
- design: Live H2 trigger simulation _run_live_trigger_validation.py; cited only as mean remaining possessions in the paper-mapping table.
- hypothesis: Suppression can be detected live in H2 with enough possessions remaining to act.
- knowable_in_advance: unclear
- member_of: FAM:SF-APPA-047 {record=APPA-047; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- notes: Primary artifact live_trigger_report.md is outside this slice.
- prespecified: unknown
- produced: RES:APPA-047 {record=APPA-047; rule=record fields}
- project: Defensive Suppression
- related_as_recorded: APPA-040
- reported_in: PAPER:Detecting_Defensive_Suppression_published {record=APPA-047; rule=project field}
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\FINAL_NUMBERS_SHEET.md
- title: Live H2 trigger timing: remaining possessions window
- uses_dataset: DS:NBA_play_by_play_possessions_and_reconstructed_lineups {record=APPA-047; rule=keyword rule DATASET_RULES}
- uses_method: METH:simulation {record=APPA-047; rule=keyword rule METHOD_RULES}

# RES:APPA-047 | Result of APPA-047
- failure_evidence: Sheet records only the mean (~21); no distribution, hit rate, or comparison to a false-alarm rate in this file.
- failure_type: E_unclear
- primary_result: Mean 21 poss remaining.
- record_stratum: not_a_test
- record_substatus: descriptive
- verdict: descriptive
