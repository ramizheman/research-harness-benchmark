# EXP:APPA-015 | A3 equilibrium vs actual significance test
- date: 2026-04-15
- date_basis: mtime
- date_issues: file modification time: upper bound only
- date_reliable: no
- design: Per-matchup A3 minus actual across 240 matchups; t-test.
- hypothesis: Matchup-aware equilibrium beats actual team behavior significantly across matchups.
- knowable_in_advance: unclear
- member_of: FAM:SF-APPA-015 {record=APPA-015; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- notes: t=2.24 with n=240 should give p about 0.026 two-sided, so the stated p and t disagree. A3 PPP is nearly constant per offense, e.g. OKC 1.356 against every opponent.
- prespecified: no
- produced: RES:APPA-015 {record=APPA-015; rule=record fields}
- project: Strategy app
- related_as_recorded: APPA-011
- related_to: EXP:APPA-011 {direction=unknown (date intervals overlap); needs_review=yes; origin=related field; record=APPA-015; rule=date-ordered record link}
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\ADVERSARIAL_REPORT_V7.md
- title: A3 equilibrium vs actual significance test
- uses_method: METH:matched_control {record=APPA-015; rule=keyword rule METHOD_RULES}

# RES:APPA-015 | Result of APPA-015
- failure_evidence: Doc reports p=0.064 not significant.
- failure_type: E_unclear
- power_info: n=240, SD 14.26 pts/100
- primary_result: A3 beats actual 138/240 (57.5%); weighted mean +2.06 pts/100; median +2.22; SD 14.26; t=2.24; p=0.0644.
- record_stratum: uncertain
- record_substatus: inadequately tested: verdict null, mechanism E_unclear
- verdict: null
