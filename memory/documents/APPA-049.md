# APPA-049: Sequential pair premium and defensive aftershock (8/8 PTs)

- Project: Defensive Suppression
- Date: 2026-05-31 (doc)
- Topic: Defensive suppression and counter strategy (BEST/AVOID)
- Pre-specified: no
- Verdict: supported
- Failure type: D_positive
- Knowable in advance: no
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); NBA play-by-play possessions and reconstructed lineups; Playoff series outcomes
- Method tags: 
- Limitation tags: small sample
- Variable tags: PPP (points per possession)
- Paper: Detecting Defensive Suppression (published)

## Hypothesis
After the opponent runs play type X, the next offensive play type Y scores above Y's unconditional H2 baseline, and every PT has a defensive aftershock.

## Design
own_seq_ec; n=458,604 opp possessions; all-games vs playoffs split; premium = Y PPP after X vs Y H2 baseline.

## Result
A2 aftershock 8/8 PTs replicate all-games and playoffs (CUT +0.119 n=21,398 / PO +0.131 n=1,145 through TRANSITION +0.135 n=26,262 / +0.126 n=1,529). Top pair premiums: PUTBACK->TRANSITION +0.084 n=565; CUT->PULL_UP +0.065 n=2,620.

## Failure evidence
8/8 play types replicate in both all-games and playoffs.

## Power and reliability
n=458,604 opp possessions

## Related
APPA-050; APPA-053

## Notes
Team-level 1-2 punch table includes tiny-n cells (BKN n=16, CHI n=18) marked sig at |t|>=2.0.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\FINAL_NUMBERS_SHEET.md

## Finding status
supported in source; independent replication not recorded

## Related records (ids resolved to merged records)
APPA-050, APPA-053

## Same study family
SF07 (duplicate_records): APPS-037
shared aftershock CUT +0.119 n=21,398 and TRANSITION +0.135 n=26,262
