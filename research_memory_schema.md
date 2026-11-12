# Research memory schema

This document defines the two forms of research memory used in the benchmark. Both are built from the same 384 merged records (`memory\ledger_merged.jsonl`) by `scripts\01_build_inventory_and_memory.py`:
- **Condition B, document memory:** `memory\documents\<id>.md`.
- **Condition C, structured memory:** `memory\graph_nodes.jsonl` and `memory\graph_edges.jsonl`.

The schema makes no assumption that the graph is better than searchable documents. Comparing the two is the purpose of the benchmark.

## 1. Design principles

1. **Same information, different organization.** Every fact in the graph comes from a field of a ledger record, a keyword rule or the reviewed study-family file. The same fact appears in that record's document. The graph adds structure (typed nodes, typed edges, shared grouping nodes), not facts. A script checks this in both directions (section 6).
2. **Provenance on everything.** Every node that comes from a record keeps `source_record`. Every edge keeps a `provenance` object naming the record, the rule that created the edge, and the record's source files or transcript ids.
3. **Derived versus recorded.** Values copied from records are kept apart from values produced by keyword rules or manual review. Rule-produced edges name their rule. Edges that need human confirmation carry `needs_review: true`.
4. **No invented content.** Fields that the records do not contain are absent from the graph and marked NOT RECORDED in the inventory. This covers primary outcome, what was learned, ruled-out directions and viable directions.

## 2. Entities (node types)

| node type | id pattern | count | source | key properties |
|---|---|---|---|---|
| Experiment | `EXP:<record id>` | 384 | one per merged record | title, project, date, date_basis, prespecified, n_runs, sources, knowable_in_advance, design, power_info, related, notes |
| Hypothesis | `HYP:<record id>` | 384 | record `hypothesis` | text, source_record |
| Result | `RES:<record id>` | 384 | record `verdict`, `primary_result`, `failure_evidence` | verdict, primary_result, failure_evidence, source_record |
| ResearchQuestion | `RQ:<topic>` | 12 | `TOPIC_RULES` | label, provenance. These are topic-level groupings, not individual questions (section 7). |
| Dataset | `DS:<label>` | 8 | `DATASET_RULES` | label |
| Variable | `VAR:<label>` | 12 | `VARIABLE_RULES` | label |
| Method | `METH:<label>` | 14 | `METHOD_RULES` | label |
| StatisticalLimitation | `LIM:<label>` | 11 | `LIMIT_RULES` over power_info, failure_evidence, notes | label |
| FailureMechanism | `FM:<type>` | 5 | fixed: A_unanswerable, B_powered_null, C_artifact, D_positive, E_unclear | label |
| Finding | `FIND:<record id>` | 89 | records with verdict supported | statement (the primary result), status ("supported in source; independent replication not recorded"), source_record |
| Paper | `PAPER:<title>` | 4 | record `project` | Structural Influence (published), Detecting Defensive Suppression (published), When a Hub Sits (manuscript), Halftime Minutes (manuscript) |
| DuplicateRecord | `ALIAS:<record id>` | 63 | records merged into another, and superseded versions | label, slice_file |
| FollowOnHypothesis | `FOLLOW:<record id>` | 10 | notes that mention a follow-up or a motivating result | text pointer to notes, status "candidate, needs curation" |

Total: 1,380 nodes.

## 3. Relations (edge types)

| relation | from to | count | created by | needs review |
|---|---|---|---|---|
| tested_by | Hypothesis to Experiment | 384 | record structure | no |
| addresses | Hypothesis to ResearchQuestion | 384 | TOPIC_RULES | no (rule-tagged) |
| produced | Experiment to Result | 384 | record structure | no |
| has_mechanism | Result to FailureMechanism | 384 | record `failure_type` | no |
| supported_by | Hypothesis to Experiment | 89 | verdict supported | no |
| contradicted_by | Hypothesis to Experiment | 151 | verdict null, failed_gate or reversed | no |
| invalidated_by | Hypothesis to Experiment | 34 | verdict artifact_found | no |
| derived_from | Finding to Experiment | 89 | verdict supported | no |
| uses_dataset | Experiment to Dataset | 540 | DATASET_RULES | no (rule-tagged) |
| uses_method | Experiment to Method | 515 | METHOD_RULES | no (rule-tagged) |
| limited_by | Experiment to StatisticalLimitation | 245 | LIMIT_RULES | no (rule-tagged) |
| measures | Experiment to Variable | 419 | VARIABLE_RULES | no (rule-tagged) |
| reported_in | Experiment to Paper | 144 | record `project` | no |
| duplicates | Experiment to DuplicateRecord, or Experiment to Experiment | 97 | 56 automatic merges, plus 41 reviewed study-family links (`audit\study_family_review.csv`) | no |
| extends | Experiment to Experiment | 358 | 334 from id references in the record's `related` field (direction not verified), plus 24 reviewed rerun or robustness links | 334 yes, 24 no |
| supersedes_version | Experiment to DuplicateRecord | 7 | record `supersedes` | no |
| rules_out | Experiment to UNRESOLVED | 1 | text pattern "ruled out" in notes | yes |
| motivates | Experiment to FollowOnHypothesis | 10 | text pattern "motivat", "follow-up", "next step", "led to" | yes |

