# EXP:APPS-044 | Clutch sequence-premium family (multiple windows)
- date: 2026-06-04
- date_basis: mtime
- date_issues: file modification time: upper bound only
- date_reliable: no
- design: Analysis A: team X then opp then star Y; premium vs star clutch baseline on Y. Windows last 5 min n>=25/30 and last 10 min n>=20/30. Analysis D is opp-suppression, separate.
- hypothesis: Star X->Y offensive sequences in clutch have stable premiums across last-5 / last-10 windows.
- knowable_in_advance: unclear
- member_of: FAM:SF-APPS-044 {record=APPS-044; rule=audit/study_family_review.csv or singleton}
- n_runs: 5
- notes: Family of window variants; conclusions do not stabilize so recorded as one descriptive family rather than separate supported findings.
- prespecified: no
- produced: RES:APPS-044 {record=APPS-044; rule=record fields}
- project: Strategy app
- related_as_recorded: APPS-035; APPS-038
- related_to: EXP:APPS-038 {direction=unknown (date intervals overlap); needs_review=yes; origin=related field; record=APPS-044; rule=date-ordered record link}
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\clutch_sequence_archetypes\clutch_sequence_premiums_CROSS_SCENARIO.md
- title: Clutch sequence-premium family (multiple windows)

# RES:APPS-044 | Result of APPS-044
- failure_evidence: Top cell changes with window/floor; many n~25-35; no pooled test or multiplicity correction.
- failure_type: E_unclear
- power_info: 29 cells last5 n>=25; 38 cells last10 n>=30
- primary_result: Last 5 n>=25: 18 pos / 11 neg of 29 cells; top S. Curry DRIVE->PULL_UP +0.426 n=28. Last 10 n>=30: 25 pos / 13 neg of 38; top A. Edwards PULL_UP->DRIVE +0.365 n=33. Headline #1 sequence is not stable across windows. No-floor table is dominated by n=1 cells.
- record_stratum: not_a_test
- record_substatus: descriptive
- verdict: descriptive
