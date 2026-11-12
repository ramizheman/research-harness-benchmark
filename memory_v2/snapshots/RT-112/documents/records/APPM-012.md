# EXP:APPM-012 | ORL-DET opponent-specific leverage decomposition
- also_recorded_as: APPS-016
- date: 2026-04-20
- date_basis: mtime
- date_issues: file modification time: upper bound only; 11 records share this modification date (possible bulk edit or sync)
- date_reliable: no
- design: Per-PT opponent PPP allowed vs league, +/-5% threshold; decompose top-3 opener dPPP.
- hypothesis: Openers' gains come from opponent-specific edges rather than universal high-PPP play types.
- knowable_in_advance: unclear
- measures: VAR:PPP_points_per_possession {record=APPM-012; rule=keyword rule VARIABLE_RULES}
- measures: VAR:play_type_share_mix {record=APPM-012; rule=keyword rule VARIABLE_RULES}
- member_of: FAM:SF-APPM-012 {record=APPM-012; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- prespecified: no
- produced: RES:APPM-012 {record=APPM-012; rule=record fields}
- project: Strategy app
- related_as_recorded: LEVERAGE_PREVALENCE.md (A-L)
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\ORL_DET_LEVERAGE.json
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\ORL_DET_LEVERAGE.md
- title: ORL-DET opponent-specific leverage decomposition
- uses_dataset: DS:Play_type_initiation_records_Neo4j_INITIATED_edges_play_type_possessions {record=APPM-012; rule=keyword rule DATASET_RULES}

# RES:APPM-012 | Result of APPM-012
- failure_evidence: No opponent-specific edge detected for either direction.
- failure_type: E_unclear
- primary_result: All top openers 'universal only' (opp-specific share +1.4% to +6.9%); DET within +/-5% of league on all seeded PTs.
- record_stratum: uncertain
- record_substatus: inadequately tested: verdict null, mechanism E_unclear, no power information
- verdict: null
