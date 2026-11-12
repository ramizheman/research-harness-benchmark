# APPA-067: TOV_FORCE 3-ply adversarial surviving lift

- Project: Strategy app
- Date: 2026-04-20 (mtime)
- Topic: Defensive suppression and counter strategy (BEST/AVOID)
- Pre-specified: no
- Verdict: descriptive
- Failure type: E_unclear
- Knowable in advance: unclear
- Runs: 4
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions)
- Method tags: regression
- Limitation tags: 
- Variable tags: turnovers
- Paper: 

## Hypothesis
Raw R1 TOV-force channel lifts survive opponent re-route or PT-shift (R2) and our follow-the-ball counter (R3).

## Design
Same 4 games; opponent min over re-route (top-3 alts) and PT-shift (>=200 opp poss); net surviving lift after R3. Direct cell if n>=10 else additive surrogate.

## Result
R1 lifts shrink ~50%+: ORL Banchero/Huerter +8.4 to net +3.7pp; DET Green/Anthony +7.0 to +3.5; PHI Harris/Vucevic +12.0 to +6.0; BOS Holiday/Council +6.1 to +2.8; PHX Booker/Wiggins +14.8 to +7.5; OKC Dort/Coffey +12.0 to +5.8; POR Lillard/McLaughlin +5.2 to +2.6; SAS Jones/Wesley +10.3 to +4.6. Many R3 cells used n<10 surrogates.

## Failure evidence
Net lift is model-implied, not observed in the games; R3 often additive surrogate at n<10.

## Power and reliability
4 games; 8 offense-defense sides

## Related
APPA-066; APPA-010

## Notes
R2 is almost always re-route (not PT-shift) because shifting 20% of mix leaves 80% of the R1 channel intact.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\HOW_TO_FORCE_TOVS_ADVERSARIAL.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\HOW_TO_FORCE_TOVS.md

## Related records (ids resolved to merged records)
APPA-066, APPA-010
