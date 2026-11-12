# APPS-039: Season adapter profiles (BEST-share consistency across seasons)

- Project: Strategy app
- Date: 2026-05-31 (doc)
- Topic: Defensive suppression and counter strategy (BEST/AVOID)
- Pre-specified: no
- Verdict: descriptive
- Failure type: E_unclear
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: NBA play-by-play possessions and reconstructed lineups
- Method tags: 
- Limitation tags: 
- Variable tags: play-type share / mix
- Paper: 

## Hypothesis
Teams' post-trigger BEST vs AVOID mix is a stable coaching signature across seasons.

## Design
BEST share of H2 counter possessions; teams with n>=2 seasons. Consistency=stdev of BEST share.

## Result
Top mean BEST share: BOS 15.7% (10 dirs, win 70%), LAL 15.5%, GSW 13.8%. Bottom: HOU 2.5%, MIL 3.5%, LAC 4.1%. DEN 4.9% BEST / 70.8% INSUFF yet 62% win. ORL AVOID share 59.3%, 0% win.

## Failure evidence
No inferential test of stability vs noise; win% not identified with BEST share (IND 4.5% BEST, 71% win).

## Power and reliability
19 teams with n>=2 seasons

## Related
APPS-030; APPS-027

## Notes


## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\season_adapter_profiles\season_adapter_profiles_report.md

## Related records (ids resolved to merged records)
APPS-030, APPS-027

## Same study family
SF08 (duplicate_records): APPA-051
shared BOS 15.7%, LAL 15.5%, 59.3% | Verdicts differ: inconclusive vs descriptive.
