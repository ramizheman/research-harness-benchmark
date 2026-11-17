# Corpses and Corpora: Can an AI Learn From a Graveyard of Failed Basketball Studies?

This repository holds the code, archive, saved runs and analysis behind the working paper *Corpses and Corpora* (Rami Zheman, November 2026). The paper tests whether giving an AI agent the record of an analyst's earlier basketball studies, failures included, helps it decide whether a new research idea is worth running.

Paper source: `paper/ssrn_research_memory_basketball.tex`.

## What was tested

Five language models judged ten of my past research ideas, each as of the day it was proposed. For each idea the model decided whether the study should go ahead or stop. The decision was graded against the recorded outcome of the study when it was later run. Retrieval was restricted to earlier studies only: each task has its own date-restricted snapshot of the archive.

| Experiment | What the models had | Runs |
|---|---|---|
| Study 1 (primary) | No archive; keyword document search; keyword graph search | 450 (5 models x 10 tasks x 3 seeds x 3 conditions) |
| Embedding extension | Embedding document search; embedding graph search | 300 (no-memory condition not repeated) |
| Study 1b | The relevant studies handed over directly, with and without short notes on when each lesson applies | 270 |

## Main results

- Across 300 paired comparisons, memory fixed 47 wrong decisions and broke 46 right ones. Pooled accuracy did not improve.
- Keyword search returned the closest earlier study in 2 of 45 runs. Embedding search returned it in 18 of 45 (document) and 22 of 45 (graph) runs, and accuracy still did not improve.
- Handing over the relevant studies raised accuracy for four of five models, but with ten tasks no difference was statistically distinguishable from zero.
- Models generally reproduced the recorded outcome statuses of the studies they cited, but did not reliably judge when a study applied to a new idea. The paper's two paired cases (RT-012 and RT-147) show one data-quality record bearing on two ideas with opposite correct answers.

See the paper for tables, uncertainty ranges, and limitations. Ten tasks are too few to support broad claims; the paper proposes a 60 to 100 task follow-up.

## The archive

The archive is one analyst's accumulated research program: 319 study families (384 merged records) from four NBA seasons (2022-23 through 2025-26), covering ten topics. Outcome statuses: 57 supported, 57 rejected, 49 untestable, 44 artifact, 52 uncertain. The remaining 60 families fall outside those five groups.

The answer key stops an idea when the task study's recorded outcome status was untestable or artifact, and lets it go ahead for the other statuses. It uses the outcome-status field, not the secondary failure-mechanism label.

## Where things are

| Path | Content |
|---|---|
| `paper/` | The paper source |
| `docs/paper1_supplement/` | Supplement files the paper links to (development record of the pilots, retrieval tables) |
| `bench/tasks.py`, `scripts/12_generate_replay_tasks.py` | Task selection (seed 20261110) |
| `bench/scoring.py`, `bench/retrieval_audit.py` | Scoring rule and retrieval audit, including the risk-code parsing correction |
| `runner/agent.py` | The runner and the prompts used in the runs |
| `memory_v2/full/documents/families/` | The 319-family archive |
| `memory_v3/snapshots/` | Per-task snapshots, one manifest and fact hash per task |
| `configs/` | Run configurations |
| `runs/` | Saved run files for the pilots, Study 1, Study 1b, and the embedding search |
| `study1b/prereg_1b.md`, `study1_embed/prereg.md` | Preregistrations for Study 1b and the embedding search. Study 1 has no separate preregistration file |
| `study2/analysis.py`, `analysis_fixes/recompute_retrieval_audit.py` | Analysis scripts that reproduce the paper's tables |

`README_archive_build.md` is the earlier README written when the archive was first assembled, before any benchmark run. It documents how the archive and inventory were built and is kept for provenance. Its statement that the benchmark had not been run is out of date.

## Status of the data-quality audits

- **Outcome labels are rule-based classifications, not independent ground truth.** The benchmark measures agreement with that classification. No independent human double-coding of the labels is included in this repository.
- **Conflicting family verdicts.** In 20 of the 319 families the member records disagreed on status. Family-level statuses are set by the rule-based adjudication in `bench/adjudicate.py` (summary: `audit/adjudication_summary.md`), which its own documentation states is not independent human adjudication.
- **Dates.** Of 384 records, 177 are dated from a date in the document or a chat transcript timestamp. 205 are dated only by file modification time, which bounds the work from above, because a file can be edited after the work it records. One record is undated and one mentions a later date. A record entered a task's snapshot only if it was certainly before the task date, so a modification-time date can wrongly remove a record but not wrongly add one, except where a task's own record was itself dated by modification time.
- **Possible duplicates.** The 319 families may still contain duplicates reported with different rounding or wording.
- **Relevance rule.** The paper documents a risk-code parsing error that was corrected, one declared manual addition (FAM:SF-CHT-025), and at least one remaining misclassification.

## Limitations to keep in mind

- Ten tasks, five models, one analyst's archive, no human baseline.
- The temporal restriction applies to the retrieved archive, not to the models' pretrained knowledge. The runs were retrospective.
- The Study 1b scope-annotation comparison is exploratory: the annotator knew the answer key and the Study 1 results.
