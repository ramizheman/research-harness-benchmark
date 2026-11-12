# APPM-055: Three-level counter ranking: population vs team-specific vs matchup

- Project: Strategy app
- Date: 2026-05-24 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: inconclusive
- Failure type: E_unclear
- Knowable in advance: yes
- Runs: 3
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); NBA play-by-play possessions and reconstructed lineups; Playoff series outcomes
- Method tags: matched control
- Limitation tags: small sample
- Variable tags: three-point attempts or luck
- Paper: 

## Hypothesis
The best counter after a suppressed play type is stable from population (L1) to team (L2) to matchup (L3); otherwise the playsheet should not use a league default.

## Design
Full graph then playoff-only ranking. First run: 946,166 possessions / 5,164 games / 887 directed matchups, 56 pairs. Later rerun: 959,223 possessions / 5,226 games. Playoff ranking: 42,787 possessions / 74 matchups.

## Result
L1 (first run): after DRIVE best=CUT 1.261 vs PNR 1.132 (spread +0.129, CUT n_mu=5 PIVOT_WINS); after PNR best=TRANSITION 1.271 (n=35); after PULL_UP best=CUT 1.370 (n=5). L2 MIA disagrees with L1 on DRIVE (L2 best=PNR not CUT, gap=+0.125), PNR (DRIVE not TRANSITION), POST_UP, PULL_UP, SPOT_UP. Playoff right-counter: after DRIVE best=SPOT_UP 1.150 vs non_pivot 1.098 (n=26); after PNR best=DRIVE 1.151 vs 1.161 (n=35); after SPOT_UP best=PULL_UP 1.302 (n=4). Later L1 (2425 file): after CUT best=PULL_UP 1.231 (n=23 PIVOT_WINS) not PNR.

## Failure evidence
L2 disagrees with L1 on multiple MIA suppressions; playoff ranking also disagrees with L1 (DRIVE counter CUT vs SPOT_UP). CUT/TRANSITION bests often rest on n_mu=5-15.

## Power and reliability
L1 n_mu 5 to 696; playoff n_matchups 4 to 44

## Related
APPM-054 playoff pair sustainability

## Notes
Knowable: small n on CUT/TRANSITION counters is visible in the rank tables. L1 best-counter identity changed between the 946k and 959k pulls for suppressed CUT (PNR 1.216 vs PULL_UP 1.231).

## Sources
- C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\_three_level_sustainability.py
- C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\_three_level_out.txt
- C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\_three_level_out2.txt
- C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\_sustainability_results_2425.txt
- C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\_right_counter_ranking.py
- C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\_right_counter_ranking_out.txt

## Related records (ids resolved to merged records)
APPM-054
