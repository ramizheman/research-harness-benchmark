# APPS-057: SQ2 holdout protocol specified but not scored

- Project: Strategy app
- Date: 2026-05-23 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: yes
- Verdict: abandoned
- Failure type: A_unanswerable
- Knowable in advance: yes
- Runs: 1
- Dataset tags: Playoff series outcomes
- Method tags: holdout, backtest or replay; calibration scoring
- Limitation tags: small sample
- Variable tags: 
- Paper: 

## Hypothesis
A frozen-engine hit rate on 25 holdout series (cap_yy>23) is the defensible SQ2 number, vs in-sample 69.8%.

## Design
Engine SHA freeze 59a9be48; tuning 17 series cap_yy<=23; holdout 25 series. Protocol written; holdout scoring result not found in files read.

## Result
No holdout hit-rate number found. Protocol states existing --full-calibrated 69.8% is in-sample until the holdout is run.

## Failure evidence
Holdout was specified (SHA 59a9be48, 17/25 split) but no scored holdout output was located in this slice.

## Power and reliability
planned holdout n=25 series

## Related
APPS-003

## Notes
Confirms APPS-003 note that the holdout protocol exists without a result file.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\data\HOLDOUT_PROTOCOL.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\validation\proof\holdout_split.py

## Related records (ids resolved to merged records)
APPS-003
