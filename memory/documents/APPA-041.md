# APPA-041: Post-trigger pickup toward BEST and alignment vs series wins

- Project: Defensive Suppression
- Date: 2026-06-19 (doc)
- Topic: Defensive suppression and counter strategy (BEST/AVOID)
- Pre-specified: no
- Verdict: null
- Failure type: B_powered_null
- Knowable in advance: no
- Runs: 1
- Dataset tags: Playoff series outcomes
- Method tags: correlation
- Limitation tags: 
- Variable tags: play-type share / mix; win probability / series outcome
- Paper: Detecting Defensive Suppression (published)

## Hypothesis
After suppression, teams shift H2 mix toward BEST-tier counters, and running BEST (vs AVOID) predicts series wins.

## Design
55 series, 272 games, 633 triggers, 110 series-directions; H1 to H2 BEST/AVOID share pickup; Spearman of %BEST/%AVOID vs series won.

## Result
591/633 triggers with BEST defined: 51.6% shifted more toward BEST, 22.4% used more AVOID; avg best_pickup +0.0024 pp; BEST share 10.0% to 10.2%; AVOID 8.9% to 9.5%. %BEST vs won rho=+0.131 p=0.17 n=110; %AVOID vs won rho=-0.098 p=0.31. H2 mix BEST 11.3% / AVOID 7.8% / INSUFF 55.8% volume.

## Failure evidence
Average BEST pickup ~0; alignment vs winning not significant at n=110. Teams already run ~29% AVOID in H1.

## Power and reliability
591 triggers; n=110 series-directions

## Related
APPA-036; APPA-024

## Notes
IND counterexample: 18.6% BEST follow, 71.4% series win rate (7 series-directions). Pickup is the behavioral claim; alignment is a second test in the same coaching section.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\FINAL_NUMBERS_SHEET.md

## Related records (ids resolved to merged records)
APPA-036, APPA-024

## Same study family
SF05 (repeat_runs_or_robustness): APPS-031, APPM-031
APPA-041 and APPS-031 share 51.6% / 22.4% / +0.0024 pp / 10.0% to 10.2%; APPM-031 is the same H1-to-H2 tier-share pickup test on another run (10.5% to 10.9%)
