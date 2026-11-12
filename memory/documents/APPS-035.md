# APPS-035: Clutch-after-suppression star PPP vs overall (30 stars, RS 2025-26)

- Project: Strategy app
- Date: 2026-06-20 (doc)
- Topic: Defensive suppression and counter strategy (BEST/AVOID)
- Pre-specified: no
- Verdict: reversed
- Failure type: B_powered_null
- Knowable in advance: no
- Runs: 1
- Dataset tags: NBA play-by-play possessions and reconstructed lineups
- Method tags: correlation
- Limitation tags: small sample; selection or regression to the mean
- Variable tags: PPP (points per possession)
- Paper: 

## Hypothesis
Stars elevate in clutch possessions of games where their team had a suppression trigger.

## Design
Clutch=Q4 last 5 min |margin|<=5. Group X=clutch in suppression games vs Z=overall. n_X>=15; n=24 OK-confidence players. Also raw clutch vs overall table.

## Result
Mean X-Z uplift -0.065, t=-2.41, p=0.025, n=24 (16 negative / 8 positive). Pearson r(uplift, IE%)=0.031, p=0.885. Brunson X-Z=+0.003 (rank 8/24). Raw clutch vs overall: Edwards +0.225, Giannis -0.240; Brunson -0.021.

## Failure evidence
Significant league-wide decline (-0.065 PPP, p=0.025), opposite of elevated clutch-cooking; IE% does not predict uplift.

## Power and reliability
n=24 players with n_X>=15; PO replication not run

## Related
APPS-045

## Notes
Selection likely: these clutch minutes occur in games where the offense already failed to adapt.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\clutch_after_suppression.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\clutch_30stars.md

## Related records (ids resolved to merged records)
APPA-026

## Follow-on candidate
candidate, needs curation (see Notes)

## Also recorded as
CHT-043
