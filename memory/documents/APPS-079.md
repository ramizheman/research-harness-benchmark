# APPS-079: State-attribution AUC decomposition of lag-1 memory

- Project: Strategy app
- Date: 2026-06-15 (mtime)
- Topic: Possession sequences and transitions
- Pre-specified: no
- Verdict: reversed
- Failure type: B_powered_null
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); NBA play-by-play possessions and reconstructed lineups
- Method tags: ablation
- Limitation tags: 
- Variable tags: play-type share / mix; win probability / series outcome
- Paper: 

## Hypothesis
Lag-1 predictive signal is process/state (pace, play type, transition) rather than outcome persistence.

## Design
Minimal-state base AUC=0.5205 vs full 0.5819 on 2025-26 opponent next-possession outcome. Block ablation.

## Result
Total attributable +0.0614 AUC. outcome_persistence marginal +0.0527 (39% share) unique +0.0069; momentum +0.0494 unique 0; transition_state unique +0.0117 (53% of unique); playtype_state unique +0.0003; lineup_state unique -0.0049.

## Failure evidence
Dominant block is outcome persistence/momentum, not play-type or lineup state. Unique signal is mostly transition_state.

## Power and reliability
2025-26 test set; original N0->N1 jump +0.0242 for reference

## Related
APPS-059

## Notes
Collinear blocks: momentum large alone, unique 0.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\sequence_memory\output\state_attribution.md

## Related records (ids resolved to merged records)
APPS-059
