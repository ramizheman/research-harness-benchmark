# APPS-084: Portability confirmatory: wiring-displacement signature travels

- Project: When a Hub Sits (Paper 2)
- Date: 2026-07-26 (mtime)
- Topic: Player absence and offensive reorganization
- Pre-specified: yes
- Verdict: supported
- Failure type: D_positive
- Knowable in advance: no
- Runs: 2
- Dataset tags: 
- Method tags: 
- Limitation tags: 
- Variable tags: three-point attempts or luck
- Paper: When a Hub Sits (manuscript)

## Hypothesis
A player's wiring-displacement signature is a portable trait (self_sim > decoy_sim at destination).

## Design
Gate movers=294 PASS. Confirmatory max_gap=0, n_perm=5000, dest_franchises=30.

## Result
median self_sim=+0.129 decoy_sim=+0.049; T1 median Delta=+0.0557 perm_p=0.0050; 173/294=0.5884 sign_test_p=2.872e-03; dest-fr CI [+0.0192,+0.0859]. All three decision-rule bars True. T1 CONFIRMED.

## Failure evidence
Delta>0, perm<0.01, CI excludes 0 at destination-franchise clustering.

## Power and reliability
n=294 movers, 30 dest franchises

## Related
APPS-080; APPS-087

## Notes
Connector follow-ups later argue connector *value* is relational even if the displacement signature travels.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\paper2_output\portability_gate_result.txt
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\paper2_output\portability_full_result.txt

## Finding status
supported in source; independent replication not recorded

## Related records (ids resolved to merged records)
APPS-080, APPS-087

## Follow-on candidate
candidate, needs curation (see Notes)

## Same study family
SF19 (duplicate_records): PAP-017
shared median Delta=+0.0557, CI [+0.0192, +0.0859], 173/294 | PAP-016 is the separate feasibility gate.
