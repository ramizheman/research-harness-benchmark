# APPA-028: Agent Test C: 3-agent halftime debate vs optimizer counter

- Project: Strategy app
- Date: 2026-06-16 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: inconclusive
- Failure type: A_unanswerable
- Knowable in advance: yes
- Runs: 1
- Dataset tags: LLM or agent outputs
- Method tags: LLM agent run
- Limitation tags: small sample; implementation bug
- Variable tags: PPP (points per possession)
- Paper: 

## Hypothesis
The LLM debate adds value over the deterministic optimizer counter.

## Design
5 suppression triggers; agreement and H2 PPP when they disagree.

## Result
Agreement 2/5 (40%); disagreements 3: debate wins 1, optimizer 1, tie 1; mean H2 PPP optimizer 1.812 vs debate 1.683.

## Failure evidence
n=5 triggers, 3 disagreements.

## Power and reliability
n=5

## Related
APPA-027

## Notes
Debate decision text and picked PT disagree in some rows (e.g. picked POST_UP while decision says SPOT_UP or CUT), suggesting a parsing bug.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\AGENT_TEST_C_optimizer_vs_debate.md

## Related records (ids resolved to merged records)
APPA-027

## Also recorded as
APPS-047
