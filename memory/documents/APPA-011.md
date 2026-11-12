# APPA-011: Matchup-aware A3 vs team kernel A2 at equilibrium

- Project: Strategy app
- Date: 2026-04-15 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: reversed
- Failure type: E_unclear
- Knowable in advance: unclear
- Runs: 3
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions)
- Method tags: placebo or permutation test; matched control
- Limitation tags: 
- Variable tags: PPP (points per possession)
- Paper: 

## Hypothesis
Player-vs-defender matchup modeling (A3) improves equilibrium PPP over team-level A2.

## Design
Same 240 matchups; V2 coarse play types; V3 adds spatial sub-types; V3_SHUFFLED re-run (what was shuffled is not documented).

## Result
V2: A3 +2.50 vs A2 +1.16 pts/100, A3 beats A2 147/240. V3: A2 +8.84, A3 +2.06, A3-A2 -6.78, A3 beats A2 71/240. V3_SHUFFLED: A2 +8.61, A3 +1.59, -7.02.

## Failure evidence
Sign flips from +1.34 (V2) to -6.78 (V3) when spatial sub-types were added.

## Power and reliability
240 matchups

## Related
APPA-010; APPA-012

## Notes
V2 concluded 'MATCHUP MODEL HELPS'; V3 'UNDERPERFORMS'. Shuffled version gives similar numbers.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\ADVERSARIAL_REPORT_V2.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\ADVERSARIAL_REPORT_V3.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\ADVERSARIAL_REPORT_V3_SHUFFLED.md

## Related records (ids resolved to merged records)
APPA-010, APPA-012
