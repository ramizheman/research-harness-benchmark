# APPA-046: Adaptation vs generic counter (W4)

- Project: Defensive Suppression
- Date: 2026-06-22 (doc)
- Topic: Defensive suppression and counter strategy (BEST/AVOID)
- Pre-specified: no
- Verdict: supported
- Failure type: D_positive
- Knowable in advance: no
- Runs: 1
- Dataset tags: 
- Method tags: 
- Limitation tags: small sample
- Variable tags: PPP (points per possession)
- Paper: Detecting Defensive Suppression (published)

## Hypothesis
BEST-tier counters are suppression-specific rather than the team's generic best available play.

## Design
_adaptation_vs_generic.py; n=1,539 RS triggers with BEST tier + viable blended PPP (55.4% of 2,779).

## Result
BEST == generic best 78.3%; suppression-specific 21.7%. Defense suppressed generic-best 4.7% (73); then specific 39.7%. When supp != generic, still picks generic 79.2%. (off,def) counter changes by what was suppressed 48.8% (190/389). PNR adapt 28.3% n=428; PULL_UP 28.5% n=291. True INSUFF (no valid counter) 0/11,087 full-graph triggers.

## Failure evidence
78.3% of ranked BEST counters are the generic best available; Rank adds value in ~20-22%, 39.7% when defense took the team's best.

## Power and reliability
n=1,539 W4 triggers; 1,466 (95.3%) had a better option already

## Related
APPA-041; APPA-042

## Notes
Deck '80%' and '1,600 triggers' should be 78.3% and 1,539. Pivot remains counterfactual: 93% do not pivot. Drop magnitude does not predict smarter counters (~22% flat).

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\FINAL_NUMBERS_SHEET.md

## Finding status
supported in source; independent replication not recorded

## Related records (ids resolved to merged records)
APPA-041, APPA-042
