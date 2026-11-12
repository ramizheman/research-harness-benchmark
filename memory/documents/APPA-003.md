# APPA-003: Within-game did_adapt toward SHOULD counters improves PPP

- Project: Team Adaptation
- Date: 2026-05-15 (mtime)
- Topic: Defensive suppression and counter strategy (BEST/AVOID)
- Pre-specified: no
- Verdict: artifact_found
- Failure type: C_artifact
- Knowable in advance: yes
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); Playoff series outcomes
- Method tags: 
- Limitation tags: selection or regression to the mean
- Variable tags: PPP (points per possession); play-type share / mix
- Paper: 

## Hypothesis
Offenses that shift toward the counter play types for the inferred opponent scheme gain PPP later in the game.

## Design
586 playoff game-team rows split into thirds; scheme inferred from early-third PT PPP vs season baseline; did_adapt if counter-PT share rises; compare early-to-late PPP delta.

## Result
531 rows with inferred scheme; 249 adapted (46.9%); adapters +0.0701 (n=239) vs non-adapters +0.0121 (n=269), advantage +0.0580 PPP; DROP +0.1001, SWITCH -0.0436, HELP +0.0450.

## Failure evidence
A1 falsification: no_signal cells (+0.1260) outperform adapters; selection on extreme early-third PPP causes mean reversion.

## Power and reliability
n=239 vs 269

## Related
APPA-001; APPA-002

## Notes
Doc calls this 'direct empirical support for the SHOULD logic'; later files in the same folder undercut it.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\did_adapt_within_game_findings.md

## Related records (ids resolved to merged records)
APPA-001, APPA-002

## Same study family
SF13 (repeat_runs_or_robustness): CHT-018, APPM-013
APPA-003 and CHT-018 share adapters +0.0701 vs +0.0121; CHT-018's first run (+0.0613, n=229) is APPM-013's playoff estimate | Verdicts differ: artifact_found vs supported. The later RTM falsification overturned the first run.
