# APPS-003: SQ2 decision quality hit rate: engine top pt_shift vs team modal PT

- Project: Strategy app
- Date: 2026-05-23 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: artifact_found
- Failure type: C_artifact
- Knowable in advance: yes
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); Playoff series outcomes
- Method tags: calibration scoring
- Limitation tags: small sample
- Variable tags: PPP (points per possession)
- Paper: 

## Hypothesis
The V4 engine's recommended play type outperforms the team's highest-volume play type in that playoff series.

## Design
(team, series) pairs across 42 correction_log series (84 rows, 53 scoreable in full-calibrated run); HIT if rec PT PPP > modal PT PPP, both n>=15.

## Result
Full-calibrated headline 69.8% (37/53); DRIVE-modal (banned-PT) comparisons 85.7% (12/14); clean comparisons 64.1% (25/39); high-confidence 64.3% (27/42). CUT recs 13/13; POST_UP 0/4. Uncalibrated archival: 51.7% (31/60), high-conf 42.9%, DRIVE recs 8% (n=25).

## Failure evidence
Headline 'structurally inflated': 14 of 53 pairs compare against banned DRIVE; 13 of 37 hits from CUT recs with structurally high PPP; in-sample, same series used to discover DRIVE failure and tune exclusion.

## Power and reliability
n=53 scoreable; no bootstrap CI computed

## Related
SQ2 holdout protocol; Post-hoc calibrated hit rate (96%); Possession-level SQ2 test; Alignment regression

## Notes
Knowable: the DRIVE ban and CUT PPP level were known before scoring. Holdout protocol (tuning 17 series, holdout 25, SHA 59a9be48) was written but no holdout result was found in files read.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\data\decision_quality_findings.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\validation\proof\decision_quality_test.py
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\validation\README.md

## Also recorded as
CHT-021
