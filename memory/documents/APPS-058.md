# APPS-058: Observed on-ball defensive scheme labels (ORL-DET G1)

- Project: Strategy app
- Date: 2026-04-20 (mtime)
- Topic: Play-type labeling and data quality
- Pre-specified: no
- Verdict: failed_gate
- Failure type: A_unanswerable
- Knowable in advance: yes
- Runs: 1
- Dataset tags: NBA play-by-play possessions and reconstructed lineups
- Method tags: matched control
- Limitation tags: small sample; label or classification error
- Variable tags: PPP (points per possession)
- Paper: 

## Hypothesis
NBA matchup/PBP fields can label on-ball coverage (DROP/ICE/SWITCH) at usable rates.

## Design
Single game 0042500101. Confident labels vs OTHER.

## Result
DET: 67 on-ball HC poss, 10 labeled (14.9%) ? DROP n=5 PPP=1.20, ICE_CANDIDATE n=5 PPP=0.80, OTHER n=57 PPP=1.42. ORL: 60 poss, 2 labeled (3.3%). switches_on unpopulated.

## Failure evidence
Confident label rates 14.9% and 3.3%; NBA matchups feed did not populate switches_on.

## Power and reliability
n=67/60 possessions, 10/2 labeled

## Related
APPS-054

## Notes
ICE_CANDIDATE is unconfirmed without screen-contact tracking.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\data\observed_defense_0042500101.md

## Related records (ids resolved to merged records)
APPA-005
