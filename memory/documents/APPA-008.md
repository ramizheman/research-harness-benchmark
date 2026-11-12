# APPA-008: Audit of overnight LLM adaptation-analysis batch ('9/10 adaptation predicts winning')

- Project: Team Adaptation
- Date: 2026-05-24 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: artifact_found
- Failure type: C_artifact
- Knowable in advance: yes
- Runs: 1
- Dataset tags: Playoff series outcomes; LLM or agent outputs
- Method tags: LLM agent run
- Limitation tags: small sample
- Variable tags: win probability / series outcome
- Paper: 

## Hypothesis
The agent batch's findings (defensive adjustments, point costs, adaptation predicts series winners 9/10) are valid.

## Design
Methodology audit of 104 game reports, 10 series, 2073 tool calls; code and graph verification.

## Result
706 findings with n<5; list_h2h_games called 0 times; series winners LLM-inferred; MIA-BOS G7 score invented (BOS 100 vs graph 84); what_came_next skips a possession; point costs are LLM arithmetic.

## Failure evidence
Series winners never looked up (0/2073 calls); master '9/10' rule built from LLM inference on inference; low-n claims (e.g. 0.0 PPP on n=3).

## Power and reliability


## Related
APPA-009

## Notes
Half-level PPP splits verified as real; causal and winning claims not validated.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\ADAPTATION_AUDIT.md

## Related records (ids resolved to merged records)
APPA-009
