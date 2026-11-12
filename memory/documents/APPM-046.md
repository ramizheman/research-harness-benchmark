# APPM-046: Matchup app reports TEAM_vs_TEAM (M-Z)

- Project: Strategy app
- Date: 2026-04-19 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: descriptive
- Failure type: E_unclear
- Knowable in advance: unclear
- Runs: 62
- Dataset tags: 
- Method tags: matched control; holdout, backtest or replay; correlation
- Limitation tags: 
- Variable tags: PPP (points per possession); win probability / series outcome
- Paper: 

## Hypothesis
(App output) pregame matchup reports.

## Design
62 generated reports (MEM 1, MIN 7, NYK 4, OKC 1, ORL 19, PHI 8, PHX 7, POR 7, SAS 1, TOR 7). Sample opened: MIN vs DEN has modeled PPP and scheme-stress numbers but no post-game outcome check.

## Result
MIN vs DEN sample: modeled MIN 1.286 vs season-avg 1.131 (Delta +0.155); DEN 1.288 vs 1.185 (Delta +0.103); DEN projected to neutralize 0.2829 PPP of MIN 0.0191 PPP gain. Spearman 0.54 on 454 holdout games restated; no game-outcome evaluation in the report.

## Failure evidence
Generated coaching reports; no hypothesis tested against realized outcomes.

## Power and reliability


## Related
APPM-041

## Notes
Updated copy of APPM-041 after opening a sample. Confirmed app output (excluded as an evaluation unless it checks a prediction). PREGAME_* files are the same class.

## Sources
- C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\MIN_vs_DEN_20260422_215604.md
- C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\MEM_vs_POR_20260514_233535.md
- C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\ORL_vs_DET_20260425_131827.md
- C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\PHI_vs_BOS_20260422_212310.md
- C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\TOR_vs_CLE_20260422_220105.md
