# APPS-037: Sequential possession premium: defensive aftershock by play type

- Project: Strategy app
- Date: 2026-05-31 (doc)
- Topic: Defensive suppression and counter strategy (BEST/AVOID)
- Pre-specified: no
- Verdict: descriptive
- Failure type: E_unclear
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); NBA play-by-play possessions and reconstructed lineups; Playoff series outcomes
- Method tags: 
- Limitation tags: small sample
- Variable tags: PPP (points per possession)
- Paper: 

## Hypothesis
Opponent next-possession PPP is suppressed (positive aftershock) after the offense runs play type X, and this replicates RS+PO vs playoffs.

## Design
All games H2 sequential pairs. Own-next baseline 0.975 PPP (n=18943); opponent-next baseline 1.206 (n=458604). Aftershock = opp baseline - opp next PPP after X succeeds.

## Result
All-games aftershock after success: CUT +0.119 (n=21398), DRIVE +0.123 (57621), PNR +0.127 (51194), POST_UP +0.128 (20619), PULL_UP +0.132 (26060), PUTBACK +0.130 (5888), SPOT_UP +0.128 (43857), TRANSITION +0.135 (26262). All 8 replicate in playoffs. Own-next A1 treated as exploratory (~4% of pairs).

## Failure evidence
Large-n aftershock is uniformly positive across PTs (opponent scores ~1.07-1.09 vs baseline 1.206) so it may be a generic dead-ball/score effect rather than PT-specific disruption.

## Power and reliability
opp-next n=458604; per-PT success n=5.9k-57.6k

## Related
APPS-053; APPS-054

## Notes
Sign convention here (positive aftershock = opponent scores LESS) is opposite of the 52-series net-swing table where DRIVE/POST_UP have negative net swing.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\sequential_premium\sequential_premium_report.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\sequential_premium_run.log

## Related records (ids resolved to merged records)
APPA-001, APPA-005

## Same study family
SF07 (duplicate_records): APPA-049
shared aftershock CUT +0.119 n=21,398 and TRANSITION +0.135 n=26,262
