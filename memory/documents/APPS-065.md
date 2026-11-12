# APPS-065: Brown-initiated possession -> Tatum next-possession ATT

- Project: Strategy app
- Date: 2026-06-13 (mtime)
- Topic: Structural roles and influence
- Pre-specified: partial
- Verdict: null
- Failure type: B_powered_null
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); NBA play-by-play possessions and reconstructed lineups
- Method tags: placebo or permutation test; bootstrap interval; matched control
- Limitation tags: 
- Variable tags: 
- Paper: 

## Hypothesis
A Jaylen Brown-initiated BOS possession raises Tatum's points on the next BOS possession (spillover/gravity).

## Design
Chain N=6992; treated=1173 control=5819. PSM 1:3 caliper 0.05; exact-match fallback; perm 800; placebo 200.

## Result
PSM ATT=-0.0165, bootstrap 95% CI [-0.0924,+0.0605]. Exact-match ATT=-0.0857. Stratified perm p=0.0275 on ATT=-0.0171. Placebo 95% [-0.0762,+0.0730]; real ATT inside. Playoffs ATT=+0.0485 CI[-0.1095,+0.2078].

## Failure evidence
PSM CI includes 0; ATT inside placebo range; not robustly >0. Perm p=0.0275 is on a near-zero negative ATT.

## Power and reliability
treated n=1173

## Related
APPS-066; APPS-075

## Notes
Verdict: NO ROBUST EFFECT, consistent with spillover/state-transition artifact.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\sequence_memory\output\brown_tatum_causal_report.txt
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\sequence_memory\brown_tatum_causal.py

## Related records (ids resolved to merged records)
APPS-066, APPS-075

## Same study family
SF30 (duplicate_records): CHT-030
shared PSM ATT -0.0165 / -0.017, bootstrap CI [-0.092, +0.061], perm p=0.028 | APPS-066 (placebo) stays separate.
