# APPA-053: Player and teammate sequential premiums

- Project: Defensive Suppression
- Date: 2026-05-31 (doc)
- Topic: Defensive suppression and counter strategy (BEST/AVOID)
- Pre-specified: no
- Verdict: descriptive
- Failure type: E_unclear
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions)
- Method tags: 
- Limitation tags: small sample; label or classification error
- Variable tags: PPP (points per possession)
- Paper: Detecting Defensive Suppression (published)

## Hypothesis
Specific same-player and teammate X->Y sequences carry PPP premiums above Y's baseline.

## Design
Full graph; min n=30; same initiator vs different initiator on Y.

## Result
Top same-player: P. George DRIVE->SPOT_UP +0.560 n=31 t=+2.2; J. Brown +0.349 n=62; L. Doncic DRIVE->PNR +0.309 n=53. Top teammate: K. Towns->O. Anunoby DRIVE->SPOT_UP +0.398 n=30; J. Brown->J. Tatum DRIVE->PNR +0.326 n=43.

## Failure evidence
Min n=30 cells; several labeled DIRECTIONAL at t~2.1-2.2; no multiplicity correction.

## Power and reliability
min n=30

## Related
APPA-049; APPA-058

## Notes
DRIVE->SPOT_UP and DRIVE->PNR dominate the top list.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\FINAL_NUMBERS_SHEET.md

## Related records (ids resolved to merged records)
APPA-049, APPA-058

## Same study family
SF40 (duplicate_records): APPS-038
shared P. George DRIVE->SPOT_UP +0.560 n=31 t=+2.2
