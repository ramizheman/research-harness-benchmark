# APPA-050: Superstar sequential suppression: opponent play before the star

- Project: Defensive Suppression
- Date: 2026-05-30 (doc)
- Topic: Defensive suppression and counter strategy (BEST/AVOID)
- Pre-specified: no
- Verdict: descriptive
- Failure type: E_unclear
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); NBA play-by-play possessions and reconstructed lineups
- Method tags: 
- Limitation tags: 
- Variable tags: PPP (points per possession)
- Paper: Detecting Defensive Suppression (published)

## Hypothesis
A specific opponent play type on the preceding possession suppresses each star's next-possession PPP relative to that star's baseline.

## Design
Full graph RS+PO; 30 stars; min n=30 after the suppressor PT.

## Result
PUTBACK is top suppressor for 6+ stars (e.g. D. Mitchell 1.178 to 0.884, d=-0.294, n_after=95; B. Beal d=-0.345 n=32; C. Holmgren d=-0.222 n=52). Other tops: TRANSITION (A. Davis -0.058), POST_UP (N. Jokic -0.075), PULL_UP (A. Edwards -0.043).

## Failure evidence
No multiplicity correction; n_after is 32-95 for several PUTBACK cells vs thousands of baseline possessions.

## Power and reliability
30 stars; min n_after=30

## Related
APPA-054; APPA-055

## Notes
PUTBACK as a league-wide suppressor is the claim later tested as a mechanism in APPA-054/055.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\FINAL_NUMBERS_SHEET.md

## Related records (ids resolved to merged records)
APPA-054, APPA-055
