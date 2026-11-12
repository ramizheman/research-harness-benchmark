# APPM-044: Live-blog game replays: LP BEST/AVOID tier accuracy

- Project: Strategy app
- Date: 2026-05-28 (mtime)
- Topic: Defensive suppression and counter strategy (BEST/AVOID)
- Pre-specified: no
- Verdict: inconclusive
- Failure type: E_unclear
- Knowable in advance: unclear
- Runs: 6
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); Playoff series outcomes
- Method tags: holdout, backtest or replay
- Limitation tags: small sample
- Variable tags: PPP (points per possession); play-type share / mix
- Paper: 

## Hypothesis
Pre-game LP BEST/AVOID tiers predict in-game play-type PPP (scored only on BEST/AVOID, not OK).

## Design
Replay of 6 playoff games with LP built on RS + prior series games; post-game tier accuracy on BEST/AVOID cells.

## Result
0042500104 and 0042500173: Final 0-0, no classified possessions. 0042500101 DET 96-ORL 108: DET 2/3 (67%), ORL 2/4 (50%); ORL AVOID share 50/79 (63%). 0042500111 BOS 123-PHI 90: BOS 3/4 (75%), PHI 2/3 (67%). 0042500114 BOS 127-PHI 94: both 3/4 (75%). 0042500311 SAS 122-OKC 115: SAS 3/6 (50%), OKC 4/6 (67%).

## Failure evidence
Two of six replays had no classified possessions; remaining games mixed 50-75% tier accuracy with frequent AVOID live-overrides (model wrong, engine caught it).

## Power and reliability
n=6 games; scored cells 3-6 BEST/AVOID per team

## Related
APPM-040; Counter-tier validation Test 1

## Notes
Updated copy of APPM-040 after opening REPLAY_0042500101/111/114/311. 0101 final DET 96-ORL 108 in replay vs RETRO 112-101; score source differs.

## Sources
- C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\REPLAY_0042500101.md
- C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\REPLAY_0042500104.md
- C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\REPLAY_0042500111.md
- C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\REPLAY_0042500114.md
- C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\REPLAY_0042500173.md
- C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\REPLAY_0042500311.md
- C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\_replay_blog.py
