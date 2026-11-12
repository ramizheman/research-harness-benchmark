# APPA-063: Holdout play-type rank validation (LAYER_AUDIT)

- Project: Strategy app
- Date: 2026-04-18 (mtime)
- Topic: Other / unclassified
- Pre-specified: partial
- Verdict: supported
- Failure type: C_artifact
- Knowable in advance: no
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); NBA play-by-play possessions and reconstructed lineups
- Method tags: holdout, backtest or replay; correlation
- Limitation tags: 
- Variable tags: PPP (points per possession)
- Paper: 

## Hypothesis
Pre-game PT PPP ranking from training data correlates with actual efficiency ranking in held-out games.

## Design
Train 523,517 possession sequences; 454 holdout games; 908 (game, team) rows; Spearman of predicted vs actual PT rank (PTs >=3 poss, >=4 common PTs); top-3 hit/lift; bottom-3 suppression.

## Result
Median rho +0.539 (IQR +0.245 to +0.750); 62.4% rho>0.4; 88.4% rho>0; 10.5% rho<0. Top-3 median hit 100%; >=2/3 hits 78.9%; median lift +0.4261 PPP; 90.8% positive lift. Bottom-3 median suppression 66.7%. MAE cited in later reports 0.0922 PPP.

## Failure evidence
Doc caveat: top-3 lift partly reflects league-wide high-efficiency PTs (CUT, PUTBACK, TRANSITION); 10.5% of rows the model misleads (rho<0).

## Power and reliability
908 game-team rows; 454 games

## Related
APPA-031; APPA-035

## Notes
This is the Spearman 0.54 recycled in generated TEAM_vs_TEAM reports. Team medians range NOP +0.727 to WAS +0.341.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\LAYER_AUDIT.md

## Finding status
supported in source; independent replication not recorded

## Related records (ids resolved to merged records)
APPA-031, APPA-035
