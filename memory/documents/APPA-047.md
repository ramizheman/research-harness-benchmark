# APPA-047: Live H2 trigger timing: remaining possessions window

- Project: Defensive Suppression
- Date: 2026-05-25 (doc)
- Topic: Defensive suppression and counter strategy (BEST/AVOID)
- Pre-specified: unknown
- Verdict: descriptive
- Failure type: E_unclear
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: NBA play-by-play possessions and reconstructed lineups
- Method tags: simulation
- Limitation tags: 
- Variable tags: 
- Paper: Detecting Defensive Suppression (published)

## Hypothesis
Suppression can be detected live in H2 with enough possessions remaining to act.

## Design
Live H2 trigger simulation _run_live_trigger_validation.py; cited only as mean remaining possessions in the paper-mapping table.

## Result
Mean 21 poss remaining.

## Failure evidence
Sheet records only the mean (~21); no distribution, hit rate, or comparison to a false-alarm rate in this file.

## Power and reliability


## Related
APPA-040

## Notes
Primary artifact live_trigger_report.md is outside this slice.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\FINAL_NUMBERS_SHEET.md

## Related records (ids resolved to merged records)
APPA-040
