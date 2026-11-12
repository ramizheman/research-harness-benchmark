# APPM-023: Recency-weighted priors seed sanity check

- Project: Strategy app
- Date: 2026-04-20 (mtime)
- Topic: NCAA tournament prediction
- Pre-specified: no
- Verdict: artifact_found
- Failure type: C_artifact
- Knowable in advance: yes
- Runs: 1
- Dataset tags: NCAA tournament and ratings data
- Method tags: matched control; regression
- Limitation tags: small sample
- Variable tags: 
- Paper: 

## Hypothesis
Win probabilities from the decision context favor the higher seed in 4 2025-26 R1 matchups.

## Design
Compare pooled/OLS vs recency HL=1/OLS vs recency HL=0.5/per_team on 4 games.

## Result
Pooled: ORL 59%/DET 41% (8 seed favored); fixed: DET 86%/ORL 14%; all 4 now favor higher seed.

## Failure evidence
Equal-weight pooling of 4 seasons diluted 2025-26 rosters, producing the wrong favorite.

## Power and reliability
n=4 games

## Related
More training seasons A/B

## Notes
Per_team calibrator chosen on val R2 0.242 though holdout R2 earlier was 0.0213.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\STRATEGY_V2_RESULTS.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\_regen_dc_recency.py
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\_regen_dc_recency.log
