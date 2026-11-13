# Study 2, Phases 0 and 1: read-and-report and task construction

No model or API calls were made. Study 1 and Study 1b files, configs, tasks, prompts, answer key and run outputs are
unchanged. The one shared-code change is in `runner/experiment.py` (two optional config keys; see section 1).

## 1. Inventory of the harness

| Need | What exists | What was missing, and what was added |
|---|---|---|
| New tasks | `scripts/12_generate_replay_tasks.py` and `bench/tasks.py` built, before Study 1, a pool of 196 eligible replay tasks with frozen statements (`tasks/replay/RT-*.json`, each with a content hash) and a rule-based answer key (`benchmark_answer_key.jsonl`). A balanced main set of 78 was selected by a fixed priority rule; the ten Study 1 tasks were its pilot. | Nothing to build: Study 2 uses the 68 main-set tasks not used in Study 1 (decision of 2026-11-12). Copies with stricter memory exclusions are in `study2/tasks/` (section 5). |
| Snapshots | `runner/experiment.ensure_snapshot_v3` builds a task's memory_v3 snapshot from exactly its permitted records and refuses a snapshot whose records differ. Snapshots existed only for the ten Study 1 tasks. | The runner read tasks only from `tasks/replay` and snapshots only from `memory_v3/snapshots`. Added optional config keys `task_dir` and `snapshot_dir`; without them every path is as before (test: `tests/test_study2.py`). Study 2 snapshots were built under `study2/memory_v3/snapshots`. |
| Gold sets | The committed Study 1b rule (`study1b/gold_rule.md`) and its script `study1b/propose_gold.py` (hard-coded to the ten tasks). | `study2/gold.py`, the same steps as a function. It reproduces the rule-proposed Study 1b lists on all ten Study 1 tasks before it is applied to Study 2. |
| Conditions A, B, O | Protocol 3 in `runner/agent.py` and `runner/tools_v3.py`: A (no memory), B (document retrieval), O (oracle: the frozen gold list through the same tool). O does not read scope annotations. | The runner requires an annotation file for O; `study2/scope_annotations_none.json` is empty. |
| Analysis | `analysis_fixes/recompute_and_match_study1.py` (Study 1) and `study1b/analyze_study1b.py` (Study 1b), each hard-coded to ten tasks. | `study2/analysis.py`, one script for everything (section 2). |
| Preflight | `scripts/21_preflight.py` handles O and OS with Study 1 comparators. | Not run (it contacts the API key endpoint). It may need small changes for a study with its own A and B and no comparators; that is Phase 3 work. |

## 2. Reproduction of the published tables

`python study2/analysis.py reproduce` rescores all 450 Study 1 and 270 Study 1b raw runs, re-audits retrieval, and
compares 161 published numbers with the recomputed values. **161 of 161 match** (`study2/phase0/reproduce_output.txt`,
`reproduce_checks.csv`). The checks cover:

- Study 1: the primary table (balanced accuracy and B−A and C−A with CIs and p for five models), the Holm value, the strict and valid-only tables, the invalid counts, the 300-pair tally, and the Appendix C retrieval counts.
- Study 1b: O and OS balanced accuracy, O−A with CIs, the Holm range, the pooled per-task rates for RT-012, RT-147 and RT-179, invalid runs, and cost.

