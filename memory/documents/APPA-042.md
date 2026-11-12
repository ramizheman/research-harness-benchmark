# APPA-042: Suppression vs routing: defense reads play type not initiator

- Project: Defensive Suppression
- Date: 2026-06-22 (doc)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: partial
- Verdict: reversed
- Failure type: B_powered_null
- Knowable in advance: no
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions)
- Method tags: holdout, backtest or replay
- Limitation tags: 
- Variable tags: PPP (points per possession)
- Paper: Detecting Defensive Suppression (published)

## Hypothesis
The H2 PPP collapse after a trigger is initiator-specific (routing) rather than play-type suppression; swapping the primary initiator should recover efficiency.

## Design
RS 2025-26 holdout 2,779 triggers; same-player both-halves pairs; same vs swapped primary initiator; _test_same_vs_swap.py. Prevalence: 1,783/2,296 processed team-games (77.7%) or 72.5% vs full-season denominator.

## Result
Deck baseline drop 0.631 (H1 1.470 to H2 0.839, n=2,779). Same player both halves drop 0.643 (n=10,194 pairs). Same initiator 825 drop 0.575/0.600; swapped 1,732 drop 0.634/0.639; SWAP-SAME +0.039 p=0.002 d=0.12. 68% swap. Routing regret on BEST counter poss +0.116 PPP, 72.4% oracle wins, n=6,808 (sheet also cites +0.124).

## Failure evidence
Same-player drop 0.643 matches the play-type drop 0.631; swapping initiator does not recover (swap drop 0.639, replacement 1.093 vs demoted 0.789).

## Power and reliability
2,779 triggers; 825 same / 1,732 swap

## Related
APPA-036; APPA-046

## Notes
Doc verdict: kill routing-regret as an adaptation mechanism on suppressed H2 plays; keep routing regret on BEST counter possessions. Cite-now line says +0.124; related-behavioral table says +0.116.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\FINAL_NUMBERS_SHEET.md

## Related records (ids resolved to merged records)
APPA-036, APPA-046

## Same study family
SF06 (duplicate_records): PAP-041
shared 1,732 / 825 swap counts and drops 0.600 / 0.639 | Verdicts differ: reversed vs null.
