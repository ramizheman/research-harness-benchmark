# APPS-018: Ranked playsheet validation, 10 series (Spearman null; pairwise BEST>AVOID)

- Project: Strategy app
- Date: 2026-05-25 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: inconclusive
- Failure type: E_unclear
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); Playoff series outcomes
- Method tags: correlation
- Limitation tags: small sample; low measurement reliability; leakage
- Variable tags: PPP (points per possession)
- Paper: 

## Hypothesis
When a defense drops a play type >=0.25 PPP H1 to H2, playsheet counter ranking predicts which alternative scored better in H2 (BEST > SECOND > AVOID).

## Design
10 completed 2025-26 playoff series; 665 counter observations / 142 unique triggers; Spearman of tier rank vs observed H2 PPP plus Kruskal-Wallis and Mann-Whitney BEST vs AVOID.

## Result
Spearman rho=-0.0639, p=0.099717, n=665 (no clear full-rank signal). Kruskal-Wallis H=32.9723, p=2.7e-05. Mann-Whitney BEST 1.257 (n=56) vs AVOID 1.092 (n=160), U=5546.0, p=0.004018. Trigger accuracy rho=0.4525, n=121. Follow rate vs H2 PPP rho=-0.0664, p=0.5486, n=84.

## Failure evidence
Full-tier Spearman not significant (rho=-0.0639, p=0.099717) while pairwise BEST vs AVOID is; average counter n=6.9 possessions.

## Power and reliability
665 counter obs, 142 unique triggers; avg counter n=6.9

## Related
APPS-019; APPS-020

## Notes
Honest assessment: ranking noisy in full Spearman; pairwise BEST vs AVOID confirmed. Pipeline season_cap_yy=26 may leak R1 into R2 series.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\validation_report.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\_validation_run.log

## Related records (ids resolved to merged records)
APPS-019, APPS-020
