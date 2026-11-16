# Offline retrieval test

Read-only on saved Study 1 runs and snapshots. No paid API call. No paper, run, config, snapshot, or Study 2 file was edited.

Models, all local, CPU, seeds `torch` 0 and `numpy` 0: `sentence-transformers/all-MiniLM-L6-v2`, `BAAI/bge-small-en-v1.5` (query prefix "Represent this sentence for searching relevant passages: "), `intfloat/e5-small-v2` (prefixes `query:` and `passage:`). Package versions: sentence-transformers 6.3.0, torch 2.15.0+cpu, rank-bm25 0.2.2, scikit-learn 1.9.1, transformers 5.23.0. Hybrid is reciprocal rank fusion (constant 60) of TF-IDF and that embedding.

## 1. Plain-language answer

A standard embedding retriever would have found the closest earlier study more often than the keyword search Study 1 used, but not often. On the 45 document-search queries, keyword search put that study in the top 4 once. The best embedding model here, bge-small, did so 9 times. The other two embedding models did so 4 times and 1 time. Mixing keyword search with embeddings did not beat keyword search. Showing 20 studies instead of 4 helps more than changing the method: keyword search then hits the closest study in 16 of 45 queries, and bge-small in 29 of 45. None of these is close to always finding it.

## 2. Table

Question-tier recall is the share of queries, on RT-012, RT-147 and RT-183, whose top k contains the question-tier family (SF-APPA-005, SF07, SF-CHT-057). Lesson-tier recall is the share of queries, on the four tasks that have lesson-tier families and no question-tier family (RT-014, RT-066, RT-112, RT-179), whose top k contains at least one of those. Rows are the models' document-search queries (150). The paper's published rates count every family the run was shown, including follow-up calls.

| Retriever | k | Question tier | Lesson tier |
|---|---:|---:|---:|
| What Study 1 showed (paper, document search) | 4, plus follow-ups | 2/45 | (folded into 50/105 relevant) |
| What Study 1 showed (paper, graph search) | 4, plus follow-ups | 2/45 | (folded into 38/105 relevant) |
| TF-IDF, this test | 4 | 1/45 | 34/60 |
| TF-IDF | 8 | 1/45 | 45/60 |
| TF-IDF | 10 | 2/45 | 49/60 |
| TF-IDF | 20 | 16/45 | 57/60 |
| BM25 | 4 | 4/45 | 34/60 |
| BM25 | 20 | 19/45 | 58/60 |
| MiniLM, full text | 4 | 4/45 | 16/60 |
| MiniLM, full text | 20 | 26/45 | 32/60 |
| bge-small, full text | 4 | 9/45 | 25/60 |
| bge-small, full text | 8 | 13/45 | 29/60 |
| bge-small, full text | 20 | 29/45 | 32/60 |
| e5-small, full text | 4 | 1/45 | 18/60 |
| e5-small, full text | 20 | 20/45 | 45/60 |
| Hybrid, TF-IDF + bge-small | 4 | 3/45 | 18/60 |
| Hybrid, TF-IDF + bge-small | 20 | 27/45 | 49/60 |
| bge-small, question and hypothesis only | 4 | 9/45 | 18/60 |
| bge-small, question and hypothesis only | 20 | 15/45 | 35/60 |

Any relevant family, the paper's measure: document search showed one in 50 of 105 runs. Replaying keyword search at k=4 on the first call only gives 46 of 105. The same replay at k=20 gives 94 of 105. bge-small at k=4 gives 37 of 105, which is worse, because it finds fewer of the lesson-tier analogues. Graph search in the paper is 38 of 105. This test has 104 graph queries (see below) and the saved runs show a relevant family in 38 of those 104. Counting the excluded run as a miss, as the paper does, is 38 of 105.

## 3. Reproduction check

Document search: 150 of 150 queries reproduced the studies the model was shown, in the same order.

Graph search: 149 of 149 queries that made a search reproduced the same set. One run never called the search tool, `cross_model_v1|openrouter:openai/gpt-oss-20b|RT-183|C|s2`. It is counted as no search made, not as a miss. The test therefore ranks 299 queries, not 300.

