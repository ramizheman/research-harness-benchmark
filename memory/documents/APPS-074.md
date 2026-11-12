# APPS-074: Gravity persistence: elite creator -> teammate PPP at lags 1-3

- Project: Strategy app
- Date: 2026-06-15 (mtime)
- Topic: Structural roles and influence
- Pre-specified: yes
- Verdict: null
- Failure type: B_powered_null
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: NBA play-by-play possessions and reconstructed lineups
- Method tags: matched control
- Limitation tags: 
- Variable tags: PPP (points per possession)
- Paper: 

## Hypothesis
After an elite creator's signature action, teammates score more on the team's next k possessions with the same lineup on the floor.

## Design
Exact match offensive lineup_id x margin bucket x period. 8 creators x 3 lags. BH-FDR 24 PPP cells.

## Result
All 8 creators horizon=0. Jokic lag-1 ATT=+0.0282 CI[-0.043,+0.099] p=0.3779. CLEAN NULL on teammate PPP. Secondary: Antetokounmpo +0.075 distinct initiators over next 3 poss (perm p=0.0002, BH 0.003) ? structure not efficiency.

## Failure evidence
No elite creator produces a positive lineup-matched teammate-PPP lift at any lag.

## Power and reliability
Jokic lag-1 n=1880; Giannis n=1804; Doncic n=325

## Related
APPS-065

## Notes
Usage redistribution without points payoff for Giannis is the only surviving structural cell.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\sequence_memory\output\gravity_persistence.md

## Related records (ids resolved to merged records)
APPS-065
