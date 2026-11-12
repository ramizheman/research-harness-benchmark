# APPM-048: NYK vs PHI 2025-26 series retrospective: model vs observed

- Project: Strategy app
- Date: 2026-05-15 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: inconclusive
- Failure type: A_unanswerable
- Knowable in advance: yes
- Runs: 1
- Dataset tags: Playoff series outcomes
- Method tags: matched control; holdout, backtest or replay
- Limitation tags: small sample
- Variable tags: PPP (points per possession); play-type share / mix; win probability / series outcome
- Paper: 

## Hypothesis
Pre-game modeled PPP gap and favorite match the series outcome and observed PPP within 0.10.

## Design
One series, 4 games (0042500211-214), NYK swept 4-0. Compare pre-game model to series-aggregate and per-game PPP.

## Result
NYK modeled PPP 1.3240 vs observed 1.2487 (Delta -0.075, within 0.10 YES). PHI 1.2410 vs 1.0355 (Delta -0.205, within 0.10 NO). Predicted gap +0.0830 vs observed +0.2132 (same direction). NYK WP 84.0%; sweep 100%. Per-game NYK PPP 1.356 / 1.091 / 1.125 / 1.412. CUT share 6.0% + DRIVE 12.6% = 18.6% vs OTHER 28.4%.

## Failure evidence
n=1 series; PHI PPP miss of 0.205; favorite-correct on a 84% favorite is a weak test.

## Power and reliability
n=4 games / 1 series

## Related
APPA-004 DID-ADAPT NYK vs PHI; APPM-024 G1 retros

## Notes
Separate from the four G1 retros. Model recommended CUT+DRIVE; observed mix was OTHER-heavy.

## Sources
- C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\RETRO_NYK_vs_PHI_2526_series.md
- C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\_retro_nyk_phi_2526.py
- C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\NYK_vs_PHI_20260515_150445.md

## Related records (ids resolved to merged records)
APPA-004
