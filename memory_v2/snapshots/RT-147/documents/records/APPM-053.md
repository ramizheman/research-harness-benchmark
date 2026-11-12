# EXP:APPM-053 | Defensive scheme extractor: SWITCH feed empty, ICE_CANDIDATE unvalidated
- date: 2026-04-24
- date_basis: doc
- date_reliable: yes
- design: v1.1 defensive_scheme_labeler: DROP on middle-channel pullups; ICE_CANDIDATE on sideline-channel same signature. SWITCH from defender-swap vs modal and MatchupEdge.total_switches. Direct v3 pull on 4 games.
- hypothesis: boxscorematchupsv3 switchesOn and per-possession ICE_CANDIDATE labels can drive defensive-scheme conformance.
- knowable_in_advance: yes
- member_of: FAM:SF-APPM-053 {record=APPM-053; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- notes: Knowable: endpoint schema includes the field but values are unused. Doc says do not re-probe this endpoint.
- prespecified: no
- produced: RES:APPM-053 {record=APPM-053; rule=record fields}
- project: Strategy app
- related_as_recorded: SCOUT defensive_pressure_response (8th query still deferred)
- source: C:\\Users\\lisas\\OneDrive\\Documents\\Basketball\\App\\Strategy\\PIPELINE_BACKLOG.md
- title: Defensive scheme extractor: SWITCH feed empty, ICE_CANDIDATE unvalidated
- uses_dataset: DS:Box_score_and_traditional_stats {record=APPM-053; rule=keyword rule DATASET_RULES}
- uses_dataset: DS:NBA_play_by_play_possessions_and_reconstructed_lineups {record=APPM-053; rule=keyword rule DATASET_RULES}
- uses_dataset: DS:Play_type_initiation_records_Neo4j_INITIATED_edges_play_type_possessions {record=APPM-053; rule=keyword rule DATASET_RULES}
- uses_method: METH:matched_control {record=APPM-053; rule=keyword rule METHOD_RULES}

# RES:APPM-053 | Result of APPM-053
- failure_evidence: NBA v3 feed does not populate switchesOn (759 rows, all zero); ICE_CANDIDATE not confirmed ICE without screen-contact tracking; HEDGE/TRAP/ZONE unlabeled.
- failure_type: A_unanswerable
- power_info: n=759 matchup rows / 4 games
- primary_result: On 0042500101, 0042500111, 0022400200, 0022400500: 759 matchup rows, zero non-zero switchesOn. R1G1 ICE_CANDIDATE counts: DET 5/5 DROP/ICE, OKC 6/4, PHX 5/2, SAS 8/6; BOS and PHI zero ICE_CANDIDATE. Confidence floor ICE 0.45 vs DROP 0.70. Manual validation (DROP agreement >=70%, ICE precision ~50%) not run.
- record_stratum: not_a_test
- record_substatus: tool_eval_fail
- verdict: tool_eval_fail
