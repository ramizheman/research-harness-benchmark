# APPS-059: Sequence-memory horizon test (per-lag vs aggregated window)

- Project: Strategy app
- Date: 2026-06-13 (mtime)
- Topic: Possession sequences and transitions
- Pre-specified: partial
- Verdict: supported
- Failure type: D_positive
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: NBA play-by-play possessions and reconstructed lineups
- Method tags: regression; ridge or RAPM ratings
- Limitation tags: small sample
- Variable tags: win probability / series outcome
- Paper: 

## Hypothesis
Increasing prior-possession history changes the opponent's next-possession outcome after controlling for game state.

## Design
1024980 possessions with >=8 priors; TRAIN 22-24, VAL 24-25, TEST 2025-26. Per-lag vs aggregated window; GBT/logit/ridge.

## Result
Per-lag GBT AUC N=0 0.5621 -> N=1 0.5863 (d+0.0242) -> N=3 0.5907 -> N=8 0.5911. R2 0.0051 -> 0.0133. Aggregated window declines after N=1 (AUC 0.5868 -> 0.5687 at N=8). Effective horizon ~2-3 possessions.

## Failure evidence
Short-memory horizon is stable OOS; almost all gain is lag-1, plateau by lag 4. Absolute AUC still only ~0.591.

## Power and reliability
n=1,024,980 possessions; time-split test 2025-26

## Related
APPS-070; APPS-080

## Notes
Aggregated-window decline was dilution of lag-1, not absence of memory.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\sequence_memory\output\sequence_memory_report.md

## Finding status
supported in source; independent replication not recorded

## Related records (ids resolved to merged records)
APPS-070, APPS-080
