# APPM-017: Possession-level SQ2 test: proxy engine on all RS games

- Project: Strategy app
- Date: 2026-05-23 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: inconclusive
- Failure type: E_unclear
- Knowable in advance: yes
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); NBA play-by-play possessions and reconstructed lineups
- Method tags: difference-in-differences; matched control; regression
- Limitation tags: small sample
- Variable tags: 
- Paper: 

## Hypothesis
A matchup-conditioned PT picker has possession-level signal at team-game level.

## Design
Proxy engine on 4,082 qualifying team-games; Tests A/B/C; 16,921 cells for FE OLS.

## Result
C gamma +0.0714 SE 0.0057 p=0.0000; B DiD +0.062 [0.051,0.073]; proxy agrees with production engine 13/79 = 16.5%.

## Failure evidence
Proxy fidelity 16.5% (<70%); in-sample contamination of RS aggregates; iid SEs.

## Power and reliability
n=16,921 cells

## Related
Possession-level SQ2 test (playoff series)

## Notes
Positive for proxy only; does not validate production engine.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\POSSESSION_PPP_ALL_GAMES_findings.md

## Also recorded as
APPS-055

## Same study family
SF37 (duplicate_records): CHT-024
shared proxy-engine gamma +0.0714 and DiD +0.062
