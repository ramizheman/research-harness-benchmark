# APPA-057: Double-suppression stacking (POST_UP then PUTBACK)

- Project: Defensive Suppression
- Date: 2026-05-31 (doc)
- Topic: Defensive suppression and counter strategy (BEST/AVOID)
- Pre-specified: no
- Verdict: null
- Failure type: B_powered_null
- Knowable in advance: no
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); NBA play-by-play possessions and reconstructed lineups
- Method tags: 
- Limitation tags: small sample
- Variable tags: PPP (points per possession)
- Paper: Detecting Defensive Suppression (published)

## Hypothesis
Opponent POST_UP then PUTBACK stacks additively against the next star possession.

## Design
League sequence opp POST_UP -> offense -> opp PUTBACK -> star next; vs each alone. Mitchell PUTBACK-by-opponent directional split.

## Result
Baseline 1.210 n=960,764. After PUTBACK only 1.097 d=-0.113 n=15,898. After POST_UP only 1.091 d=-0.119 n=76,329. Stacked 1.138 d=-0.071 n=1,047 vs additive prediction -0.232. Mitchell after PUTBACK 0.919 vs 1.252 (d=-0.333, n=95); 8/13 teams below baseline n>=5, spread 1.200 PPP.

## Failure evidence
Stacked suppression -0.071 is less than either alone and far below additive -0.232 (n=1,047).

## Power and reliability
n=1,047 stacked; 15,898 / 76,329 singles

## Related
APPA-054; APPA-050

## Notes
Shared-pathway interpretation: offense adjusts after the first disruption.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\FINAL_NUMBERS_SHEET.md

## Related records (ids resolved to merged records)
APPA-054, APPA-050

## Same study family
SF09 (duplicate_records): APPS-042
shared 0.113 / 0.119 / 0.232 and n=15,898 / 76,329 | Verdicts differ: null vs inconclusive.
