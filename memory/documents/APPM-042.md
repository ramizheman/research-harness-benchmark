# APPM-042: Lineup structural-role coverage vs talent accumulation (prereg T1)

- Project: Structural Influence (Paper 1)
- Date: 2026-07-13 (doc)
- Topic: Structural roles and influence
- Pre-specified: yes
- Verdict: null
- Failure type: A_unanswerable
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: NBA play-by-play possessions and reconstructed lineups
- Method tags: bootstrap interval; regression; correlation
- Limitation tags: low power / large MDE
- Variable tags: PPP (points per possession)
- Paper: Structural Influence (published)

## Hypothesis
Conditional on talent and linear role counts, a lineup covering organizer+connector+terminal (COVERED) produces more PPP than one missing a function.

## Design
Possession-level OLS on 420,993 all-5-classified RS possessions (2022-24), 90 team-seasons; COVERED threshold plus n_ORG/n_CONN/n_TERM + leave-game-out TALENT + team-season FE; cluster-robust p and 2000 team-season cluster bootstrap. Feasibility gate first (G1-G3).

## Result
Gate PASS (COVERED 30.0%; 72 team-seasons both strata; |Spearman(COVERED,TALENT)|=0.042; R2(COVERED~counts)=0.203; Spearman(TALENT,PPP)=+0.027). M1 COVERED b=+0.0067 (+0.67 pts/100), t=1.35, p=0.176, team-season CI [-0.28,+1.65] pts/100 includes 0. n_ORGANIZER +2.24 t=7.29; n_CONNECTOR +0.53 t=1.35; n_TERMINAL +0.08 t=0.18; TALENT +3.98 t=0.60. M2 +0.64 p=0.188; naive +0.68 p=0.177; >=4/5 +0.83 p=0.068 CI [-0.08,+1.75]. MDE(80%) 1.4 pts/100 (from PAPER_NUMBERS_SHEET).

## Failure evidence
Estimate 0.67 below MDE 1.4 pts/100; p=0.176; CI includes 0. T1 NOT CONFIRMED: accumulation, not coverage.

## Power and reliability
n=420,993 possessions; MDE 1.4 pts/100; SE implied by t=1.35 on +0.67

## Related
APPM-037; Paper numbers audit

## Notes
Updated copy of APPM-037 after reading TOPOLOGY_COVERAGE_PREREGISTRATION.md (gate numbers and n_CONNECTOR/n_TERMINAL/TALENT terms were not in the earlier record). Terminal confirmatory test of the role program; no fallback.

## Sources
- C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\TOPOLOGY_COVERAGE_PREREGISTRATION.md
- C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\coverage_gate.py
- C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\coverage_full_study.py
- C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\PAPER_NUMBERS_SHEET.md

## Also recorded as
CHT-055

## Same study family
SF29 (duplicate_records): PAP-010
shared coverage confirmatory statistics (0.176, 1.35, 1.65) | Paper 1 T_cov preregistered test.
