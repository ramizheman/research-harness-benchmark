# APPA-001: A1 adaptation falsification: asymmetry, confidence and carryover tests

- Project: Team Adaptation
- Date: 2026-05-16 (mtime)
- Topic: Structural roles and influence
- Pre-specified: partial
- Verdict: failed_gate
- Failure type: C_artifact
- Knowable in advance: yes
- Runs: 1
- Dataset tags: NBA play-by-play possessions and reconstructed lineups; Playoff series outcomes
- Method tags: 
- Limitation tags: selection or regression to the mean; label or classification error
- Variable tags: PPP (points per possession)
- Paper: 

## Hypothesis
If the A1 adapter PPP lift is real coverage response, wrong-way teams should do worse than no-signal teams, the gap should widen with scheme-vote confidence, and adapting in Game N should carry over to Game N+1.

## Design
Playoff possessions only; game-team cells bucketed adapter/neutral/no_signal/wrong_way; early-to-late third PPP deltas; 430 consecutive (N, N+1) series pairs; one-sided Welch and Mann-Whitney tests.

## Result
T1 dPPP: adapter +0.0667 (n=205), neutral +0.0248 (n=50), no_signal +0.1260 (n=57), wrong_way +0.0111 (n=274). T2: adapter minus no-signal -0.0361 (1 vote), -0.1170 (2 votes). T3 next-game PPP Welch t=-1.003, p=0.842; MW p=0.863; counter-carry Welch t=-2.163, p=0.985.

## Failure evidence
no_signal bucket (+0.1260) beats adapters (+0.0667); gap does not widen with confidence; carryover p=0.84; follow-up showed buckets selected on extreme early-third PPP (regression to mean).

## Power and reliability
n=205/50/57/274 cells; 430 pairs

## Related
APPA-002; APPA-003

## Notes
Scheme labels are only assigned when early-third PT PPP is >=10% hot/cold, which mechanically builds in mean reversion; this selection was knowable from the labeling rule before outcomes.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\A1_FALSIFICATION_findings.md

## Related records (ids resolved to merged records)
APPA-002, APPA-003

## Follow-on candidate
candidate, needs curation (see Notes)

## Also recorded as
APPS-053
