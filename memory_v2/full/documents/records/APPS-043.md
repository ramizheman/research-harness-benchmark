# EXP:APPS-043 | PNR suppression RTM-excess team and player tables
- date: 2026-08-21
- date_basis: mtime
- date_issues: file modification time: upper bound only
- date_reliable: no
- design: 2838 PNR triggers; matched pairs caliper 0.10 n=380. CR1 cluster SE on game. Player tables also c=0.15/0.20.
- hypothesis: PNR H1->H2 drops contain a team- and player-specific RTM-excess signal (who loses PNR; who takes it away).
- knowable_in_advance: yes
- member_of: FAM:SF-APPS-043 {record=APPS-043; rule=audit/study_family_review.csv or singleton}
- n_runs: 1
- notes: CHA/SAC digs are case studies on the same PNR-excess tables, not separate tests.
- prespecified: no
- produced: RES:APPS-043 {record=APPS-043; rule=record fields}
- project: Strategy app
- related_as_recorded: APPS-022
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\cha_pnr_dig.md
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\pnr_suppression_rtm.md
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\playsheet_validation\sac_pnr_dig.md
- title: PNR suppression RTM-excess team and player tables
- uses_dataset: DS:Play_type_initiation_records_Neo4j_INITIATED_edges_play_type_possessions {record=APPS-043; rule=keyword rule DATASET_RULES}
- uses_method: METH:matched_control {record=APPS-043; rule=keyword rule METHOD_RULES}

# RES:APPS-043 | Result of APPS-043
- failure_evidence: Overlapping CIs; player n>=10 at primary caliper is 2; many team CIs include 0. Ranks not distinguishable.
- failure_type: A_unanswerable
- power_info: 380 matched pairs at c=0.10 from 2838 triggers
- primary_result: Offense excess c=0.10: GSW +0.702 n=12; MIA +0.110 CI[-0.119,+0.340] n=15. Defense: DAL +0.761 n=6 (CI crosses 0); UTA -0.005 CI[-0.203,+0.194] n=7. Players c=0.10 n>=5: J. Brown +0.643 n=10; only 2 players n>=10 at this caliper.
- record_stratum: not_a_test
- record_substatus: descriptive
- verdict: descriptive
