# Study 2 preregistration, version 2: oracle retrieval on 68 new tasks, with embedding retrieval for condition B

Status: **approved 2026-11-15 (see section 12). Replaces `study2/prereg.md` (version 1, which used keyword search for B).**

## Amendment from version 1

Version 1 was approved on 11/15/2026 and the full run was started. It was stopped on 2026-11-15 after 209 of 816 runs (Gemini only, keyword search for B), at Rami's instruction, because condition B used TF-IDF keyword search. Those runs stay on disk in `runs/study2_v1/` and are not part of this analysis. They are reported only as a keyword-search pilot. Changes in version 2:

1. Condition B uses embedding retrieval (bge-small-en-v1.5, 10 results per call, 14,000-character result cap); section 0 below states it in full. Conditions A and O are unchanged.
2. New config `configs/study2_embed.json` and output `runs/study2_embed_v1/`. All 816 runs are rerun, including A and O, so that every run shares one config and one code version.
3. Budget $14, stop at 80% ($11.20).
4. Predictions, tasks, gold families, models, seed, scoring, tests and decision rules are unchanged.

## 0. Retriever (fixed before any embedding run)

| Item | Setting |
|---|---|
| Method | Embedding similarity. Model `BAAI/bge-small-en-v1.5` (sentence-transformers, CPU, unit-length vectors, cosine). Queries use the model's retrieval instruction prefix; documents do not. |
| Condition B | The full text of each family document is embedded (the model truncates long text to its 512-token limit). The request (query, concepts and methodological questions joined, as before) is embedded and families are ranked by cosine. No relevance threshold: the top 10 are always returned, so this search never returns an empty list. |
| Condition C | The same graph search as Study 1, with TF-IDF replaced by the same embeddings: concept nodes and family question-and-hypothesis text are embedded; the top 8 concepts and top 4 families by cosine are the seeds (no positive-score filter). Edge weighting, one-step traversal and tie-breaking are unchanged. Top 10 families are returned. |
| Results per call (`k`) | 10 (Study 1 and 1b used 4). Follow-up search tools use the same k. |
| Result cap | 14,000 characters per tool result for B and C (Study 1 used 6,000). The 10 family views of about 1,000 characters each fit. Conditions A and O are unchanged. |
| Everything else | Study 1 protocol 3, prompts, tools, tool-call and repair limits, token and time budgets, family views (950 characters), models and settings, tasks, snapshots, answer key and scoring. |

**Why this retriever.** Study 1 used TF-IDF keyword search and returned at most four families. No embedding retriever was tested at design time, and the repo records no reason for the keyword choice. An offline check (`retrieval_test/report.md`, run after Study 1 and without calling any model) reranked the saved queries with three local embedding models, BM25 and a hybrid. At k = 4 bge-small found the closest earlier study on 9 of 45 queries against 1 of 45 for keyword search, and at k = 10 on 16 of 45. It found a lesson-tier analogue less often than keyword search at k = 4 (25 of 60 against 34 of 60) and also less often at k = 10 (32 of 60 against 49 of 60). Rami chose bge-small alone, k = 10, and the larger cap on 2026-11-15. The choice used retrieval recall on the snapshots and the space available per result. It did not use any model's decisions.

**Not tested offline.** The offline check covered document search (B). The graph search (C) with embeddings was never evaluated before this run.


Everything below is a plan or a hypothesis. No result is described here, and none will be called a finding unless it
meets the decision rules in section 6.

## 1. Question

Study 1b, on ten tasks, found higher accuracy with oracle retrieval for four of five models, but no difference was
detectable. Study 2 asks the same question on tasks not used before.

**Q1.** On 68 new tasks, does giving the agent the relevant prior families (condition O) improve the decision about
whether a proposed study should proceed, compared with no memory (A) and with embedding-based document retrieval (B)?

- H1: accuracy is higher under O than under A.
- H2: accuracy is higher under O than under B.

## 2. Design

| Item | Plan |
|---|---|
| Tasks | 68: the main replay set (built and keyed before Study 1) minus the ten Study 1 tasks. Frozen copies are in `study2/tasks/`; the manifest is `study2/task_manifest.json`. |
| Strata | 14 untestable, 14 supported, 14 rejected, 14 artifact, 12 uncertain. 28 should be flagged, 40 should proceed. |
| Conditions | A (no memory), B (embedding document retrieval; see section 0), O (the frozen gold families through the same retrieval tool, as Study 1b). Protocol 3, prompts, tools and budgets as in Study 1 and 1b. |
| Gold families | The Study 1b rule (`study1b/gold_rule.md`) applied by `study2/gold.py`, by code only. 50 tasks have gold families; 18 have none, and on those O gives the agent the same empty list as A. |
| Models | Gemini 2.5 Flash, DeepSeek V4 Pro, Claude Haiku 5.5, gpt-oss-20b. Settings are copied unchanged from `configs/study1b.json`. Sonnet 5.5 is not run. |
| Seeds | Seed 1 only. |
| Runs | 68 Ã— 3 Ã— 4 = 816 (`configs/study2_embed.json`). |
| Order | Gemini, DeepSeek, Haiku, gpt-oss, with tasks and conditions shuffled within each model (order seed 20261113). |
| Condition S | Not run. It would need new scope annotations for 186 gold slots, written by someone who knows the answer key (the Study 1b weakness), so it needs its own preregistration. |

