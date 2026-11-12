# EXP:APPM-025 | Personnel feasibility of rank-1 CUT openers
- date: 2026-04-20
- date_basis: mtime
- date_issues: file modification time: upper bound only; 11 records share this modification date (possible bulk edit or sync)
- date_reliable: no
- design: 8 teams; personnel capacity and stretch ceiling per PT vs rank-1 opener CUT target.
- hypothesis: Model's rank-1 openers are executable by each team's top-8 rotation.
- knowable_in_advance: yes
- member_of: FAM:SF32 {record=APPM-025; rule=audit/study_family_review.csv or singleton}
- motivates: FOLLOW:APPM-025 {needs_review=yes; record=APPM-025; rule=text pattern motivate/follow-up/next step}
- n_runs: 1
- notes: Led to V2 risk-aware, feasibility-filtered playsheet.
- prespecified: no
- produced: RES:APPM-025 {record=APPM-025; rule=record fields}
- project: Strategy app
- related_as_recorded: Playoff G1 retrospective
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\PERSONNEL_FEASIBILITY_PLAYOFF_TEAMS.md
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\PLAYOFF_RETRO_SUMMARY_2026-04-20.md
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\RISK_AWARE_OPENERS.md
- source: C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\STRATEGY_V2_RESULTS.md
- title: Personnel feasibility of rank-1 CUT openers
- uses_dataset: DS:Play_type_initiation_records_Neo4j_INITIATED_edges_play_type_possessions {record=APPM-025; rule=keyword rule DATASET_RULES}

# FOLLOW:APPM-025 | Follow-on candidate from APPM-025
- status: candidate from text pattern; not curated
- text: Led to V2 risk-aware, feasibility-filtered playsheet.

# RES:APPM-025 | Result of APPM-025
- failure_evidence: Optimizer uses league-average CUT execution and ignores personnel, so every team gets the same CUT-heavy opener.
- failure_type: C_artifact
- power_info: n=8 teams
- primary_result: All 24 openers seeded by CUT/PUTBACK/TRANSITION/PNR; CUT target exceeds stretch ceiling by +9.6 to +15.9pp for every team (e.g. PHI capacity 1.7% vs target 16.4%).
- record_stratum: artifact
- record_substatus: verdict artifact_found
- verdict: artifact_found
