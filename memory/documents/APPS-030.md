# APPS-030: Coaching alignment: BEST/AVOID run rates vs series wins (55 series)

- Project: Strategy app
- Date: 2026-05-30 (mtime)
- Topic: Defensive suppression and counter strategy (BEST/AVOID)
- Pre-specified: no
- Verdict: null
- Failure type: A_unanswerable
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: Playoff series outcomes
- Method tags: correlation
- Limitation tags: small sample
- Variable tags: PPP (points per possession); win probability / series outcome
- Paper: 

## Hypothesis
Teams that run BEST counters more (and AVOID less) after suppression win more series.

## Design
633 triggers, 110 series-directions. Spearman of pct triggers ran BEST/AVOID vs series won.

## Result
% ran BEST 44.7% of triggers / 9.7% volume; % ran AVOID 61.1% / 23.3% volume. Spearman BEST vs won rho=+0.131 p=0.1723; AVOID vs won rho=-0.098 p=0.3099. Mean PPP BEST 1.395 vs AVOID 0.865.

## Failure evidence
Alignment-win Spearmans ns (p=0.172 / 0.310) at n=110 directions; INSUFF_EVIDENCE is 91.5% of triggers.

## Power and reliability
n=110 series-directions

## Related
APPS-027; APPS-031

## Notes
Volume share of BEST is only 9.7%; most H2 counters are INSUFF_EVIDENCE (46.8% volume).

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\coaching_alignment_55series\coaching_alignment_report.md

## Related records (ids resolved to merged records)
APPS-027, APPS-031
