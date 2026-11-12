# APPM-012: ORL-DET opponent-specific leverage decomposition

- Project: Strategy app
- Date: 2026-04-20 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: null
- Failure type: E_unclear
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions)
- Method tags: 
- Limitation tags: 
- Variable tags: PPP (points per possession); play-type share / mix
- Paper: 

## Hypothesis
Openers' gains come from opponent-specific edges rather than universal high-PPP play types.

## Design
Per-PT opponent PPP allowed vs league, +/-5% threshold; decompose top-3 opener dPPP.

## Result
All top openers 'universal only' (opp-specific share +1.4% to +6.9%); DET within +/-5% of league on all seeded PTs.

## Failure evidence
No opponent-specific edge detected for either direction.

## Power and reliability


## Related
LEVERAGE_PREVALENCE.md (A-L)

## Notes


## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\ORL_DET_LEVERAGE.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\ORL_DET_LEVERAGE.json

## Also recorded as
APPS-016
