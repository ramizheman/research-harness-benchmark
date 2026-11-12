# APPA-026: Agent Test A: LLM vs engine series-level PT recommendations

- Project: Strategy app
- Date: 2026-05-23 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: abandoned
- Failure type: A_unanswerable
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); Playoff series outcomes; LLM or agent outputs
- Method tags: LLM agent run
- Limitation tags: small sample
- Variable tags: 
- Paper: 

## Hypothesis
A generalist LLM (gemini-2.5-flash) on raw aggregates agrees with the engine and beats the team modal PT.

## Design
3 (team, series) pairs scored.

## Result
Pairs with both agent and engine recs: 0; agent scoreable n=0; engine hit 2/3 (66.7%).

## Failure evidence
0 agent recommendations produced; n=3.

## Power and reliability
n=3

## Related
APPA-027

## Notes


## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\AGENT_TEST_A_findings.md

## Related records (ids resolved to merged records)
APPA-027

## Also recorded as
APPS-045
