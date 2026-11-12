# APPA-054: PUTBACK suppression mechanism: fatigue vs value

- Project: Defensive Suppression
- Date: 2026-05-31 (doc)
- Topic: Defensive suppression and counter strategy (BEST/AVOID)
- Pre-specified: no
- Verdict: supported
- Failure type: E_unclear
- Knowable in advance: yes
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); NBA play-by-play possessions and reconstructed lineups
- Method tags: 
- Limitation tags: small sample; insufficient exposure
- Variable tags: PPP (points per possession)
- Paper: Detecting Defensive Suppression (published)

## Hypothesis
PUTBACK suppresses the next star possession via fatigue (stronger in H2 and Q4), while PUTBACK itself remains high-value.

## Design
Four tests on PUTBACK-suppressed stars: H1 vs H2 delta, Q1 vs Q4, PUTBACK H2 PPP vs baseline, offense PPP after opp PUTBACK.

## Result
H1 delta -0.038 vs H2 -0.130 (22 stars, 3.4x). Q1 -0.009 vs Q4 -0.289 (11 stars; Q4 pooled n=34). PUTBACK H2 1.528 vs 1.217 (+0.311) n=8,614 vs 474,564. After opp PUTBACK offense 1.097 vs 1.210 (d=-0.113) n=15,898.

## Failure evidence
Q4 PUTBACK is sparse (34 pooled poss at n>=30; Mitchell n=34 drives the Q4 cell) even though the H2 vs H1 and aftershock tests are larger.

## Power and reliability
22 stars H1+H2; Q4 pooled n=34; 15,898 aftershock poss

## Related
APPA-050; APPA-055

## Notes
Sheet calls fatigue the primary driver; Q4 sparsity is knowable from the n>=30 gate.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\FINAL_NUMBERS_SHEET.md

## Finding status
supported in source; independent replication not recorded

## Related records (ids resolved to merged records)
APPA-050, APPA-055

## Also recorded as
APPS-040
