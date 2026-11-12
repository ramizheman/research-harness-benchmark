# APPS-085: Connector teammate-path quality Q_p split-half reliability

- Project: When a Hub Sits (Paper 2)
- Date: 2026-07-26 (mtime)
- Topic: Player absence and offensive reorganization
- Pre-specified: no
- Verdict: failed_gate
- Failure type: A_unanswerable
- Knowable in advance: yes
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions)
- Method tags: split-half reliability; correlation
- Limitation tags: low measurement reliability
- Variable tags: PPP (points per possession)
- Paper: When a Hub Sits (manuscript)

## Hypothesis
Connector quality Q_p (teammate-initiated on-off PPP gap) is a stable player-season attribute.

## Design
Odd/even game_id split; n=102 connectors with both halves; on&off >=80 poss/half, teammate-init on >=50. Spearman-Brown; ANOVA ICC.

## Result
Pearson r(Q_a,Q_b)=+0.215 p=0.0297; Spearman rho=+0.242. Spearman-Brown Q~0.355, S~0.278. Sign agreement 65.7% (67/102) binomial p=0.000996. ICC(player-season)=0.216 (78.4% within). Attenuation: even a perfect predictor max |r| with Q_p ~0.595; true r=0.30 attenuates to 0.179 (often undetectable).

## Failure evidence
Split-half r=0.215 / SB 0.355 is too low to treat Q_p as a stable scoutable trait; most variance is within-player half-to-half.

## Power and reliability
n=102 connectors

## Related
APPS-086; APPS-090

## Notes
L(p)/shape nulls are not just attenuation of a large true effect (true r<=0.25 could still be missed).

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\paper2_output\connector_qp_reliability_report.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\paper2_output\connector_qp_variance_audit_report.md

## Related records (ids resolved to merged records)
APPS-086, APPS-090
