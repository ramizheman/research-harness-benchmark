# APPA-015: A3 equilibrium vs actual significance test

- Project: Strategy app
- Date: 2026-04-15 (mtime)
- Topic: Strategy engine and AI agent evaluation
- Pre-specified: no
- Verdict: null
- Failure type: E_unclear
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: 
- Method tags: matched control
- Limitation tags: 
- Variable tags: 
- Paper: 

## Hypothesis
Matchup-aware equilibrium beats actual team behavior significantly across matchups.

## Design
Per-matchup A3 minus actual across 240 matchups; t-test.

## Result
A3 beats actual 138/240 (57.5%); weighted mean +2.06 pts/100; median +2.22; SD 14.26; t=2.24; p=0.0644.

## Failure evidence
Doc reports p=0.064 not significant.

## Power and reliability
n=240, SD 14.26 pts/100

## Related
APPA-011

## Notes
t=2.24 with n=240 should give p about 0.026 two-sided, so the stated p and t disagree. A3 PPP is nearly constant per offense, e.g. OKC 1.356 against every opponent.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\ADVERSARIAL_REPORT_V7.md

## Related records (ids resolved to merged records)
APPA-011