Total: 4,235 edges, of which 345 need review.

**Missing relations.** `rules_out` and `motivates` are almost empty, because the records rarely say which later work a result ruled out or motivated. Filling them is curation work (section 7). Until then, a structured-memory agent cannot get those relations from the graph; it has to reason them out, just as a document-memory agent must.

## 4. Provenance object

Each edge carries:

```json
{"rule": "<rule name or 'record structure'>",
 "record": "<record id the edge was derived from>",
 "sources": ["<absolute path or transcript id>", "..."],
 "family": "<study family id, family edges only>",
 "evidence": "<shared numbers that identify the family, family edges only>"}
```

The `sources` paths are copied as cited. For the 22 records that cite the old `Documents\Basketball Strategy\` folder, the resolved path is in the inventory column `source_paths_resolved_after_folder_move`.

## 5. Condition B: document memory

There is one markdown file per merged record, `memory\documents\<id>.md`, with these sections:
- header lines: project, date and date basis, topic, prespecified, verdict, failure type, knowable in advance, runs, the dataset, method, limitation and variable tags, and paper;
- Hypothesis, Design, Result, Failure evidence, Power and reliability, Related, Notes, Sources;
- Finding status (supported records only);
- Related records, with ids resolved to merged records;
- Follow-on candidate (only where the notes mention one);
- Also recorded as (merged duplicates);
- Same study family (members, kind and shared-number evidence; family members only).

An agent in condition B gets these files and a full-text search tool, with no graph.

## 6. Equivalence between conditions B and C

| fact | in B | in C |
|---|---|---|
| hypothesis, design, result, failure evidence, power text, related text, notes, sources | document sections | Hypothesis, Result and Experiment node properties |
| verdict, failure type, prespecified, knowable in advance, date and date basis, runs | document header | node properties and has_mechanism edges |
| topic, paper | document header | addresses and reported_in edges |
| dataset, method, limitation, variable tags | document header | uses_dataset, uses_method, limited_by and measures edges |
| finding status, follow-on candidate flag | "Finding status" and "Follow-on candidate" sections | Finding and FollowOnHypothesis node properties |
| related records (ids resolved to merged records) | "Related records" section | extends edges |
| duplicates and study families | "Also recorded as" and "Same study family" sections | duplicates and extends edges with family provenance |

**Equivalence check (done).** `scripts\06_equivalence_check.py` runs the check in both directions:
- **Graph to documents:** for each record, every string on the record's own nodes, every label of a node one edge away, and every provenance value of the record's edges must appear in `<id>.md`.
- **Documents to graph:** every value in the document must appear among those graph strings.

The latest run (`audit\equivalence_check.md`) found 0 mismatches in either direction across all 384 records.

**What still differs.** The organization differs, and that difference is the treatment:
- **Condition C:** shared nodes connect records directly, for example every record limited by measurement reliability.
- **Condition B:** reaching the same set needs a text search for the tag.

## 7. Known limitations of the structured memory

1. **Research questions are topics.** The 12 ResearchQuestion nodes are topic labels. A real question layer would group hypotheses that ask the same thing in different studies, such as "do offenses abandon a suppressed play type?" asked in SF02, SF05 and PAP-042. That grouping needs human curation. A keyword pass found only 4 families of repeated questions (`audit\question_families.md`).
2. **Tags are keyword rules.** Datasets, methods, limitations and variables are tagged by keyword. They miss items (52 records have no dataset tag, 105 no method tag) and sometimes mis-tag, for example "placebo" in a record that only mentions a placebo planned for later.
3. **The direction of `extends` is unverified.** The 334 edges from `related` fields only record that one record names another. Some point backward ("builds on"), some forward ("was ruled out by"), and some sideways ("repeats").
4. **Findings are not consolidated.** Each supported record makes its own Finding node, so one result recorded in several families or records produces several Findings. Review collapses these for the 40 study families. No cross-family consolidation has been done.
5. **Hindsight fields.** `knowable_in_advance` is stored as an Experiment property. It was judged after outcomes were known (`data_quality_and_classification_audit.md`, section 4.4).
6. **No temporal edges.** Dates are node properties. There are no `preceded_by` edges, so a chronological cutoff has to be applied by filtering on date (`benchmark_design.md`, section 3.3).

## 8. Example queries

These show what condition C supports directly. Condition B has to answer them through text search.

| question | graph path |
|---|---|
| Which hypotheses about one topic were contradicted, and why? | `RQ:<topic>` back through addresses to the Hypothesis, then contradicted_by to the Experiment, then produced to the Result, then has_mechanism to the mechanism |
| Which methods most often produced artifacts? | Experiment uses_method to Method, joined with Result has_mechanism to `FM:C_artifact` (record-level rates in `audit\tables.md`) |
| Which studies were limited by measurement reliability? | `LIM:low measurement reliability` back through limited_by to the Experiment |
| Was this result recorded more than once? | duplicates and extends edges from the Experiment |
| Which findings come from a paper? | Finding derived_from the Experiment, then reported_in the Paper |
