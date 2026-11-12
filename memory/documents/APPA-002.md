# APPA-002: A1 within-scheme re-test controlling early-third PPP selection

- Project: Team Adaptation
- Date: 2026-05-16 (mtime)
- Topic: In-game and series adaptation
- Pre-specified: no
- Verdict: inconclusive
- Failure type: E_unclear
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: Playoff series outcomes
- Method tags: matched control
- Limitation tags: 
- Variable tags: PPP (points per possession)
- Paper: 

## Hypothesis
Within the same inferred scheme (and within early-PPP quintiles), adapters improve PPP more than wrong-way teams, and this carries to the next game.

## Design
Same playoff cells as A1; adapter vs wrong-way within DROP/HELP/SWITCH, early-PPP quintile matching, and within-scheme Game N to N+1 carryover; Welch and MW tests.

## Result
Within scheme gap: DROP +0.0830 (Welch p=0.0046), HELP +0.0539 (p=0.0493), SWITCH -0.0199 (p=0.6514). Quintile gaps -0.0440, -0.0231, +0.0138, +0.0133, +0.0966. Carryover gaps DROP +0.0039 (p=0.4244), HELP -0.0130 (p=0.7833), SWITCH -0.0392 (p=0.9353).

## Failure evidence
Quintile-matched gaps near zero in 4 of 5 quintiles; carryover null in all schemes; only DROP within-scheme gap significant without multiplicity correction.

## Power and reliability
adapt/wrong n: DROP 73/109, HELP 96/115, SWITCH 36/50

## Related
APPA-001; APPA-003

## Notes
The 'pooled across quintiles' gap +0.0556 equals the unmatched pooled gap, so it is not a matched estimate; flagged.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\A1_WITHIN_SCHEME_findings.md

## Related records (ids resolved to merged records)
APPA-001, APPA-003

## Also recorded as
CHT-019

## Same study family
SF12 (duplicate_records): APPS-051
shared within-scheme gaps DROP +0.0830 (p=0.0046), HELP +0.0539 (p=0.0493), SWITCH -0.0199 (p=0.6514) | APPA-001 shares only the baseline cell counts and stays separate.
