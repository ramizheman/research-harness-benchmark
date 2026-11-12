# Revised memory audit (memory v2)

Memory v2 replaces the version-1 documents and graph for the benchmark. Both renderings are generated from one list of canonical facts. A fact is a subject, a predicate, an object and qualifiers. Every relationship carries the rule that produced it.

Sources: `audit\memory_v2_audit.json`, `audit\extends_direction_audit.csv`, `research_question_clusters.csv` and `automated_adjudication.csv`. The original memory files are unchanged.

## 1. Equivalence of conditions B and C (re-run)

| check | full history | pilot snapshots |
|---|---|---|
| canonical facts | 20,111 | 5,527 to 18,169 per task |
| facts parsed back from documents | 20,111 | equal to canonical in all 10 |
| facts parsed back from graph | 20,111 | equal to canonical in all 10 |
| missing or extra facts, title mismatches | 0 | 0 |
| excluded records present | not applicable | 0 in all 10 |

The check parses the rendered documents and the exported graph back into facts and compares both with the canonical list. Neither rendering is compared only with itself. A unit test repeats the round trip with braces, semicolons and other characters that previously broke parsing.

**Information is equivalent; access is not.** Condition B searches documents with TF-IDF ranking. Condition C has a structured query with the same TF-IDF ranking for free text, plus type filters and neighbor traversal. The retrieval rankers were made identical so that differences between B and C come from structure, not from a weaker search function.

## 2. Question clusters

Clusters group families that ask substantially the same question, across topics, using average-linkage clustering of TF-IDF vectors over title, hypothesis and design. Identifiers, numbers and stopwords are removed, and synonyms are normalized.

| relation of a family to its nearest neighbour in the cluster | families |
|---|---|
| repeat of an earlier family (similarity at or above 0.344, earlier family certainly first) | 12 |
| repeated by a later family | 7 |
| repeat, order unknown (dates overlap) | 81 |
| related question (same cluster, below the repeat threshold) | 89 |
| distinct question (alone in its cluster) | 130 |

There are 206 clusters, 76 of them with more than one family.

External check: of 305 explicit cross-family references in the records' `related` fields, 24.6% fall in the same cluster. References often point to methodological predecessors rather than to the same question, so low agreement is expected. It also means the clusters should not be read as a map of every intellectual dependency.

## 3. Extends relationships: corrected and flagged

The version-1 memory drew `extends` edges from related-field references without checking direction.

| version-1 `extends` edges (358) | count |
|---|---|
| direction correct by dates | 40 |
| direction reversed | 44 |
| direction ambiguous (dates overlap or are upper bounds only) | 274 |

In version 2, a relationship between records has the later record extend the earlier one:

- 39 verified by dates;
- 42 corrected, because the citing record was the earlier one;
- 234 downgraded to `related_to` because the order cannot be established.

An artifact finding that follows a supported record becomes `invalidates`. Of the 4,568 edges, 286 carry `needs_review`, which flags a relationship that rests on overlapping dates or lexical similarity alone. No edge lacks a rule.

## 4. Repeated findings consolidated

32 consolidated findings group 71 families that sit in the same question cluster and share a stratum: 11 supported, 6 rejected, 6 untestable, 6 artifact and 3 uncertain. Each consolidated finding lists its member families (`consolidates`) and the question it is about. Consolidation only links findings; it never replaces a family's own finding.

## 5. Results by type

| finding status | families |
|---|---|
| supported | 57 |
| rejected (adequately powered null) | 57 |
| untestable | 49 |
| artifact | 44 |
| uncertain (inconclusive or inadequately tested) | 52 |

Rejected and artifact findings carry `rules_out` edges to the hypothesis, scoped to that design and data. A `rules_out` is not a claim that the idea is false under every design.

## 6. Data-level versus design-level limitations

| level | family limitation links |
|---|---|
| data (exposure, measurement reliability, label error, drift, stated data scarcity) | 64 |
| design (selection or regression to the mean, leakage, multiple testing, confounding, implementation bug) | 42 |
| unclear (sample size or power without a statement that the data cannot supply more) | 109 |

Small samples are not assigned to the data level automatically. A small sample is a data limitation only when the record says the data cannot supply more, for example "only 31 series exist". Otherwise it may simply be a design choice.

## 7. Provenance

Every edge has a `rule` qualifier naming the source of the relationship:

- the family review file;
- a keyword rule;
- question clustering with its threshold;
- automated adjudication;
- date comparison.

Edges also carry the family or record they came from. Adjudication attributes include `adjudication_type: automated (rule-based); not independent human adjudication`.

## 8. Snapshots

A snapshot is a pure function of the permitted records. The same records give the same fact hash, and the manifest stores the record list, the fact hash and the equivalence result. The runner refuses to run a task when the snapshot's records differ from the frozen task's permitted list, when the snapshot is not equivalent, or when an excluded record is present.

Family verdicts inside a snapshot are re-adjudicated from the permitted members only. A family whose later member is after the cutoff therefore shows the verdict that was known at the time.

## 9. Known weaknesses

- Lexical clustering misses paraphrased repeats and can join unrelated questions that share technical words. The repeat threshold sits at the median of same-study pairs, so about half of known same-study pairs fall below it.
- 205 of 384 records have only an upper-bound date. Many order relations are therefore unknown, and permitted memory for tasks dated by file modification time is conservative: it is smaller than the memory actually available at the time.
- Memory contains automated adjudication fields (stratum, confidence) for earlier families. An agent in B or C sees these labels and may over-trust them; the labels are provisional.
