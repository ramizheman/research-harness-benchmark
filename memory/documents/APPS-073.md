# APPS-073: Persistent Impact Score lag curves (global then within-team)

- Project: Strategy app
- Date: 2026-06-14 (mtime)
- Topic: In-game and series adaptation
- Pre-specified: partial
- Verdict: artifact_found
- Failure type: C_artifact
- Knowable in advance: yes
- Runs: 2
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); NBA play-by-play possessions and reconstructed lineups
- Method tags: matched control
- Limitation tags: 
- Variable tags: PPP (points per possession)
- Paper: 

## Hypothesis
Running play type X raises the same team's next 1-5 possession PPP vs a matched baseline (action memory).

## Design
Global baseline then re-center on team-season mean. PNR inferrer-only; OT+garbage excluded; min n>=30.

## Result
Global horizons: DRIVE/SPOT_UP/TRANSITION=5; others 0 (PNR/CUT/POST_UP/PUTBACK). SPOT_UP lag-1 lift +0.027 ctrl_p=0.0000. Within-team: all horizons 0 except SPOT_UP horizon(all)=1; PNR lag-1 within_team_lift=-0.0218.

## Failure evidence
Flat non-decaying global lifts disappear after team-season demeaning; remaining within-team memory is essentially none except SPOT_UP lag-1.

## Power and reliability
DRIVE lag-1 n=163696; SPOT_UP n=175021

## Related
APPS-059; APPS-069

## Notes
Knowable: good teams both run certain PTs and score more later, which a global baseline attributes to the PT.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\sequence_memory\output\persistent_impact_level1.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\sequence_memory\output\persistent_impact_level1_withinteam.md

## Related records (ids resolved to merged records)
APPS-059, APPS-069
