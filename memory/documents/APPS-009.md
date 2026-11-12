# APPS-009: Player routing V4 vs V5 direct scoring

- Project: Strategy app
- Date: 2026-05-05 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: inconclusive
- Failure type: A_unanswerable
- Knowable in advance: yes
- Runs: 1
- Dataset tags: Playoff series outcomes
- Method tags: 
- Limitation tags: small sample
- Variable tags: PPP (points per possession)
- Paper: 

## Hypothesis
V5 player routing picks players with higher observed PPP than V4 routing.

## Design
Series where V4 and V5 routed to different players; compare observed PPP (n>=5 each).

## Result
8 divergences, 0 scoreable, 8 unscored (player missing from Neo4j); hit rate n/a.

## Failure evidence
Scoreable 0 of 8; V5 mostly routed to 'team' rather than a player.

## Power and reliability
n=8 divergences, 0 scoreable

## Related


## Notes
Data coverage could be checked before running.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\data\player_routing_results.md
