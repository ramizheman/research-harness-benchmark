# APPA-048: Player-level BEST vs AVOID H2 PPP gaps (exploratory)

- Project: Defensive Suppression
- Date: 2026-05-31 (doc)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: descriptive
- Failure type: A_unanswerable
- Knowable in advance: yes
- Runs: 1
- Dataset tags: Playoff series outcomes
- Method tags: 
- Limitation tags: 
- Variable tags: PPP (points per possession); play-type share / mix
- Paper: Detecting Defensive Suppression (published)

## Hypothesis
Players score more on BEST-ranked counters than AVOID-ranked counters in the 55-series playsheets.

## Design
55-series graph; each player BEST-tier vs AVOID-tier H2 PPP; min 5 rows per tier; N=78 players.

## Result
78 players with >=5 BEST and >=5 AVOID rows. Top gaps D. Lively II +1.833 (n=6/6), M. Brogdon +1.831 (7/11); some reverse (N. Jokic -0.333 n=8/18; L. Doncic -0.190 n=6/14). Stars mixed (D. White +0.864 n=49/42; SGA +0.333 n=5/60).

## Failure evidence
n is small for most players (single-game playsheets); no multiplicity or clustered test.

## Power and reliability
78 players; min 5 rows/tier

## Related
APPA-036

## Notes
Exploratory; sheet says n is small for most players.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\FINAL_NUMBERS_SHEET.md

## Related records (ids resolved to merged records)
APPA-036
