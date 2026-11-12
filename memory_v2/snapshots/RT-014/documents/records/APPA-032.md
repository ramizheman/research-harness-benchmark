# EXP:APPA-032 | Execution conformance scoring ORL vs DET
- date: 2026-04-20
- date_basis: mtime
- date_issues: file modification time: upper bound only; 11 records share this modification date (possible bulk edit or sync)
- date_reliable: no
- design: One game, 2 offenses; leverage-weighted conformance scores.
- hypothesis: Measure how closely each team executed the recommended opener.
- knowable_in_advance: unclear
- member_of: FAM:SF-APPA-032 {record=APPA-032; rule=audit/study_family_review.csv or singleton}
- n_runs: 2
- notes: DET note says it 'nailed the high-leverage moves' while PULL_UP was +10.2pp over the recommendation.
- prespecified: no
- produced: RES:APPA-032 {record=APPA-032; rule=record fields}
- project: Strategy app
- related_as_recorded: APPA-033
- related_to: EXP:APPA-033 {direction=unknown (date intervals overlap); needs_review=yes; origin=related field; record=APPA-032; rule=date-ordered record link}
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\EXECUTION_CONFORMANCE_ORL_DET_v2.md
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\EXECUTION_CONFORMANCE_ORL_DET_v3.md
- title: Execution conformance scoring ORL vs DET
- uses_method: METH:matched_control {record=APPA-032; rule=keyword rule METHOD_RULES}

# RES:APPA-032 | Result of APPA-032
- failure_type: E_unclear
- power_info: 1 game
- primary_result: ORL avg leverage |d| 12.6pp, scores 86.3/87.4; DET 7.7pp, 82.3/92.3; DET matched opener #3.
- record_stratum: not_a_test
- record_substatus: descriptive
- verdict: descriptive
