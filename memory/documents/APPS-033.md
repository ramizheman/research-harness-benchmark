# APPS-033: INSUFF_EVIDENCE deep audit (post-orphan-fix)

- Project: Strategy app
- Date: 2026-06-19 (mtime)
- Topic: Play-type labeling and data quality
- Pre-specified: no
- Verdict: descriptive
- Failure type: E_unclear
- Knowable in advance: yes
- Runs: 1
- Dataset tags: 
- Method tags: 
- Limitation tags: 
- Variable tags: PPP (points per possession)
- Paper: 

## Hypothesis
INSUFF_EVIDENCE counter rows are recoverable missed tree branches rather than true no-history pairs.

## Design
1153 counter obs; 427 INSUFF (37.0%). Cause A wrong-src vs Cause B counter-absent. Cap/lift/per-src diagnostics.

## Result
CAUSE_A n=208 (48.7%, mean PPP 1.162); CAUSE_B n=219 (51.3%, mean 1.055). BEST-AVOID gap 0.620; MISSED_GOOD 1.148 vs AVOID 0.821 (+0.327). Expanding cap 25->50 recovers <=0 confirmed truncated pairs; ADAPT_LIFT_MIN filter 0 rows.

## Failure evidence
Audit of coverage, not an outcome test; 37% of counters still unranked.

## Power and reliability
427 INSUFF of 1153

## Related
APPS-019

## Notes
Highest-ROI model change identified as per-src_pt ranking (recover 208/427) with no new data.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\insuff_evidence_deep_audit.md

## Related records (ids resolved to merged records)
APPS-019
