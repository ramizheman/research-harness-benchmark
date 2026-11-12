# APPM-031: Teams don't adapt after suppression (H1 to H2 tier shares)

- Project: Defensive Suppression
- Date: 2026-06-19 (mtime)
- Topic: Defensive suppression and counter strategy (BEST/AVOID)
- Pre-specified: no
- Verdict: supported
- Failure type: D_positive
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); Playoff series outcomes
- Method tags: 
- Limitation tags: 
- Variable tags: PPP (points per possession); play-type share / mix
- Paper: Detecting Defensive Suppression (published)

## Hypothesis
Offenses shift toward BEST counters and away from suppressed plays after a trigger.

## Design
55 playoff series; H1 vs H2 BEST/AVOID shares; continuation cost of suppressed PT.

## Result
BEST share 10.5% -> 10.9%, AVOID 29.1% -> 29.5% (pickup +0.003 pp); continuing suppressed PT -0.646 PPP (corrected 0.63 trigger row-mean); ~5.4 points per trigger; AVOID vs continue +0.054 (corrected +0.069/+0.162).

## Failure evidence
Shares flat H1->H2.

## Power and reliability


## Related
Within-series learning

## Notes
Claim is a behavioral null (no adaptation).

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\PRESENTATION_SLIDE_NUMBERS.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\PRESENTATION_STRUCTURE_v8.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\_points_left_on_table.py
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\_cost_of_ignoring_suppression.py

## Finding status
supported in source; independent replication not recorded

## Same study family
SF05 (repeat_runs_or_robustness): APPA-041, APPS-031
APPA-041 and APPS-031 share 51.6% / 22.4% / +0.0024 pp / 10.0% to 10.2%; APPM-031 is the same H1-to-H2 tier-share pickup test on another run (10.5% to 10.9%)
