# APPM-053: Defensive scheme extractor: SWITCH feed empty, ICE_CANDIDATE unvalidated

- Project: Strategy app
- Date: 2026-04-24 (doc)
- Topic: Play-type labeling and data quality
- Pre-specified: no
- Verdict: tool_eval_fail
- Failure type: A_unanswerable
- Knowable in advance: yes
- Runs: 1
- Dataset tags: Play-type initiation records (Neo4j INITIATED edges / play-type possessions); NBA play-by-play possessions and reconstructed lineups; Box score and traditional stats
- Method tags: matched control
- Limitation tags: label or classification error
- Variable tags: 
- Paper: 

## Hypothesis
boxscorematchupsv3 switchesOn and per-possession ICE_CANDIDATE labels can drive defensive-scheme conformance.

## Design
v1.1 defensive_scheme_labeler: DROP on middle-channel pullups; ICE_CANDIDATE on sideline-channel same signature. SWITCH from defender-swap vs modal and MatchupEdge.total_switches. Direct v3 pull on 4 games.

## Result
On 0042500101, 0042500111, 0022400200, 0022400500: 759 matchup rows, zero non-zero switchesOn. R1G1 ICE_CANDIDATE counts: DET 5/5 DROP/ICE, OKC 6/4, PHX 5/2, SAS 8/6; BOS and PHI zero ICE_CANDIDATE. Confidence floor ICE 0.45 vs DROP 0.70. Manual validation (DROP agreement >=70%, ICE precision ~50%) not run.

## Failure evidence
NBA v3 feed does not populate switchesOn (759 rows, all zero); ICE_CANDIDATE not confirmed ICE without screen-contact tracking; HEDGE/TRAP/ZONE unlabeled.

## Power and reliability
n=759 matchup rows / 4 games

## Related
SCOUT defensive_pressure_response (8th query still deferred)

## Notes
Knowable: endpoint schema includes the field but values are unused. Doc says do not re-probe this endpoint.

## Sources
- C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\PIPELINE_BACKLOG.md
