# APPS-069: State persistence vs window-overlap null (pre-registered FAIL)

- Project: Strategy app
- Date: 2026-07-12 (mtime)
- Topic: Possession sequences and transitions
- Pre-specified: yes
- Verdict: failed_gate
- Failure type: B_powered_null
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); NBA play-by-play possessions and reconstructed lineups
- Method tags: bootstrap interval; correlation
- Limitation tags: small sample
- Variable tags: 
- Paper: 

## Hypothesis
Process-only latent state (PCA-1 of tempo/transition) persists above the rolling-window overlap null after game x team demeaning.

## Design
N=1060893 possessions, 4 seasons, W=3 lagged. Excess = observed r - window-overlap null. Pre-registered criterion: excess persistence.

## Result
Process-only lag-1 r=+0.645 vs null +0.655; EXCESS=-0.010, cluster-bootstrap 95% CI [-0.012,-0.009]. Scoring excess -0.000; action texture +0.003. Instantaneous scoring autocorr lag-1=-0.0128.

## Failure evidence
HEADLINE FAIL: excess=-0.010 with CI entirely negative; state persistence does not clear the overlap null. No state-persistence paper.

## Power and reliability
N=1,060,893 possessions

## Related
APPS-059; APPS-072

## Notes
High raw r~0.65 is mechanical window overlap. Season-stable observed r 0.642-0.647.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\sequence_memory\output\state_persistence.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\sequence_memory\state_persistence.py

## Related records (ids resolved to merged records)
APPS-059, APPS-072
