# APPA-025: Agent sequential adaptation test (costly-hit / matchup-hit)

- Project: Team Adaptation
- Date: 2026-05-23 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: partial
- Verdict: tool_eval_pass
- Failure type: A_unanswerable
- Knowable in advance: yes
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); NBA play-by-play possessions and reconstructed lineups; Playoff series outcomes; LLM or agent outputs
- Method tags: matched control; LLM agent run
- Limitation tags: small sample
- Variable tags: 
- Paper: 

## Hypothesis
An LLM agent given possession sequences identifies costly PTs and the series-specific top net-swing PT.

## Design
6 series-team units; agent output scored on costly-hit and matchup-hit.

## Result
Parse 6/6; costly-hit 100%; matchup-hit 100%; CUT emphasized 6/6.

## Failure evidence
n=6; agent emphasized CUT in 6/6, consistent with generic advice.

## Power and reliability
n=6

## Related
APPA-026

## Notes
Costly PTs are the same league-wide (77-88% of units), so the costly-hit benchmark is easy.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\AGENT_SEQ_ADAPTATION_findings.md

## Related records (ids resolved to merged records)
APPA-026

## Also recorded as
APPS-048
