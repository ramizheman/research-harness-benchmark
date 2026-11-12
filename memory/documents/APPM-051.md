# APPM-051: Risk-aware feasible openers vs legacy mu-top CUT

- Project: Strategy app
- Date: 2026-04-20 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: artifact_found
- Failure type: C_artifact
- Knowable in advance: yes
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); NBA play-by-play possessions and reconstructed lineups; Playoff series outcomes
- Method tags: matched control
- Limitation tags: small sample
- Variable tags: PPP (points per possession); turnovers
- Paper: 

## Hypothesis
Scoring candidates by P(overperform) over 95 possessions and dropping INFEASIBLE personnel pushes changes the rank-1 opener away from CUT for playoff G1s.

## Design
4 games / 8 team-sides; pool pt_shift, matchup_hunt, four_factor, tempo; compare legacy E[Delta PPP] opener vs best feasible risk-aware opener.

## Result
ORL underdog: CUT-push INFE P=36.7% -> OREB_PUSH +3.0pp P=35.0% (DeltaP -1.7pp); baseline P(overperform) 29.9%, best feasible +5.1pp to 35.0%. DET favorite: TOV_AVOID stays, P=76.8%. PHI: PUTBACK INFE 28.9% -> OREB_PUSH 28.5%. BOS: CUT INFE 80.3% -> OREB_PUSH 79.9%. OKC: CUT INFE 60.5% -> OREB_PUSH 60.1%. PHX/POR/SAS four_factor already FEAS, DeltaP +0.0pp. ORL 18/26 candidates INFEASIBLE; DET 18/38 INFEASIBLE.

## Failure evidence
Legacy rank-1 is INFEASIBLE CUT/PUTBACK for 4/8 sides; feasible four-factor openers replace them with only -0.3 to -1.7pp modeled P.

## Power and reliability
n=8 team-sides; not outcome-tested

## Related
APPM-025; APPM-023

## Notes
Demonstration of a product change, not a backtest against game outcomes. Complements the CUT-capacity table (ORL stretch 6.0% vs target 19.1%, gap +13.1pp).

## Sources
- C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\RISK_AWARE_OPENERS.md
- C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\_risk_rerank_playoff.py
- C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\PERSONNEL_FEASIBILITY_PLAYOFF_TEAMS.md
- C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\STRATEGY_V2_RESULTS.md

## Related records (ids resolved to merged records)
APPM-025, APPM-023
