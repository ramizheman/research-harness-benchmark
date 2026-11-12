# APPS-031: Coaching pickup: H1->H2 share shift toward BEST vs AVOID

- Project: Strategy app
- Date: 2026-05-30 (mtime)
- Topic: Defensive suppression and counter strategy (BEST/AVOID)
- Pre-specified: no
- Verdict: null
- Failure type: B_powered_null
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: NBA play-by-play possessions and reconstructed lineups
- Method tags: 
- Limitation tags: 
- Variable tags: play-type share / mix
- Paper: 

## Hypothesis
After suppression, teams shift volume toward the sheet BEST counter and away from AVOID.

## Design
best_pickup = H2 share - H1 share of BEST counter; 591/633 triggers with BEST defined. Also possession-weighted AVOID vs INSUFF mix H1->H2.

## Result
% shifted more toward BEST 51.6%; % used more AVOID 22.4%. Avg best pickup +0.0024 pp; BEST share 10.0%->10.2%. PO AVOID share within AVOID+INSUFF 13.4%->13.7% (+0.3 pp); BEST 12.9%->12.8%. RS AVOID +1.1 pp; BEST 13.1%->12.3%.

## Failure evidence
BEST pickup +0.24 pp is essentially zero; teams do not shift toward BEST; AVOID ticks up slightly.

## Power and reliability
n=591 triggers with BEST defined

## Related
APPS-030

## Notes
INSUFF_EVIDENCE dominates (~83-86% of AVOID+INSUFF possessions).

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\coaching_pickup_55series\coaching_pickup_report.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\h1h2_tier_mix_shift.md

## Related records (ids resolved to merged records)
APPS-030

## Same study family
SF05 (repeat_runs_or_robustness): APPA-041, APPM-031
APPA-041 and APPS-031 share 51.6% / 22.4% / +0.0024 pp / 10.0% to 10.2%; APPM-031 is the same H1-to-H2 tier-share pickup test on another run (10.5% to 10.9%)
