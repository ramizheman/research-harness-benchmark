# Study 1 rerun with embedding retrieval: preregistration

Status: **approved 2026-11-15 (see section 12).** Everything below is a plan or a hypothesis. No result is described here.

## 1. Question

Study 1 found no reliable benefit of memory retrieved by keyword search. Does it matter if the retrieval is done with a standard embedding retriever, returning more studies per call?

- **Q1.** With embedding retrieval (B-embed, C-embed), is decision accuracy higher than with no memory (A)?
- **Q2.** Is accuracy under embedding retrieval different from accuracy under the keyword retrieval of Study 1, for the same condition?

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

## 2. Design

| Item | Plan |
|---|---|
| Tasks | The ten Study 1 tasks (`configs/study1_embed.json`). |
| Conditions | B-embed and C-embed are run. **A is not rerun**: it does not use search and is taken from the original Study 1 runs, as are the keyword B and C comparators. |
| Models | The five Study 1 models: Gemini 2.5 Flash, Claude Haiku 5.5, gpt-oss-20b, DeepSeek V4 Pro, Claude Sonnet 5.5. Settings unchanged. |
| Seeds | 1, 2, 3. |
| Runs | 5 models x 10 tasks x 2 conditions x 3 seeds = 300. |
| Order | gpt-oss, Haiku, Gemini, DeepSeek, Sonnet; shuffled within each model and seed (order seed 20261116). A spend stop therefore cuts Sonnet first, then DeepSeek. |

## 3. Outcome and scoring (unchanged from Study 1)

Flag rule `bench.scoring.score_replay`; a run is correct when its flag matches `should_flag_before_running`. Balanced accuracy is the mean of the flag-task and no-flag-task correct rates, at the task level, with seeds averaged within task. Scoring rules: primary (no scorable flag counts as wrong), strict, valid-only.

## 4. Contrasts and tests

All by `study2/analysis.py study1embed` (the script that reproduces all 161 published Study 1 and 1b numbers; its Study 1 reproduction was re-run before the freeze and matched).

- **Primary (Q1).** For each of five models: B-embed minus A and C-embed minus A. Percentile bootstrap 95% CI over tasks (10,000 resamples, seed 0), two-sided sign-flip p, Holm across the ten contrasts, with Study 1 task weights.
- **Secondary (Q2).** B-embed minus B-keyword and C-embed minus C-keyword, per model, with Holm across five models within each condition.
- **Pooled.** The same four contrasts pooled over models (per-task difference is the mean over models), Holm across the four.
- **Descriptive.** Run-level tally (fixed, broke, same correct, same wrong) of embedding versus A; the retrieval audit of `bench/retrieval_audit.py` for B-embed and C-embed beside the keyword rates; invalid outputs; cost.

Ten tasks cannot detect effects below about 0.3 in balanced accuracy. All results are descriptive, and no difference detected is not evidence of no effect.

## 5. Decision rules (fixed now)

- **Embedding retrieval helps (per model):** the embedding-minus-A difference is positive and its 95% CI lower bound is above 0.
- **Embedding retrieval harms:** the CI upper bound is below 0.
- **Otherwise:** no detectable difference.
- The same words apply to embedding minus keyword. Nothing is called a finding unless it meets these rules after Holm adjustment. The paper reports every contrast, including those that do not.

## 6. Budget and stopping

Budget $18; the runner stops before any new run once recorded spend reaches 80% ($14.40; `budget_usd` 18, `stop_fraction` 0.8, `max_cost_usd` 14.4). It also stops on an unknown cost or after 3 consecutive API errors. The expected total is about $12 (an assumption: the keyword B and C runs cost about $7 in total, and I assume about 1.8 times that for ten results per call; one smoke run of gpt-oss, about $0.002, showed no surprise). If the stop binds, the runs on disk are analysed and the incomplete models reported as incomplete. The supervisor `scripts/supervise.py` retries an API-error run at most twice and keeps the failed file.

## 7. Disclosures