## 3. Outcome and scoring (unchanged from Study 1)

- **Flag rule.** `bench.scoring.score_replay`. A run counts as a flag if any of these holds:
  - its decision is "do not proceed";
  - its stated testability probability is below 0.5;
  - its predicted probability of an untestable or artifact outcome exceeds 0.5.
- **Correct.** A run is correct when its flag matches `should_flag_before_running`.
- **Per-task rate.** Each task's correct rate is its single seed-1 run.
- **Balanced accuracy.** The mean of the flag-task rate and the no-flag-task rate.
- **Scoring rules.**
  - primary: no scorable flag counts as wrong;
  - strict: an invalid output counts as wrong;
  - valid_only: invalid or unscorable runs are dropped.

## 4. Contrasts and tests

All analysis is by `study2/analysis.py study2`. This is the script that reproduces all 161 published Study 1 and 1b
numbers.

- **Task as the unit.** Per-task differences are weighted by 1/(2p) for flag tasks and 1/(2(1 âˆ’ p)) for no-flag tasks, with p = 28/68. Their mean equals the balanced-accuracy difference.
- **Primary.** Pooled O âˆ’ A and pooled O âˆ’ B. Each task's difference is the mean over the four models.
  - 95% percentile bootstrap CI over tasks (10,000 resamples, seed 0).
  - Two-sided sign-flip p (20,000 sign draws, seed 0).
  - Holm across the two primary contrasts.
- **Secondary.** O âˆ’ A and O âˆ’ B for each model, with Holm across the four models within each contrast. A model whose runs are incomplete is analyzed on the tasks where it has all three conditions, and this is reported.

## 5. Power

Minimum detectable effects at 80% power were computed by `study2/analysis.py power` (`study2/power.json`). They use the
spread of seed-1 per-task differences in the Study 1 and 1b runs (ten tasks, four models), rescaled to 68 tasks:

| Contrast | MDE, pooled (Î± = 0.025, Holm first step) | MDE, per model (Î± = 0.0125, Holm first step) |
|---|---|---|
| O âˆ’ A | 0.14 | 0.20 (Haiku) to 0.26 (Gemini) |

