# Automation plan: research-memory benchmark without human curation

Status on 2026-11-10: the replay pipeline runs end to end without human input. A mock dry run of the 10-task pilot (30 runs) completed through scoring and analysis. The real pilot needs one thing before it can run: a working model API key (all three keys in the project `.env` were rejected; see `remaining_human_requirements.md`).

Every label produced here is **automated adjudication**: rule-based, reproducible and stored with confidence and provenance. It is not equivalent to independent human adjudication, and results that rest on it are described as provisional.

## 1. Pipeline

All scripts are in `scripts\`, read the existing benchmark records without modifying them, and write only new files in this folder. Run them in order with the benchmark virtual environment.

| step | script | produces |
|---|---|---|
| history preparation | `10_prepare_history.py` | `automated_adjudication.csv`, `research_question_clusters.csv`, `audit\date_audit.csv`, `audit\overlap_candidates.csv`, `audit\cluster_calibration.json`, `audit\adjudication_summary.md` |
| memory v2 | `11_build_memory_v2.py` | `memory_v2\full\` (documents and graph), `audit\memory_v2_audit.json`, `audit\extends_direction_audit.csv` |
| replay tasks | `12_generate_replay_tasks.py` | `replay_task_pool.csv`, `benchmark_answer_key.jsonl`, `tasks\replay\RT-*.json`, pilot snapshots in `memory_v2\snapshots\` |
| prospective challenges | `13_generate_challenges.py` | `prospective_challenge_pool.csv`, `tasks\prospective\PC-*.json` |
| 2026-27 data | `14_fetch_2026_27.py` | `data_2026_27\development\` now; `data_2026_27\validation\` only after the gate opens |
| experiment | `20_run_experiment.py` | `runs\<experiment>\` raw runs, blinded outputs, scores, analysis, report |
| pre-flight | `21_preflight.py` | console check of tasks, snapshots, key and estimated cost (spends nothing) |
| tests | `python -m unittest discover -s tests -t .` | 41 tests, all passing |

Code lives in `bench\` (history, memory, tasks, challenges, scoring, statistics, claims, redaction) and `runner\` (model clients, tools, agent loop, experiment phases).

## 2. Section 1 prerequisites: what each rule does

| prerequisite | implementation | result |
|---|---|---|
| Resolve conflicting family verdicts | `adjudicate.resolve`, rules R0 to R6, applied in order: single record or no test (R0); unanimous (R1); bundle of different sub-claims becomes mixed (R6); an artifact finding dominates unless a later, corrected supported re-test exists (R2); latest member wins when the date order is certain (R3); paper record wins when order is uncertain (R4); otherwise uncertain (R5) | 319 families: R0 281, R1 20, R5 7, R2 6, R4 4, R3 1 |
| Confidence | starts at 1.0; minus 0.3 for an unclear mechanism, 0.2 for verdict and mechanism that contradict each other, 0.2 when under half the result numbers were found in sources, 0.5 for no result, 0.05 for a date that is only an upper bound; multiplied by the rule's multiplier; leave-one-out stability for families of three or more | high 227, medium 76, low 16 |
| Preserve conflicting evidence | `member_strata`, `member_verdicts`, `mechanism_votes` and `conflicting_evidence` keep every member's label | 20 families with disagreeing members, all with conflicting evidence recorded |
| Separate outcome from mechanism | `outcome_status` (verdict family) and `failure_mechanism` (A to E) are separate columns; the stratum combines them by explicit rule | |
| Reconcile family and record counts | one row per family; members listed; record total equals 384 (unit test) | |
| Duplicates and overlaps | lexical similarity at or above the repeat threshold plus at least three shared distinctive numbers marks a probable duplicate | 110 candidates, 2 probable duplicates |
| Independent versus same-pipeline validation | `validation_status` from text patterns with negation handling ("not an independent replication" is not independent) | same-pipeline 121, none 198, independent 0 |
| Knowability from information available at the time | `knowability`: an earlier family with an overlapping limitation, by certain date order (yes_from_history) or by recorded point dates (yes_from_history_probable); a data-scarcity statement (yes_from_data) | yes_from_history 9, probable 16, from data 6, no evidence 114, not applicable 174 |
| Missing or unreliable dates | documents and transcripts give exact dates; a file modification time only bounds a record from above | 177 exact, 205 upper bounds, 85 in bulk-edit groups, 1 with a later date mentioned in text, 1 undated |
| Machine-readable answer key | `benchmark_answer_key.jsonl`, one object per eligible family | 196 entries |

Recorded "knowable in advance = yes" is not taken at face value: 62 families recorded as knowable have no earlier evidence that the rules can find.

## 3. Thresholds come from the data, not from judgment

The question-clustering thresholds are calibrated on the 107 record pairs that the existing family review placed in the same study (`audit\cluster_calibration.json`). Same-study pairs separate from other pairs with an AUC of 0.993.

- **Merge threshold, 0.231:** the 25th percentile of same-study similarity.
- **Repeat threshold, 0.344:** the median.
- **Unrelated baseline, 0.103:** the 95th percentile of similarity between records of different studies.

Snapshots reuse these full-history thresholds. They depend only on family structure, not on outcomes, so no outcome information leaks into earlier snapshots through them.

## 4. Replay pool in one paragraph

Of 319 families, 196 are eligible. The exclusions are: 53 are not hypothesis tests, 52 evaluate internal app software, 15 hypotheses quote their own result numbers, 7 have no result, 16 fall below confidence 0.5, 1 fails the answer-key screen, and 1 is undated. A balanced main set of 78 (16 supported, 16 rejected, 16 untestable, 16 artifact, 14 uncertain; 15 adaptation tasks, at most 20%) and a 10-task pilot (2 per stratum) are selected automatically.

Every task has:
- a frozen statement written from the original hypothesis;
- the data available on that date;
- a frozen list of permitted memory records;
- a SHA-256 task hash.

Permitted records must certainly precede the task date. The task's own family, records that cite it, probable duplicates, and records sharing three or more distinctive numbers with it are all removed.

## 5. Prospective pool in one paragraph

40 candidate challenges for 2026-27 cover 10 categories, and each is written as an objective rather than a hypothesis. Each one is screened automatically:

- **Redundancy:** lexical similarity to any historical record at or above the repeat threshold.
- **Adaptation proximity:** similarity to lineup or in-game adaptation work at or above the merge threshold.
- **Feasibility:** expected validation units against the units required.
- **Decision value.**

"History-relevant" means the challenge involves a risk type (trait reliability, sparse lineup or matchup exposure, selection on runs or slumps, play-type labels, same-game leakage) that at least three failed or uncertain historical families carry as a recorded risk.

The result is 19 relevant, 19 irrelevant, 2 redundant and 32 eligible, with 12 selected (6 relevant, 6 irrelevant, at most 2 per category). The validation period (2027-01-31 to 2027-04-12) is locked in code. The fetcher requests the development window only, and it refuses the validation window until the claim registry verifies, is closed, and the date is after 2027-04-12.

## 6. How to run the pilot

```
$env:PYTHONIOENCODING="utf-8"; $env:PYTHONDONTWRITEBYTECODE="1"
$py = "$env:TEMP\supp_audit_venv\Scripts\python.exe"
& $py scripts\21_preflight.py configs\pilot.json
& $py scripts\20_run_experiment.py configs\pilot.json --confirm-spend
```

The pilot config uses one inexpensive model through OpenRouter: 10 tasks, three conditions and one seed, 30 runs in all. The cost estimate is about 0.14 USD, and the cap is 5 USD. Runs are resumable, and runs already saved are never repeated or overwritten. The report is written to `runs\pilot_v1\report.md`.

## 7. Deliberately not automated

- **Independent ground truth.** No script, and no second model, makes the answer key independent. Section 6 of `remaining_human_requirements.md` lists the minimum human checks.
- **Usefulness and novelty of prospective discoveries against the published literature.** Automated screens are provided as filters only.
- **The prospective agent sandbox** (code execution against 2026-27 development data) is specified in `experiment_runner_spec.md` but not built. The pilot does not need it, and building it before the pilot answers the main question would be premature.