An earlier execution, before this run, reproduced two graph queries with the same four studies in a different order. Unrounded scores of the swapped pair were equal: 0.2879102035925031 and 0.2879102035925031 for gpt-oss RT-147 seed 3 (`FAM:SF-APPA-050` and `FAM:SF-APPM-022`), and differed by 2.8e-17 for DeepSeek RT-183 seed 1 (`FAM:SF-PAP-033` and `FAM:SF-APPM-039`). This completed run's tie-break matched the saved order, so its log records 149 exact order matches. Recall at k does not depend on that order. Run ids: `cross_model_v1|openrouter:openai/gpt-oss-20b|RT-147|C|s3` and `reasoning_models_v1|openrouter:deepseek/deepseek-v4-pro|RT-183|C|s1`.

## 4. What this suggests, and what it does not

This is consistent with the closest-study misses in Study 1 being partly the retriever. bge-small at k=4 finds the question-tier family 9 times where keyword search finds it once. It is not consistent with "any modern retriever would have found them." 9 of 45 is still a miss on 36 queries, and two of the three embedding models barely move the number.

It is consistent with the page size mattering as much as the method. Keyword search at k=20 reaches 16 of 45 on the closest study and 94 of 105 on any relevant family. Study 1 never showed the model 20 families, so this does not say the decisions would have changed.

It suggests the Study 1b oracle gap is not something a better search at k=4 would have closed. The oracle hands over the relevant studies. The best retriever here still misses the closest study on most queries, and it returns fewer lesson-tier analogues than keyword search. That is consistent with Study 1b testing a different intervention from "use embeddings."

Model-written queries against the task's own question: one clean query per task, so the question-tier comparison is 3 queries, not 45. Keyword search hits none of the three at k=4. MiniLM and bge-small hit 2 of 3. On RT-147 the clean question ranks SF07 at 3 under both of those models, while the models' own queries put it in the top 4 in 0 of 15 bge-small runs (median rank 14) and 1 of 15 keyword runs (median rank 22). The models' queries do the opposite for the labeling audit SF-CHT-025, which is not the question-tier family: keyword search ranks it at a median of 2 on RT-012 and 4 on RT-147. So the wording the models chose is consistent with pulling up a data-quality audit and pushing down the prior study of the same question. With one clean query per task, that comparison is thin.

No retriever abstains. On RT-065, RT-101 and RT-146, which have no relevant family, every method returned exactly 4 families on all 30 queries.

## 5. Limitations and judgment calls

- Question tier here omits the TF-IDF similarity term in `relevant_families`, matching `analysis_fixes/recompute_retrieval_audit.py`, which checked that this version reproduces the saved audit columns. Adding that term back could add families.
- Lesson tier uses the corrected risk-code parsing. SF-CHT-025 is not in either tier for these tasks. It is reported on its own. Keyword search already ranks it in the top 4 on 11 of 15 RT-012 document queries and 8 of 15 RT-147 document queries, so the models' failure to use it is not a failure to retrieve it.
- SF-CHT-057, the question-tier family for RT-183, shares a median of 9.5 percent of the query's words (one document query shares none). SF07 shares about 23 percent. The closest-study misses are not only a no-shared-words problem. Embeddings also miss SF07 at k=4 on every document query in this test.
- Embedding vectors use each model's default maximum length, so long family records are cut at that limit.
- Graph queries are 44 of 45 on the question-tier tasks because of the excluded run. Paper denominators of 45 and 105 count that run as a miss.
- Clean-query results are one query per task.
- Rank of the first relevant family in the saved run is computable for every query in this execution, because this execution reproduced the saved order. The two tie cases above can flip between executions.

## 6. Suggested limitations paragraph

An offline check reranked the same pools the models searched, using the queries saved from the runs, and did not call a model. Keyword search put the closest earlier study in the top 4 on 1 of 45 document-search queries. A local embedding model (bge-small-en-v1.5) did so on 9 of 45, and the other two local models on 4 and 1 of 45. Raising the cutoff from 4 to 20 raised the keyword figure to 16 of 45 and the best embedding figure to 29 of 45. The same embedding model returned a lesson-tier analogue less often than keyword search (25 of 60 against 34 of 60 at k=4). No method declined to return results on the three tasks with nothing relevant. This is consistent with the closest-study misses being partly the retriever and partly the cutoff of four, and not with those misses being an artifact of keyword search alone.
