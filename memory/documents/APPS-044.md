# APPS-044: Clutch sequence-premium family (multiple windows)

- Project: Strategy app
- Date: 2026-06-04 (mtime)
- Topic: Possession sequences and transitions
- Pre-specified: no
- Verdict: descriptive
- Failure type: E_unclear
- Knowable in advance: unclear
- Runs: 5
- Dataset tags: 
- Method tags: 
- Limitation tags: 
- Variable tags: 
- Paper: 

## Hypothesis
Star X->Y offensive sequences in clutch have stable premiums across last-5 / last-10 windows.

## Design
Analysis A: team X then opp then star Y; premium vs star clutch baseline on Y. Windows last 5 min n>=25/30 and last 10 min n>=20/30. Analysis D is opp-suppression, separate.

## Result
Last 5 n>=25: 18 pos / 11 neg of 29 cells; top S. Curry DRIVE->PULL_UP +0.426 n=28. Last 10 n>=30: 25 pos / 13 neg of 38; top A. Edwards PULL_UP->DRIVE +0.365 n=33. Headline #1 sequence is not stable across windows. No-floor table is dominated by n=1 cells.

## Failure evidence
Top cell changes with window/floor; many n~25-35; no pooled test or multiplicity correction.

## Power and reliability
29 cells last5 n>=25; 38 cells last10 n>=30

## Related
APPS-035; APPS-038

## Notes
Family of window variants; conclusions do not stabilize so recorded as one descriptive family rather than separate supported findings.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\clutch_sequence_archetypes\clutch_sequence_premiums_CROSS_SCENARIO.md

## Related records (ids resolved to merged records)
APPS-035, APPS-038
