# APPA-064: G5 blog replay: LP opener vs realized mix SAS-OKC

- Project: Strategy app
- Date: 2026-05-26 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: inconclusive
- Failure type: A_unanswerable
- Knowable in advance: yes
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions)
- Method tags: matched control; holdout, backtest or replay
- Limitation tags: small sample
- Variable tags: play-type share / mix
- Paper: 

## Hypothesis
The LP-equilibrium opener (CUT) and AVOID (PNR) match realized efficiency in WCF Game 5 SAS @ OKC (0042500315).

## Design
One game scored post hoc against historical H2H baselines (replay uses PlayTypeInferrer + PNR proxy). Live blog is the in-game feed of the same game.

## Result
Final SAS 114-OKC 127. SAS CUT 9 poss 1.67 vs H2H 1.59 CORRECT; SAS PNR 22 poss 0.95 vs 0.94 MIXED (LP AVOID). OKC CUT 1 poss 2.00 vs 1.69 CORRECT but 1% mix vs plan. OKC PNR 19 poss 1.26 vs 1.11 (AVOID but above H2H). Live: both teams ~65-71% PULL_UP, CUT 1-5%.

## Failure evidence
One game; CUT opener was high-PPP on tiny volume (SAS n=9, OKC n=1) while both teams ran PULL_UP as the modal PT.

## Power and reliability
1 game; SAS 87 / OKC 82 callable poss

## Related
APPA-033; APPA-063

## Notes
Live blog has no post-game accuracy table; the scored assessment is only in G5_BLOG_REPLAY.md.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\G5_BLOG_REPLAY.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\LIVE_BLOG_SAS_OKC_G5.md

## Related records (ids resolved to merged records)
APPA-033, APPA-063
