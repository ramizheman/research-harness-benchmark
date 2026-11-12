# APPA-014: A4 sequence-context modifiers vs A3

- Project: Strategy app
- Date: 2026-04-15 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: null
- Failure type: C_artifact
- Knowable in advance: unclear
- Runs: 2
- Dataset tags: 
- Method tags: matched control
- Limitation tags: 
- Variable tags: PPP (points per possession); play-type share / mix; win probability / series outcome
- Paper: 

## Hypothesis
Previous-outcome and repetition modifiers lift equilibrium PPP and diversify mixes.

## Design
240 matchups; same equilibrium framework.

## Result
A4 +2.06 vs A3 +2.06; -0.00 pts/100; A4 beats A3 14/240; sample equilibrium mixes identical to A3.

## Failure evidence
Identical mixes and exactly 0.0000 deltas suggest the modifiers had no effect (possibly inert in code), not a tested null.

## Power and reliability
240 matchups

## Related
APPA-011

## Notes
V6 and V7 report the same headline.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\ADVERSARIAL_REPORT_V6.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\ADVERSARIAL_REPORT_V7.md

## Related records (ids resolved to merged records)
APPA-011
