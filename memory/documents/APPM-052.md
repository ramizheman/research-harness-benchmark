# APPM-052: MIA vs BOS G6 2023 agent adaptation review

- Project: Strategy app
- Date: 2026-05-24 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: inconclusive
- Failure type: E_unclear
- Knowable in advance: unclear
- Runs: 2
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); LLM or agent outputs
- Method tags: LLM agent run
- Limitation tags: small sample
- Variable tags: PPP (points per possession)
- Paper: 

## Hypothesis
MIA failed to pivot after H1-H2 suppression of PULL_UP/PNR in 2023 ECF G6 (0042200306), leaving points vs H2H baseline.

## Design
Two LLM adaptation reviews of the same game plus generated playsheets. Agent review and FIXED copy are identical. Tactical review uses a different PT table.

## Result
Agent review: H1 PPP 1.158 -> H2 0.971. PULL_UP 1.6 (n=5) -> 0.5 (n=6); cost vs H2H 1.361: (1.361-0.5)*6=5.166 points. PNR 1.0 (n=4) -> 0.333 (n=6); cost (1.0-0.333)*6=4.002. Combined 9.168 points. Tactical review: reportable-PT overall 1.157 (n=38) -> 1.171 (n=35); PNR 1.0 (n=4) -> 0.333 (n=6), cost vs H2H 1.172: 4.895 points; PULL_UP 1.25 (n=4) -> 0.75 (n=4).

## Failure evidence
n=1 game; two reviews disagree on the primary miss (PULL_UP vs PNR) and on whether overall H2 PPP fell (0.971 vs 1.171) because possession classification differs.

## Power and reliability
n=1 game; H2 cells n=4 to 9

## Related
APPM-022 Superstar suppression; sequential premiums

## Notes
MIA_G6_2023_AGENT_REVIEW_FIXED.md is a byte-identical copy of the unfixed file. Ranked/tiered/v2 playsheets are app output (CUT opener, AVOID PNR) without outcome scoring.

## Sources
- C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\MIA_G6_2023_AGENT_REVIEW.md
- C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\MIA_G6_2023_AGENT_REVIEW_FIXED.md
- C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\MIA_BOS_G6_tactical.md
- C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\MIA_BOS_ranked_playsheet.md
- C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\MIA_BOS_tiered_playsheet.md
- C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\MIA_BOS_G6_v2_playsheet.md

## Related records (ids resolved to merged records)
APPM-022
