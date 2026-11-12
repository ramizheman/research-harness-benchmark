# APPS-051: A1 within-scheme adapter vs wrong-way (selection-controlled)

- Project: Strategy app
- Date: 2026-05-16 (mtime)
- Topic: Defensive suppression and counter strategy (BEST/AVOID)
- Pre-specified: partial
- Verdict: inconclusive
- Failure type: E_unclear
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: NBA play-by-play possessions and reconstructed lineups; Playoff series outcomes
- Method tags: matched control
- Limitation tags: implementation bug
- Variable tags: PPP (points per possession)
- Paper: 

## Hypothesis
Within inferred scheme, teams that shift toward SHOULD counters (adapters) have higher early->late dPPP than wrong-way teams, after removing early-PPP selection.

## Design
Playoff possessions. Within-scheme adapter vs wrong-way; also early-PPP quintile match. Carryover Game N->N+1.

## Result
DROP: adapt +0.0041 vs wrong -0.0789, gap +0.0830, Welch p=0.0046, n=73/109. HELP: +0.0943 vs +0.0404, gap +0.0539, p=0.0493, n=96/115. SWITCH: +0.1200 vs +0.1399, gap -0.0199, p=0.6514, n=36/50. Pooled quintiles: adapt +0.0667 n=205 vs wrong +0.0111 n=274, gap +0.0556. Carryover next-game PPP gaps ns (DROP +0.0039 p=0.4244).

## Failure evidence
DROP/HELP within-scheme gaps are positive; SWITCH has the wrong sign; next-game carryover is null. Early-PPP of wrong_way (1.0939) still exceeds adapters (1.0448).

## Power and reliability
n adapt=205, wrong=274

## Related
APPS-052; APPS-053

## Notes
Wrote to fix unfair T1 that compared adapters to no_signal cells that never started hot.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\A1_WITHIN_SCHEME_findings.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\validation\proof\a1_within_scheme.py

## Related records (ids resolved to merged records)
APPM-013, APPA-001

## Same study family
SF12 (duplicate_records): APPA-002
shared within-scheme gaps DROP +0.0830 (p=0.0046), HELP +0.0539 (p=0.0493), SWITCH -0.0199 (p=0.6514) | APPA-001 shares only the baseline cell counts and stays separate.