- **The relevance labels in the offline check come from the audit rule** (question and lesson tiers, plus one manual addition) that Rami reviewed. They are automated and not independent human judgments.
- **Post-hoc design.** The retriever was chosen after Study 1 and 1b results were known and after the offline check. The runs below are a rerun with a changed retriever, not a replication under the same conditions.
- **Three settings changed together** (embedding method, 10 results instead of 4, larger result cap). If results differ from Study 1, this design cannot say which change caused it.
- **Model drift.** The keyword-search comparators were run on 2026-11-10 and 11 (Study 1) and 2026-11-12 to 14 (Study 1b, Study 2 pilot). Providers can change models between dates.
- **Builder/subject overlap and automated key:** as in Study 1. Claude Haiku 5.5 and Claude Sonnet 5.5, subject models, are from the same developer as the builder.
- **A smoke run** (gpt-oss, RT-147, B and C, seed 1) checked the code before the full run. It is not analysed.
- **Graph embedding search (C) is untested offline** (see section 0).

## 8. Rami's prediction

Overall prediction: Handing the agent the relevant past studies moves every model toward the answer key, both against no archive and against the model searching the archive itself.

Basis: Handing over past studies focuses the LLM on the right information. There is no similar but irrelevant content to confuse it.

| Model | O vs A (help / hurt / no clear difference) | O vs B (help / hurt / no clear difference) |
|---|---|---|
| Pooled | help | help |
| Gemini | help | help |
| DeepSeek | help | help |
| Haiku | help | help |
| gpt-oss | help | help |

These are the ten calls Rami made for Study 2 before any Study 2 run, written on 2026-11-15 after the Study 1 and 1b results. They are copied unchanged. No separate prediction was recorded for the embedding reruns of conditions B and C in Study 1.

## 9. Frozen inputs (sha256)

| File | sha256 |
| `configs/study1_embed.json` | `4c33483670d8179aae6ebc1c2395afdeeca2b9315367f066dca02f0b28487c72` |
| `runner/tools_v3.py` | `27d9c16cff4fbd25d496b7dd0146db73c9fc24f9f145238372e430acd036e629` |
| `runner/experiment.py` | `ecd5a6ad0242163a74b281084c734b216b49380c470fa928f2930e5d8037103c` |
| `runner/agent.py` | `aa99acd71524799fc767b8d2a379ca08a58447f2a011ec2e96d2da990aa113c4` |
| `bench/scoring.py` | `437fa27bdb5aac037042a1b61f9a6ad9e2f0bea87e4ee1007ca95ba6f0537441` |
| `bench/retrieval_audit.py` | `1968dab7072937610a9a0593552a6d8b1031543d4b1a5c705297f47c4fde7d79` |
| `bench/stats.py` | `8a86e3eb5ad7095501920119d0917f0c9437b326c286d9d309649397919612b8` |
| `study2/analysis.py` | `a13ce5f95c3846d47e96b2e119ea605d3f575200e08d5b4285b3ce3b75182dfd` |
| `benchmark_answer_key.jsonl` | `cdb876cb2d22b0e72ad1fc8c93e406a5b0ef32138d8ebc1462f465fb409819d0` |
| `scripts/supervise.py` | `8dbb1065b5326cb7affbc5b7e27f38f50d063bcc89df3b52dff448f8a9779d5e` |
| `retrieval_test/report.md` | `0826f33fb6e957b031db7b2a531a610eb778f6b967431d0d47285d47194bcbb4` |

## 12. Approval

Approved by: Rami Zheman    Date: 2026-11-15

Recorded by the coding assistant on Rami's written instruction in chat on 2026-11-15: "RECORD MY PREREG. SAME FUCKING ANSWERS AS LAST TIME. PUT MY NAME AND DATE ON THERE. DO STUDY 1 AND EDIT THE FRUCKING PAPER 1. THEN DO STUDY 2. JUST DO IT." That instruction followed Rami's "YES" to the retriever and result-cap recommendation (bge-small embeddings, 10 results, result cap raised). Rami did not read this text before the runs started; he asked to be left to sleep. The assistant wrote it from the chat record, and the answers in section "Rami's prediction" are copied unchanged from the Study 2 preregistration he approved on 11/15/2026.
