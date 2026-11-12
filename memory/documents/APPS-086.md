# APPS-086: Connector ecosystem quality: L(p) and |dA| do not predict Q_p

- Project: When a Hub Sits (Paper 2)
- Date: 2026-07-26 (mtime)
- Topic: Player absence and offensive reorganization
- Pre-specified: no
- Verdict: null
- Failure type: B_powered_null
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: 
- Method tags: correlation
- Limitation tags: 
- Variable tags: structural influence / load (L)
- Paper: When a Hub Sits (manuscript)

## Hypothesis
Scalar structural load L(p) or an |dA|-weighted ecosystem lift predicts teammate-path quality Q_p.

## Design
N=102 connectors (pos=53, neg=49). Talent+opp+period+score residualized S_p and Q_p.

## Result
L(p) vs Q_p r~0. Uniform mean tm_dPPP vs Q_p r=+0.812; |dA|-weighted eco r=+0.703; eco residualized on uniform vs Q_p r=+0.084 p=0.399 NULL. Cosine to mean positive footprint vs Q_p r=-0.336 p=0.000559 (wrong sign). Pair-level dA contrasts do not survive FDR.

## Failure evidence
Proposed structural metrics add nothing beyond a uniform average of teammate lifts (eco residual r=+0.084 p=0.399). Load is not quality.

## Power and reliability
n=102

## Related
APPS-085; APPS-084

## Notes
Together with portability: signature may travel but connector *value* looks relational/context-specific.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\paper2_output\connector_ecosystem_quality_report.md

## Related records (ids resolved to merged records)
APPS-085, APPS-084
