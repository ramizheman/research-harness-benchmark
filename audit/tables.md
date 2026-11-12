# Audit tables (generated)

## Verdict counts (unique designs)

| verdict | designs | runs (sum n_runs) |
|---|---|---|
| null | 115 | 170 |
| supported | 89 | 114 |
| descriptive | 46 | 152 |
| inconclusive | 42 | 111 |
| artifact_found | 34 | 42 |
| failed_gate | 29 | 33 |
| abandoned | 10 | 10 |
| tool_eval_pass | 8 | 33 |
| reversed | 7 | 10 |
| tool_eval_fail | 4 | 6 |

## Failure type counts

| failure_type | designs |
|---|---|
| D_positive | 96 |
| B_powered_null | 83 |
| E_unclear | 82 |
| A_unanswerable | 63 |
| C_artifact | 60 |

## Verdict x failure type

| verdict | A_unanswerable | B_powered_null | C_artifact | D_positive | E_unclear | total |
|---|---|---|---|---|---|---|
| abandoned | 5 | 0 | 0 | 0 | 5 | 10 |
| artifact_found | 0 | 0 | 34 | 0 | 0 | 34 |
| descriptive | 4 | 0 | 0 | 5 | 37 | 46 |
| failed_gate | 10 | 9 | 9 | 0 | 1 | 29 |
| inconclusive | 19 | 0 | 3 | 0 | 20 | 42 |
| null | 23 | 67 | 11 | 0 | 14 | 115 |
| reversed | 0 | 6 | 0 | 0 | 1 | 7 |
| supported | 0 | 0 | 1 | 85 | 3 | 89 |
| tool_eval_fail | 1 | 1 | 2 | 0 | 0 | 4 |
| tool_eval_pass | 1 | 0 | 0 | 6 | 1 | 8 |

## Derived epistemic status

| status | designs |
|---|---|
| supported | 85 |
| adequately rejected (as specified) | 71 |
| cannot be tested with available data | 63 |
| artifact | 60 |
| no hypothesis test (descriptive) | 42 |
| not tested adequately | 32 |
| genuinely uncertain | 20 |
| tool evaluation | 8 |
| ambiguous classification | 3 |

## Topic x verdict

| topic | designs | supported | null | artifact | failed_gate | inconclusive | descriptive | A_unanswerable |
|---|---|---|---|---|---|---|---|---|
| Strategy engine and AI agent evaluation | 86 | 9 | 19 | 10 | 5 | 18 | 11 | 18 |
| Defensive suppression and counter strategy (BEST/AVOID) | 83 | 24 | 22 | 8 | 0 | 12 | 15 | 10 |
| Player absence and offensive reorganization | 63 | 24 | 18 | 3 | 8 | 3 | 3 | 9 |
| Structural roles and influence | 44 | 12 | 19 | 2 | 1 | 5 | 2 | 9 |
| Lineup and matchup effects | 32 | 4 | 17 | 1 | 6 | 0 | 4 | 10 |
| Play-type labeling and data quality | 18 | 1 | 1 | 4 | 4 | 2 | 3 | 3 |
| In-game and series adaptation | 16 | 1 | 8 | 2 | 0 | 1 | 3 | 0 |
| NCAA tournament prediction | 14 | 6 | 6 | 1 | 0 | 0 | 1 | 1 |
| Possession sequences and transitions | 13 | 2 | 3 | 2 | 3 | 0 | 2 | 1 |
| Other / unclassified | 7 | 1 | 1 | 0 | 1 | 1 | 2 | 1 |
| Playing time and luck response | 7 | 5 | 0 | 1 | 1 | 0 | 0 | 1 |
| Shot selection and shot quality | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |

## Pre-specification x failed

| prespecified | failed | not failed |
|---|---|---|
| yes | 44 | 31 |
| partial | 37 | 32 |
| no | 116 | 121 |
| unknown | 2 | 1 |

## Knowable in advance x failure type

| knowable | A_unanswerable | B_powered_null | C_artifact | D_positive | E_unclear |
|---|---|---|---|---|---|
| yes | 56 | 5 | 41 | 3 | 7 |
| no | 0 | 28 | 6 | 55 | 1 |
| unclear | 7 | 50 | 13 | 32 | 70 |
| NOT RECORDED | 0 | 0 | 0 | 6 | 4 |

## Projects

