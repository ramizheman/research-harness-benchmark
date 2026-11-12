# APPM-028: Live trigger timing: early vs late detection

- Project: Strategy app
- Date: 2026-06-19 (mtime)
- Topic: Defensive suppression and counter strategy (BEST/AVOID)
- Pre-specified: no
- Verdict: supported
- Failure type: D_positive
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: Playoff series outcomes
- Method tags: correlation
- Limitation tags: small sample
- Variable tags: PPP (points per possession); win probability / series outcome
- Paper: 

## Hypothesis
Earlier suppression triggers leave time to act and yield better BEST-counter outcomes.

## Design
228 trigger events (2024-26 playoffs); rest-of-game PPP by tier; early (<=12 H2 poss) vs late.

## Result
Tier Spearman rho -0.2066 p=1e-06 n=557; BEST-AVOID gap early 0.701 (26 triggers) vs late 0.415 (202); rho 0.2859 p=0.031 n=57.

## Failure evidence
rho 0.2859, p=0.031 (n=57).

## Power and reliability
n=57 BEST obs

## Related
Counter-tier validation Test 1

## Notes
Weak evidence: single p=0.03 with n=57.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\OVERNIGHT_SUMMARY.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\_run_live_trigger_validation.py

## Finding status
supported in source; independent replication not recorded

## Same study family
SF04 (repeat_runs_or_robustness): APPS-029, APPS-028, CHT-038
APPM-028 and APPS-029 share rho=-0.2066, n=557, gaps 0.701/0.415; APPS-028 (10 series) and CHT-038 (25 games) are earlier runs of the same trigger-timing design
