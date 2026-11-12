# APPA-044: Oracle player matchup specificity on BEST counters (Route step)

- Project: Defensive Suppression
- Date: 2026-06-22 (doc)
- Topic: Structural roles and influence
- Pre-specified: no
- Verdict: supported
- Failure type: D_positive
- Knowable in advance: no
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); NBA play-by-play possessions and reconstructed lineups
- Method tags: matched control
- Limitation tags: small sample
- Variable tags: 
- Paper: Detecting Defensive Suppression (published)

## Hypothesis
The oracle BEST player for a counter play type varies by opponent, not a single team identity.

## Design
_oracle_player_specificity.py; n=6,852 oracle BEST possessions; (off_team, play_type) cells.

## Result
64/78 (82%) (off, PT) cells have >1 oracle player across opponents; 19/78 dominated by one player (>=90%); median oracle-player entropy 0.928.

## Failure evidence
82% of cells vary the oracle player by opponent.

## Power and reliability
n=6,852 oracle BEST possessions; 78 cells

## Related
APPA-042; APPA-045

## Notes
Valid on counter plays only; routing on suppressed plays was rejected in APPA-042.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\FINAL_NUMBERS_SHEET.md

## Finding status
supported in source; independent replication not recorded

## Related records (ids resolved to merged records)
APPA-042, APPA-045
