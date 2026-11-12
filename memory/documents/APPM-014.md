# APPM-014: Play-type label accuracy / distribution audit

- Project: Strategy app
- Date: 2026-05-24 (mtime)
- Topic: Play-type labeling and data quality
- Pre-specified: partial
- Verdict: tool_eval_fail
- Failure type: C_artifact
- Knowable in advance: yes
- Runs: 2
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); NBA play-by-play possessions and reconstructed lineups
- Method tags: matched control
- Limitation tags: small sample; leakage; label or classification error
- Variable tags: PPP (points per possession); free throws / fouls
- Paper: 

## Hypothesis
Inferred play-type labels match benchmark volumes, foul rates, PPP and known team identities.

## Design
~1.07M possessions; compare volume, foul-draw, PPP to benchmark bands; team identity and known-game checks.

## Result
Audit overall FAIL: OTHER 20.2% vs <10% target; 40.8% low confidence; DRIVE foul-draw 1.7% vs 14-22% benchmark; most PTs PPP above benchmark band; MIA identity checks fail.

## Failure evidence
'play type labels have systematic issues that undermine adaptation findings'; foul possessions leak into OTHER.

## Power and reliability
n=1,073,607-1,078,047 possessions

## Related
Within-game adaptation; superstar suppression

## Notes
Undermines OTHER-based findings elsewhere.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\PT_ACCURACY_DIAGNOSTIC.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\PT_DISTRIBUTION_AUDIT.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\_pt_accuracy_diagnostic.py
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\_run_pt_audit.py
