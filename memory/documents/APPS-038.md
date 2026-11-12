# APPS-038: Player sequential-premium family (same-player X->Y after opponent response)

- Project: Strategy app
- Date: 2026-05-31 (doc)
- Topic: Possession sequences and transitions
- Pre-specified: no
- Verdict: descriptive
- Failure type: E_unclear
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions)
- Method tags: 
- Limitation tags: small sample
- Variable tags: 
- Paper: 

## Hypothesis
Specific player X->Y sequences score above that player's unconditional Y baseline.

## Design
Same initiator on t and t+2; min n=30; focus pairs CUT->DRIVE, DRIVE->SPOT_UP, etc. Flag |t|>=2.0.

## Result
Top: P. George DRIVE->SPOT_UP +0.560 (n=31, t=+2.2). D. Mitchell SPOT_UP->DRIVE +0.279 (n=56, t=+2.8). Bottom: C. White DRIVE->SPOT_UP -0.466 (n=37); D. Bane DRIVE->PNR -0.324 (n=70, t=-2.7). Most cells DIRECTIONAL (n<50).

## Failure evidence
Many |t|<2 and n<50; no multiplicity correction; mixed signs on the same pair across players.

## Power and reliability
min n=30; DIRECTIONAL if n<50

## Related
APPS-037; APPS-070

## Notes
Later Brown->Tatum +0.326 (n=43) was shown to be a placebo artifact (APPS-070).

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\player_seq_premium\player_sequence_premium_report.md

## Related records (ids resolved to merged records)
APPS-037, APPS-070

## Same study family
SF40 (duplicate_records): APPA-053
shared P. George DRIVE->SPOT_UP +0.560 n=31 t=+2.2