- The O âˆ’ B spread could not be estimated from ten tasks (Haiku's seed-1 O and B runs agreed on all ten), so the O âˆ’ A values are the planning values for O âˆ’ B too.
- Study 1b's O âˆ’ A estimates were 0.01 to 0.26. Study 2 can therefore detect a pooled effect of about the Study 1b average size, but per model only effects as large as the largest Study 1b estimate.
- If O helps only where there are gold families, the effect over all 68 tasks is about 50/68 of the effect on those 50.

## 6. Decision rules (fixed now)

**For H1, pooled O âˆ’ A:**
- **Supported:** the difference is above 0, the 95% CI lower bound is above 0, and the Holm-adjusted p is below 0.05.
- **No meaningful benefit:** the 90% bootstrap CI lies inside (âˆ’0.10, +0.10) (`bench.stats.tost`, margin 0.10). This outcome would count against the Study 1b direction.
- **Otherwise:** inconclusive.

**For H2, pooled O âˆ’ B:** the same three rules.

**Per model:**
- "Oracle helps": O âˆ’ A above 0, CI lower bound above 0, and Holm-adjusted p below 0.05.
- "Oracle harms": CI upper bound below 0.
- Otherwise: no detectable difference.

**Reading the combinations (stated in advance):**

| H1 (O vs A) | H2 (O vs B) | What it would suggest |
|---|---|---|
| Supported | Supported | Retrieval quality limits what memory adds. |
| Supported | Not supported | Search already captures most of what the gold families add. |
| No meaningful benefit | Any | Giving the agent the right families does not detectably improve this decision, which points to applicability or representation rather than retrieval. |
| Inconclusive | Any | The study cannot separate these. |

## 7. Secondary analyses (descriptive; no claims beyond section 6)

1. **Sensitivity.** The primary contrasts under the strict and valid_only rules, and on these subsets:
   - without the 12 uncertain tasks (contestable keys);
   - the 50 tasks with gold families;
   - the 18 tasks without gold families, as a noise reference, since O is A there.
2. **Run-level tally.** Same model, task and seed: O versus A, B versus A, and O versus B, counted as fixed, broke, same correct or same wrong.
3. **Retrieval audit for B and O.** Fixed definitions in `bench/retrieval_audit.py`. For each model, the share of runs where a relevant family was surfaced, returned, "meaningfully used" (Study 1 definition), and decision-linked (the stronger definition in `study2/phase0_report.md`, section 4).
4. **Hand check.** 30 runs coded as used under either definition are sampled (seed 20261112) into `study2/analysis/used_hand_check.csv`. Rami codes them by hand, and agreement with each automated definition is reported.
5. **Validity and cost.** Invalid outputs, unscorable flags, stop reasons and cost per model.
6. **Recompute-and-match.** The rescored flags compared with the runner's `scores.csv`.

## 8. Budget and stopping

**Budget.** $14, covering every call. The runner stops at 80% ($11.20: `budget_usd` 14, `stop_fraction` 0.8,
`max_cost_usd` 11.2). It also stops if any finished run has unknown cost, or after 3 consecutive API errors.

**Cost arithmetic** (`study2/cost_estimate.txt`). Measured mean cost per run (Study 1 A and B, Study 1b O) Ã— 68 tasks:

| Model | A | B | O | Total |
|---|---|---|---|---|
| Gemini | 0.85 | 1.16 | 1.04 | 3.05 |
| DeepSeek | 0.76 | 1.17 | 0.98 | 2.91 |
| Haiku | 0.17 | 0.27 | 0.23 | 0.67 |
| gpt-oss | 0.03 | 0.03 | 0.04 | 0.10 |
| **Total** | | | | **$6.72** |

- Version 1's expected total was $6.72. Version 2 expects about $9 (an assumption: B costs about 1.8 times its keyword cost with ten results per call). That is about 64% of the $14 budget. That is $0.033 per task-condition across the four models.
- No cuts are planned. If the $11.20 stop binds, models run in order, so gpt-oss is cut first, then Haiku.
- The high scenario, where every run costs as much as the most expensive measured task, is $8.43, which would reach the stop. Because models run in order, a stop would cut gpt-oss first, then Haiku, keeping Gemini and DeepSeek.
- If the stop binds, the analysis uses the completed runs and reports what was cut.

**Time.** About 13 hours if run in one process (mean measured wall time; DeepSeek about 9 of those hours).

**Procedure.**
1. Gate check.
2. Preflight (no model calls).
3. Smoke test: a single gpt-oss run on RT-147 in conditions B and C with the embedding retriever (about $0.002), plus the version 1 smoke test, which used keyword B. Not analysed.
4. Full run (Rami asked that it start without waiting), with no changes during it. Any amendment is recorded here, with its reason, before it takes effect.

## 9. Disclosures

- **The relevance labels in the offline check come from the audit rule** (question and lesson tiers, plus one manual addition) that Rami reviewed. They are automated and not independent human judgments.
- **Post-hoc design.** The retriever was chosen after Study 1 and 1b results were known and after the offline check. The runs below are a rerun with a changed retriever, not a replication under the same conditions.
- **Three settings changed together** (embedding method, 10 results instead of 4, larger result cap). If results differ from Study 1, this design cannot say which change caused it.
- **Model drift.** The keyword-search comparators were run on 2026-11-10 and 11 (Study 1) and 2026-11-12 to 14 (Study 1b, Study 2 pilot). Providers can change models between dates.
- **Study 2 version 1 was stopped part-way** (209 runs, keyword B). Version 2 was written after seeing no results from those runs; they were not analysed.

- **Sonnet 5.5 excluded.** This is for cost. It had the highest Study 1 accuracy without memory.
- **Single seed.** Each task-condition cell is one run, so per-task results are noisy. The no-gold tasks show how large differences between identical conditions can be.
- **Builder/subject overlap.**
  - The harness, task generator, adjudication rules and gold rule were written by the Cursor coding agent, Claude Opus (Anthropic). That identification is inferred from this project's chat history, not recorded in the screen's own file.
  - That agent's answer-key "consistency screen" excluded one family, which is in no task.
  - The Study 2 build was done by Claude Opus as well.
  - None of the four subject models took part. Claude Haiku 5.5, a subject model, is from the same developer as the builder.
- **The answer key is automated** (rule-based adjudication of extracted records), not independent human adjudication. All 12 uncertain tasks are keyed "proceed" by convention.
- **Relevance coding is automated.**
  - Question relevance uses question clusters and a TF-IDF threshold; lesson relevance uses automated risk-code tags.
  - Some relevant prior work may be missed, and some listed families may be weakly relevant.
  - The Study 1 "used" measure is weak (met in 94% of successful retrievals). The decision-linked measure is stricter but still a text rule.
- **Gold coverage is uneven.** 18 tasks have no gold families, 8 of them uncertain tasks, and 138 of the 186 gold slots are lesson-tier.
- **Stricter leakage rule.** It removed 4 records from 3 tasks' memory (RT-024, RT-063, RT-070) relative to the original frozen tasks.
- **Task selection.** The tasks are not a random sample. The main set was chosen by a priority rule (confidence, self-contained statement, reliable date) with stratum quotas, and the Study 1 pilot was drawn from it first.
- **Prior knowledge.** The design and the gold rule were fixed after Study 1 and 1b results were known, but before any Study 2 run. The predictions below are written with that knowledge.
- A Study 1b test, `test_study_cap_is_80_percent_of_budget`, still expects the original $8 spend stop rather than the approved $25 amendment. That failure is known, and the test is left unchanged.

## 10. Rami's prediction

Overall prediction: Handing the agent the relevant past studies moves every model toward the answer key, both against no archive and against the model searching the archive itself.

Basis: Handing over past studies focuses the LLM on the right information. There is no similar but irrelevant content to confuse it.

| Model | O vs A (help / hurt / no clear difference) | O vs B (help / hurt / no clear difference) |
|---|---|---|
| Pooled | help | help |
| Gemini | help | help |
| DeepSeek | help | help |
| Haiku | help | help |
| gpt-oss | help | help |

Predictions written on 2026-11-15, after the Study 1 and 1b results and before any Study 2 run (version 1 or 2). The ten calls were selected by Rami. The overall sentence restates those calls. The basis is Rami's own words. They are unchanged from version 1.

## 11. Frozen inputs (sha256)

| File | sha256 |
|---|---|
| `study2/task_manifest.json` | `eaf1d22fe28bf9aa517c31ed297b3c13346e948e90fdb13565e171f044193bea` |
| `study2/gold_families_frozen.json` | `e11f83fb424dbc0100079cf45ef3ff4ca629bfb1a493b47c465a5b104ddfdbbd` |
| `study2/scope_annotations_none.json` | `f1cb43d5fbcf1526efaeaf76d0669583323e8042ed4e500d4847739f6052034f` |
| `benchmark_answer_key.jsonl` | `cdb876cb2d22b0e72ad1fc8c93e406a5b0ef32138d8ebc1462f465fb409819d0` |
| `configs/study2_embed.json` | `60434ddde9622afadc49647920042da7a3c947446d34439aca5867a4bb922b6a` |
| `study1b/gold_rule.md` | `6351c76a3e307a4c4987b56aa40b6e71fe233dbf17e3ca58c8b2e29c9aec62a1` |
| `bench/scoring.py` | `437fa27bdb5aac037042a1b61f9a6ad9e2f0bea87e4ee1007ca95ba6f0537441` |
| `bench/retrieval_audit.py` | `1968dab7072937610a9a0593552a6d8b1031543d4b1a5c705297f47c4fde7d79` |
| `bench/stats.py` | `8a86e3eb5ad7095501920119d0917f0c9437b326c286d9d309649397919612b8` |
| `runner/agent.py` | `aa99acd71524799fc767b8d2a379ca08a58447f2a011ec2e96d2da990aa113c4` |
| `runner/tools_v3.py` | `27d9c16cff4fbd25d496b7dd0146db73c9fc24f9f145238372e430acd036e629` |
| `runner/experiment.py` | `ecd5a6ad0242163a74b281084c734b216b49380c470fa928f2930e5d8037103c` |
| `study2/analysis.py` | `a13ce5f95c3846d47e96b2e119ea605d3f575200e08d5b4285b3ce3b75182dfd` |
| `scripts/supervise.py` | `8dbb1065b5326cb7affbc5b7e27f38f50d063bcc89df3b52dff448f8a9779d5e` |

## 12. Approval

Approved by: Rami Zheman    Date: 2026-11-15

Recorded by the coding assistant on Rami's written instruction in chat on 2026-11-15: "RECORD MY PREREG. SAME FUCKING ANSWERS AS LAST TIME. PUT MY NAME AND DATE ON THERE. DO STUDY 1 AND EDIT THE FRUCKING PAPER 1. THEN DO STUDY 2. JUST DO IT." That instruction followed Rami's "YES" to the retriever and result-cap recommendation (bge-small embeddings, 10 results, result cap raised). Rami did not read this text before the runs started; he asked to be left to sleep. The assistant wrote it from the chat record, and the answers in section "Rami's prediction" are copied unchanged from the Study 2 preregistration he approved on 11/15/2026.
