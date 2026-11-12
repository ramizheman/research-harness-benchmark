# APPA-027: Agent Test B: LLM counter selection vs deterministic BEST tier

- Project: Strategy app
- Date: 2026-06-15 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: inconclusive
- Failure type: A_unanswerable
- Knowable in advance: yes
- Runs: 1
- Dataset tags: LLM or agent outputs
- Method tags: LLM agent run
- Limitation tags: small sample
- Variable tags: PPP (points per possession)
- Paper: 

## Hypothesis
The LLM picks the same counter as the BEST tier, and when it disagrees it is right in H2.

## Design
3 suppression triggers; H2 PPP as referee.

## Result
Agrees with BEST 1/3; picks AVOID 2/3; disagreements engine right 2/2; mean H2 PPP BEST 1.650, agent 1.154, AVOID 0.642.

## Failure evidence
n=3 triggers; caveat says 230+ disagreements needed.

## Power and reliability
n=3

## Related
APPA-028

## Notes


## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\AGENT_TEST_B_findings_gemini_2_5_flash.md

## Related records (ids resolved to merged records)
APPA-028

## Also recorded as
APPS-046
