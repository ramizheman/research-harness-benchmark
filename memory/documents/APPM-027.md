# APPM-027: Upset test: app-alignment vs game upsets

- Project: Strategy app
- Date: 2026-06-19 (mtime)
- Topic: Defensive suppression and counter strategy (BEST/AVOID)
- Pre-specified: no
- Verdict: null
- Failure type: A_unanswerable
- Knowable in advance: yes
- Runs: 2
- Dataset tags: Playoff series outcomes
- Method tags: 
- Limitation tags: small sample
- Variable tags: play-type share / mix; win probability / series outcome
- Paper: 

## Hypothesis
Upset winners ran more BEST + AVOID_OVERRIDE plays.

## Design
2025-26: 13 upsets vs 30 non-upset wins; 2024-25: 17 vs 36; compare smart share.

## Result
Smart-share edge +0.0307 (winner higher in 50% of upsets); 2024-25 +0.0616 (48%).

## Failure evidence
Winner had higher smart share in only 50%/48% of upset games; n=13/17 upsets.

## Power and reliability
n=13 and 17 upsets

## Related


## Notes
Smart share includes outcome-defined AVOID_OVERRIDE.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\OVERNIGHT_SUMMARY.md