The Study 2 analysis uses the same functions (`load_rows`, `cells`, `ba`, `contrast`, `tally`), with the task weights
computed from the share of flag tasks (for ten tasks this gives Study 1's 1/0.8 and 1/1.2 exactly).

One wording point for the paper (not edited, because the paper is outside Study 2 work): "Fifteen of 270 runs were
invalid and two had no scorable flag" can be read as 17 runs, but the two runs without a scorable flag are among the 15
invalid ones.

## 3. Audit parser fix and relevance definitions

- **Parser fix is in place.** `bench/retrieval_audit.py` parses plain-string risk codes (`_codes`) and reads memory_v3 graphs (risk-code edges and question edges). The pre-fix copy is frozen as `bench/retrieval_audit_study1.py`. The fixed audit reproduces the published Appendix C counts (section 2).
- **Relevance is fixed in code.**
  - `relevant_families`: the question tier, meaning same question cluster, precedents or same-question families named in the key, or TF-IDF similarity of at least 0.231 (`memory_v2.full_history_thresholds`).
  - `lesson_families`: the lesson tier, meaning untestable, artifact or uncertain families sharing an expected risk code.
  - File hash: `bench/retrieval_audit.py` sha256 `1968dab7072937610a9a0593552a6d8b1031543d4b1a5c705297f47c4fde7d79`.

## 4. A stronger "used" definition (proposed for Study 2; Study 1 numbers unchanged)

The current measure, `meaningfully_used`, is met when retrieval returned a relevant family, the output cites a
relevant family it saw, and the evidence-use text has at least 30 characters. In Study 1 it was met in 94% of runs where
retrieval succeeded, so it barely separates runs.

**Proposed: decision-linked use** (`study2/analysis.decision_linked_use`). A run counts only if both of these hold:

- a relevant family that appeared in the run's memory tool results is named in a field that carries the decision: `risks[].text`, `testability.blocking_constraints[].text`, or `historical_effect.explanation`;
- no status the output gives that family contradicts the family's recorded stratum.

On the Study 1 runs (new, descriptive, not published) it is met in 33 of the 47 B runs and 22 of the 35 C runs that
meet the current definition. It remains an automated text rule. In Phase 5, 30 codings are sampled for your hand check
(`study2/analysis/used_hand_check.csv`).

## 5. Task construction (Phase 1)

**Tasks.** The 68 tasks are the main replay set minus the ten Study 1 tasks:

- Strata: 14 each for untestable, supported, rejected and artifact, and 12 uncertain.
- Answer key: 28 should be flagged and 40 should proceed.
- Priors: 14 tasks have a prior same-question family in memory.
- Clusters: 60 question clusters.
- Size of permitted memory: 3 to 380 records, median 264.

**Answer-key rules.** These were written in code before Study 1 and never changed (`bench/tasks.py`): flag if and only
if the stratum is untestable or artifact. **Contestable keys:** all 12 uncertain tasks are keyed "proceed" by that
convention, the one RT-147 exposed. They stay in the primary analysis, and a sensitivity analysis drops them.

**Leakage checks.** `bench/tasks.py` already removed from each task's memory:

- the task's own family;
- records not certainly dated before the task;
- records that cite the task family in `related` or `notes`;
- probable-duplicate families;
- records sharing 3 or more distinctive result numbers, using the precomputed candidate list `audit/duplicate_candidates_raw.tsv` (110 pairs).

`distinctive_numbers()` is used twice: to screen task statements for the family's own result numbers, and, through the
precomputed list, for the 3+ rule. `study2/leakage_check.py` re-derives every rule independently and more strictly:

- citations are searched in every text field of the record;
- shared result numbers are counted over every record pair, ignoring calendar years.

**Leakage changes.** The citation check found nothing new. The all-pairs number check found 4 records in 3 tasks:

| Task | Removed record | Shared numbers |
|---|---|---|
| RT-024 | APPA-037, PAP-036 | 0.378, 0.438, 136 |
| RT-063 | APPA-046 | 466, 539, 95.3 |
| RT-070 | TMP-031 | 0.11, 0.14, 0.21 |

They were removed in the Study 2 copies, and the originals in `tasks/replay` are untouched.
`study2/build_tasks.py` re-checks every Study 2 task and stops the build on any violation; `tests/test_study2.py`
repeats the check. Judgment call: TMP-031's three shared numbers are small, common-looking values. The rule removes it
anyway, since the rule was not tuned after seeing results.

**Gold families.**
- Computed by `study2/gold.py` (the Study 1b rule) on each Study 2 snapshot, by code only: no model, no manual additions.
- Coverage: 50 tasks have gold families (42 have four), and 18 have none (8 of the 12 uncertain tasks among them).
- Composition: 186 gold slots, 48 question-tier and 138 lesson-tier.
- Checked: every gold family is in the task's memory and is never the task's own family.
- Files: `study2/gold_families_frozen.json`, with details in `gold_details.json`.

**Builder/subject overlap.**
- The only model-made input to the answer key is the "consistency screen by the building model" in `audit/answer_key_flags.csv`.
- That model was the Cursor coding agent that built the harness in this project's chat, Claude Opus (Anthropic). This is recorded from the chat history, which shows Opus in use during the build; the screen's file does not name the model.
- The screen flagged one family, SF-APPA-046, which was excluded from the pool and is in no task.
- The same agent wrote the task generator, the adjudication rules and the gold rule, and the current agent (also Claude Opus) wrote the Study 2 build.
- None of the four subject models took part. Haiku 5.5 is from the same developer as the builder, which is disclosed in the prereg.

**Frozen files (sha256).**
- `study2/task_manifest.json`: `eaf1d22fe28bf9aa517c31ed297b3c13346e948e90fdb13565e171f044193bea`. It holds per-task task hashes, source-task hashes, snapshot fact hashes, answer-key entry hashes and gold lists.
- `study2/gold_families_frozen.json`: `e11f83fb424dbc0100079cf45ef3ff4ca629bfb1a493b47c465a5b104ddfdbbd`.
- `benchmark_answer_key.jsonl`: `cdb876cb2d22b0e72ad1fc8c93e406a5b0ef32138d8ebc1462f465fb409819d0`.
- Build report: `study2/build_report.md`.

## 6. Tests

`tests/test_study2.py` (12 tests) checks the following, and all pass:

- the default paths;
- the Study 2 paths;
- the task hashes, and that the originals are untouched;
- every exclusion rule;
- that snapshots match the permitted records and fact hashes;
- that the gold lists equal a fresh application of the rule;
- the manifest file hashes;
- the configs.

The full suite has 158 passing and 2 failing. Both failures predate Study 2: `test_cost_cap`, left alone as instructed,
and `test_study_cap_is_80_percent_of_budget`, which expects Study 1b's original $8 stop rather than the approved $25
amendment.
