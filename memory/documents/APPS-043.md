# APPS-043: PNR suppression RTM-excess team and player tables

- Project: Strategy app
- Date: 2026-08-21 (mtime)
- Topic: Defensive suppression and counter strategy (BEST/AVOID)
- Pre-specified: no
- Verdict: descriptive
- Failure type: A_unanswerable
- Knowable in advance: yes
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions)
- Method tags: matched control
- Limitation tags: 
- Variable tags: 
- Paper: 

## Hypothesis
PNR H1->H2 drops contain a team- and player-specific RTM-excess signal (who loses PNR; who takes it away).

## Design
2838 PNR triggers; matched pairs caliper 0.10 n=380. CR1 cluster SE on game. Player tables also c=0.15/0.20.

## Result
Offense excess c=0.10: GSW +0.702 n=12; MIA +0.110 CI[-0.119,+0.340] n=15. Defense: DAL +0.761 n=6 (CI crosses 0); UTA -0.005 CI[-0.203,+0.194] n=7. Players c=0.10 n>=5: J. Brown +0.643 n=10; only 2 players n>=10 at this caliper.

## Failure evidence
Overlapping CIs; player n>=10 at primary caliper is 2; many team CIs include 0. Ranks not distinguishable.

## Power and reliability
380 matched pairs at c=0.10 from 2838 triggers

## Related
APPS-022

## Notes
CHA/SAC digs are case studies on the same PNR-excess tables, not separate tests.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\pnr_suppression_rtm.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\cha_pnr_dig.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\sac_pnr_dig.md

## Related records (ids resolved to merged records)
PAP-036
