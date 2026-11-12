# APPS-026: Dose-response of continuation ratio vs matched excess decline

- Project: Strategy app
- Date: 2026-07-26 (mtime)
- Topic: Defensive suppression and counter strategy (BEST/AVOID)
- Pre-specified: partial
- Verdict: null
- Failure type: B_powered_null
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions)
- Method tags: matched control; regression
- Limitation tags: 
- Variable tags: 
- Paper: 

## Hypothesis
Among 11064 suppression triggers, higher h2_n/h1_n continuation predicts larger matched-pair excess decline.

## Design
OLS excess ~ cont_ratio + self_h1 + C(season)+C(play_type), cluster-robust SE by game. Exploratory post-hoc.

## Result
Raw n=11064: beta_cont=+0.0120, 95% CI [-0.0020,+0.0261], p=0.09336. Caliper 0.10: +0.0095 [-0.0122,+0.0312], p=0.392. All caliper and play-type strata not significant.

## Failure evidence
Primary CI includes 0 at n=11064 (p=0.09336); every caliper 0.05-0.30 and all six play types ns.

## Power and reliability
n=11064 triggers, 4606 game clusters

## Related
APPS-025

## Notes
Pre-specified read was that a CI including zero means no dose-response at this sample size.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\dose_response_continuation_results.md

## Related records (ids resolved to merged records)
APPS-025

## Same study family
SF14 (duplicate_records): CHT-067
shared raw n=11,064 beta +0.012 p=0.093, caliper 0.10 p=0.392
