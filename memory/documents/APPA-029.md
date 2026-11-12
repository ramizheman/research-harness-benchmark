# APPA-029: Crunch-time identity stability year over year

- Project: Strategy app
- Date: 2026-05-06 (mtime)
- Topic: Structural roles and influence
- Pre-specified: partial
- Verdict: null
- Failure type: A_unanswerable
- Knowable in advance: yes
- Runs: 1
- Dataset tags: NBA play-by-play possessions and reconstructed lineups
- Method tags: correlation
- Limitation tags: 
- Variable tags: PPP (points per possession)
- Paper: 

## Hypothesis
Team crunch-time PPP delta vs baseline is a stable organizational identity.

## Design
93 team-seasons 2022-25, gate >=100 crunch possessions; YoY Pearson across 62 pairs; player-attribution heuristic.

## Result
YoY r = -0.023 (n=62 pairs); consistently positive CHI +0.056, CHA +0.040; negative NOP -0.074.

## Failure evidence
r=-0.023 on 62 pairs; per-team-season crunch samples ~100+ possessions, so deltas of +/-0.05 PPP are within sampling noise.

## Power and reliability
62 pairs; >=100 crunch poss per team-season

## Related


## Notes
Doc still calls consistently positive teams 'genuine crunch-time performers' despite r~0, and has a blank team row. Knowable because single-season PPP on ~100 possessions has SE comparable to the deltas.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\crunch_identity_findings.md

## Also recorded as
CHT-012