| project | designs |
|---|---|
| Strategy app | 171 |
| When a Hub Sits (Paper 2) | 49 |
| Defensive Suppression | 46 |
| Structural Influence (Paper 1) | 44 |
| Team Adaptation | 14 |
| Lineup Adaptation | 14 |
| March Madness | 13 |
| Lineup/Team Adaptation | 12 |
| Defensive Suppression (supplementary audit) | 9 |
| Halftime Minutes | 5 |
| When a Hub Sits (Paper 2) / opponent scouting | 3 |
| Playing-time / luck | 2 |
| Restoration Timing | 1 |
| When a Hub Sits (Paper 2) / Lineup Adaptation | 1 |

## Largest n_runs

| id | n_runs | title |
|---|---|---|
| APPM-046 | 62 | Matchup app reports TEAM_vs_TEAM (M-Z) |
| APPS-056 | 45 | Historical series_analysis backtest: winner and PT-rank Spearman |
| PAP-087 | 19 | NCAA men's feature additions that raised or failed to lower Brier |
| APPS-002 | 16 | Three-series adaptation review and v2 playsheet pipeline test |
| APPA-009 | 12 | Series adaptation experiment: static vs rolling vs adversarial-agent p |
| APPM-049 | 11 | SCOUT D6/D7 8-game calibration batch |
| PAP-057 | 11 | Pre-registered case forecasts (11 absences) |
| TMP-031 | 11 | Registered absence case studies (8 primary + 3 supplementary) |
| APPS-001 | 10 | Overnight 10-series LLM adaptation review (adapters win series) |
| APPS-017 | 8 | Execution conformance of observed mix vs recommended plan |
| PAP-091 | 8 | NCAA architecture failures (SWA, Platt, beta, MLP, 2nd isotonic in-sam |
| APPA-016 | 6 | Per-team calibration: model 'signal' (bias) vs actual PPP, V1-V6 |
| APPM-044 | 6 | Live-blog game replays: LP BEST/AVOID tier accuracy |
| PAP-086 | 6 | NCAA men's feature additions that improved LOSO Brier |
| APPS-044 | 5 | Clutch sequence-premium family (multiple windows) |

## Limitation categories (rule-tagged)

| limitation | designs |
|---|---|
| small sample | 118 |
| label or classification error | 24 |
| low power / large MDE | 21 |
| low measurement reliability | 20 |
| selection or regression to the mean | 16 |
| leakage | 13 |
| insufficient exposure | 10 |
| confounding | 10 |
| implementation bug | 7 |
| multiple testing | 3 |
| drift | 3 |

## Method x artifact rate

| method | designs | artifacts | rate |
|---|---|---|---|
| matched control | 98 | 18 | 0.18 |
| correlation | 89 | 11 | 0.12 |
| holdout, backtest or replay | 71 | 9 | 0.13 |
| regression | 56 | 7 | 0.12 |
| placebo or permutation test | 50 | 10 | 0.20 |
| calibration scoring | 40 | 8 | 0.20 |
| bootstrap interval | 35 | 4 | 0.11 |
| split-half reliability | 20 | 2 | 0.10 |
| difference-in-differences | 14 | 2 | 0.14 |
| LLM agent run | 14 | 3 | 0.21 |
| simulation | 13 | 2 | 0.15 |
| ablation | 7 | 2 | 0.29 |
| case study | 5 | 0 | 0.00 |
| ridge or RAPM ratings | 3 | 0 | 0.00 |

## Audit flag counts

| flag | designs |
|---|---|
| failure_type unclear | 82 |
| C_artifact but verdict null | 11 |
| B_powered_null without power_info | 11 |
| C_artifact but verdict failed_gate | 9 |
| no primary_result | 7 |
| descriptive with failure_type D_positive | 5 |
| descriptive with failure_type A_unanswerable | 4 |
| supported but failure_type E_unclear | 3 |
| ambiguous epistemic status | 3 |
| C_artifact but verdict inconclusive | 3 |
| C_artifact but verdict tool_eval_fail | 2 |
| supported but failure_type C_artifact | 1 |
| C_artifact but verdict supported | 1 |
| n_runs # (check whether runs are independent) | 1 |
| only #/# result numbers found in sources | 1 |
| no date | 1 |

Number verification: 356 records checkable, 3030 decimal numbers, 2988 found verbatim in cited sources (98.6%). Not checkable: 0. No decimals in result: 28.

Graph: 1380 nodes, 4235 edges. Node types: {'FailureMechanism': 5, 'Experiment': 384, 'Hypothesis': 384, 'ResearchQuestion': 12, 'Result': 384, 'Dataset': 8, 'StatisticalLimitation': 11, 'Variable': 12, 'DuplicateRecord': 63, 'FollowOnHypothesis': 10, 'Method': 14, 'Finding': 89, 'Paper': 4}. Edge types: {'tested_by': 384, 'addresses': 384, 'produced': 384, 'has_mechanism': 384, 'contradicted_by': 151, 'uses_dataset': 540, 'limited_by': 245, 'measures': 419, 'duplicates': 97, 'extends': 358, 'motivates': 10, 'uses_method': 515, 'invalidated_by': 34, 'supported_by': 89, 'derived_from': 89, 'reported_in': 144, 'supersedes_version': 7, 'rules_out': 1}. Edges needing review: 345.

## Study-family level: verdict of representative record

| verdict | study families |
|---|---|
| null | 107 |
| supported | 59 |
| descriptive | 41 |
| inconclusive | 34 |
| artifact_found | 29 |
| failed_gate | 21 |
| abandoned | 10 |
| tool_eval_pass | 8 |
| reversed | 6 |
| tool_eval_fail | 4 |

## Study-family level: derived epistemic status of representative record

| status | study families |
|---|---|
| adequately rejected (as specified) | 62 |
| cannot be tested with available data | 58 |
| supported | 55 |
| artifact | 50 |
| no hypothesis test (descriptive) | 37 |
| not tested adequately | 32 |
| genuinely uncertain | 14 |
| tool evaluation | 8 |
| ambiguous classification | 3 |

## Study-family level: topic

| topic | study families |
|---|---|
| Strategy engine and AI agent evaluation | 79 |
| Defensive suppression and counter strategy (BEST/AVOID) | 62 |
| Player absence and offensive reorganization | 42 |
| Structural roles and influence | 41 |
| Lineup and matchup effects | 30 |
| Play-type labeling and data quality | 18 |
| NCAA tournament prediction | 14 |
| In-game and series adaptation | 12 |
| Possession sequences and transitions | 10 |
| Other / unclassified | 7 |
| Playing time and luck response | 3 |
| Shot selection and shot quality | 1 |

## Multi-record study families

| family | kind | members | verdicts | conflict |
|---|---|---|---|---|
| SF01 | repeat_runs_or_robustness | APPA-037; PAP-036; PAP-037; PAP-038 | APPA-037=supported; PAP-036=supported; PAP-037=supported; PAP-038=supported | no |
| SF02 | duplicate_records | APPA-040; APPS-021; PAP-039; CHT-040 | APPA-040=supported; APPS-021=supported; PAP-039=supported; CHT-040=null | yes |
| SF03 | repeat_runs_or_robustness | APPA-036; APPM-030; APPS-019; APPS-020; PAP-043; CHT-042 | APPA-036=supported; APPM-030=supported; APPS-019=supported; APPS-020=supported; PAP-043=supported; CHT-042=supported | no |
| SF04 | repeat_runs_or_robustness | APPM-028; APPS-029; APPS-028; CHT-038 | APPM-028=supported; APPS-029=supported; APPS-028=inconclusive; CHT-038=descriptive | yes |
| SF05 | repeat_runs_or_robustness | APPA-041; APPS-031; APPM-031 | APPA-041=null; APPS-031=null; APPM-031=supported | yes |
| SF06 | duplicate_records | APPA-042; PAP-041 | APPA-042=reversed; PAP-041=null | yes |
| SF07 | duplicate_records | APPA-049; APPS-037 | APPA-049=supported; APPS-037=descriptive | yes |
| SF08 | duplicate_records | APPA-051; APPS-039 | APPA-051=inconclusive; APPS-039=descriptive | yes |
| SF09 | duplicate_records | APPA-057; APPS-042 | APPA-057=null; APPS-042=inconclusive | yes |
| SF10 | duplicate_records | APPA-059; CHT-089 | APPA-059=failed_gate; CHT-089=inconclusive | yes |
| SF11 | duplicate_records | APPA-018; CHT-005 | APPA-018=null; CHT-005=failed_gate | yes |
| SF12 | duplicate_records | APPA-002; APPS-051 | APPA-002=inconclusive; APPS-051=inconclusive | no |
| SF13 | repeat_runs_or_robustness | APPA-003; CHT-018; APPM-013 | APPA-003=artifact_found; CHT-018=artifact_found; APPM-013=supported | yes |
| SF14 | duplicate_records | APPS-026; CHT-067 | APPS-026=null; CHT-067=null | no |
| SF15 | duplicate_records | APPS-063; CHT-035 | APPS-063=null; CHT-035=artifact_found | yes |
| SF16 | duplicate_records | APPM-018; CHT-008 | APPM-018=descriptive; CHT-008=descriptive | no |
| SF17 | duplicate_records | APPS-080; CHT-049; PAP-002 | APPS-080=supported; CHT-049=supported; PAP-002=supported | no |
| SF18 | repeat_runs_or_robustness | APPS-083; PAP-004; APPA-039 | APPS-083=supported; PAP-004=supported; APPA-039=supported | no |
| SF19 | duplicate_records | APPS-084; PAP-017 | APPS-084=supported; PAP-017=supported | no |
| SF20 | duplicate_records | APPA-006; APPA-007; APPS-081; CHT-051; PAP-023 | APPA-006=supported; APPA-007=failed_gate; APPS-081=inconclusive; CHT-051=failed_gate; PAP-023=null | yes |
| SF21 | duplicate_records | CHT-077; PAP-045; PAP-046; TMP-025 | CHT-077=supported; PAP-045=supported; PAP-046=supported; TMP-025=supported | no |
| SF22 | repeat_runs_or_robustness | PAP-047; TMP-027; CHT-078; PAP-049; PAP-059 | PAP-047=supported; TMP-027=supported; CHT-078=inconclusive; PAP-049=supported; PAP-059=supported | yes |
| SF23 | duplicate_records | PAP-048; TMP-028 | PAP-048=supported; TMP-028=artifact_found | yes |
| SF24 | duplicate_records | PAP-052; TMP-033 | PAP-052=artifact_found; TMP-033=supported | yes |
| SF25 | bundle | TMP-036; PAP-063 | TMP-036=failed_gate; PAP-063=failed_gate | no |
| SF26 | bundle | TMP-035; CHT-079; PAP-060 | TMP-035=failed_gate; CHT-079=failed_gate; PAP-060=null | yes |
| SF27 | duplicate_records | CHT-004; PAP-097 | CHT-004=supported; PAP-097=null | yes |
| SF28 | duplicate_records | CHT-059; PAP-012 | CHT-059=inconclusive; PAP-012=null | yes |
| SF29 | duplicate_records | APPM-042; PAP-010 | APPM-042=null; PAP-010=null | no |
| SF30 | duplicate_records | APPS-065; CHT-030 | APPS-065=null; CHT-030=null | no |
| SF31 | duplicate_records | APPM-015; CHT-017 | APPM-015=artifact_found; CHT-017=artifact_found | no |
| SF32 | duplicate_records | APPA-033; APPM-025 | APPA-033=artifact_found; APPM-025=artifact_found | no |
| SF33 | duplicate_records | TMP-014; TMP-015 | TMP-014=null; TMP-015=failed_gate | yes |
| SF34 | duplicate_records | TMP-020; CHT-075 | TMP-020=null; CHT-075=null | no |
| SF35 | duplicate_records | CHT-070; TMP-011 | CHT-070=failed_gate; TMP-011=artifact_found | yes |
| SF36 | repeat_runs_or_robustness | PAP-069; TMP-010; PAP-070; PAP-071 | PAP-069=supported; TMP-010=supported; PAP-070=supported; PAP-071=supported | no |
| SF37 | duplicate_records | APPM-017; CHT-024 | APPM-017=inconclusive; CHT-024=inconclusive | no |
| SF38 | duplicate_records | CHT-065; TMP-008 | CHT-065=null; TMP-008=null | no |
| SF39 | duplicate_records | CHT-074; TMP-019 | CHT-074=null; TMP-019=null | no |
| SF40 | duplicate_records | APPA-053; APPS-038 | APPA-053=descriptive; APPS-038=descriptive | no |

Study families: 319 (from 384 merged records; 40 multi-record families covering 105 records; 20 with conflicting verdicts). Runs: lower bound 612 (largest n_runs within each family), upper bound 681 (sum over merged records).

Totals: designs 384, runs 681, failed 199, raw slice records 448.
