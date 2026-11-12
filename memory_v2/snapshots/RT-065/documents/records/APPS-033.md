# EXP:APPS-033 | INSUFF_EVIDENCE deep audit (post-orphan-fix)
- date: 2026-06-19
- date_basis: mtime
- date_issues: file modification time: upper bound only
- date_reliable: no
- design: 1153 counter obs; 427 INSUFF (37.0%). Cause A wrong-src vs Cause B counter-absent. Cap/lift/per-src diagnostics.
- hypothesis: INSUFF_EVIDENCE counter rows are recoverable missed tree branches rather than true no-history pairs.
- knowable_in_advance: yes
- measures: VAR:PPP_points_per_possession {record=APPS-033; rule=keyword rule VARIABLE_RULES}
- member_of: FAM:SF-APPS-033 {record=APPS-033; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- notes: Highest-ROI model change identified as per-src_pt ranking (recover 208/427) with no new data.
- prespecified: no
- produced: RES:APPS-033 {record=APPS-033; rule=record fields}
- project: Strategy app
- related_as_recorded: APPS-019
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\insuff_evidence_deep_audit.md
- title: INSUFF_EVIDENCE deep audit (post-orphan-fix)

# RES:APPS-033 | Result of APPS-033
- failure_evidence: Audit of coverage, not an outcome test; 37% of counters still unranked.
- failure_type: E_unclear
- power_info: 427 INSUFF of 1153
- primary_result: CAUSE_A n=208 (48.7%, mean PPP 1.162); CAUSE_B n=219 (51.3%, mean 1.055). BEST-AVOID gap 0.620; MISSED_GOOD 1.148 vs AVOID 0.821 (+0.327). Expanding cap 25->50 recovers <=0 confirmed truncated pairs; ADAPT_LIFT_MIN filter 0 rows.
- record_stratum: not_a_test
- record_substatus: descriptive
- verdict: descriptive
