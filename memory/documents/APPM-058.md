# APPM-058: PNR shot-level season rates vs possession labels

- Project: Strategy app
- Date: 2026-04-29 (mtime)
- Topic: Play-type labeling and data quality
- Pre-specified: no
- Verdict: descriptive
- Failure type: E_unclear
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); NBA play-by-play possessions and reconstructed lineups; Shot-level data with expected FG
- Method tags: 
- Limitation tags: 
- Variable tags: play-type share / mix
- Paper: 

## Hypothesis
PBP-derived shot-level PNR rates sit in a realistic band (script notes possession-level rates will be higher) and vary by team as expected.

## Design
PNR classifier on cached 2024-25 RS shots; team-level pnr_total_pct = (pnr_bh+pnr_roll)/half_court_shots.

## Result
2024-25 shot-level PNR share of half-court shots ranges from OKC 7.567% (498/6581) and BOS 7.854% to IND 13.824% (856/6192) and NYK 11.959%. ATL 11.361%, DEN 11.404%, PHX 10.232% (bh 7.050 / roll 3.181).

## Failure evidence
No pass/fail gate in the output; rates are a calibration input for PBPProxyPNR (later logs show calibrated PNR ~17.9-19.6% of possessions).

## Power and reliability
30 teams, half_court_shots ~5994-6581

## Related
APPM-014 PT audit (DRIVE foul-draw / OTHER leak)

## Notes
Script date 2026-04-29; csv mtime 2026-05-25. These are SHOT-level rates; do not compare directly to possession mix shares.

## Sources
- C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\_pnr_season_test.py
- C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\pnr_season_results.csv

## Related records (ids resolved to merged records)
APPM-014
