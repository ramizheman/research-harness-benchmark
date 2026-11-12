# APPA-043: Counter play-type matchup specificity (Rank step)

- Project: Defensive Suppression
- Date: 2026-06-22 (doc)
- Topic: Defensive suppression and counter strategy (BEST/AVOID)
- Pre-specified: no
- Verdict: descriptive
- Failure type: E_unclear
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions)
- Method tags: matched control; holdout, backtest or replay
- Limitation tags: 
- Variable tags: play-type share / mix
- Paper: Detecting Defensive Suppression (published)

## Hypothesis
Given the same defense, different offenses get different BEST counters, and knowing the suppressed PT reduces counter entropy.

## Design
RS holdout; _counter_specificity.py and _counter_matchup_specificity.py; entropy of BEST counters.

## Result
Median entropy 1.543 (mostly matchup-specific). Knowing suppressed PT reduces entropy -0.344 (within-PT 1.331). One offense vs different defenses mixed: BOS/MIA/OKC vary; LAL/TOR often one counter.

## Failure evidence
No inferential test on the entropy values; mixed identity vs matchup pattern across teams.

## Power and reliability


## Related
APPA-046

## Notes
Supports Rank as partly matchup-informed; ~80% of BEST counters are still the generic best (W4).

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\FINAL_NUMBERS_SHEET.md

## Related records (ids resolved to merged records)
APPA-046
