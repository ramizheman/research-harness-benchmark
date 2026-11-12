# Study 1b gold-family selection rule

Fixed before any gold list was computed. No subject model takes part in selection.

Inputs per task: the fixed retrieval audit (`bench/retrieval_audit.py`) on the task's memory_v3 snapshot.

- Q = question tier: same question cluster as the task family, knowable precedents and same-question families named in the answer key, and families with a record whose TF-IDF similarity to a task-family record is at least the calibrated merge threshold (0.231).
- L = lesson tier: untestable, artifact or uncertain families in the snapshot that share at least one of the task's expected risk codes.
- sim(f) = maximum TF-IDF cosine similarity between any record of family f and any record of the task family (the audit's vectoriser).

Selection, at most 4 families per task (the retrieve_history page size):

1. Order Q by: named in the answer key first, then sim descending, then family id.
2. Order L by: number of the task's expected risk codes shared, descending, then sim descending, then family id. A family in both tiers is treated as Q only.
3. Take the first 2 of Q and the first 2 of L. If a tier has fewer than 2, fill the remaining slots from the other tier in its order, up to 4 in total.
4. A task with no candidates gets no gold families; in O and OS its retrieve_history returns an empty list, as in condition A.

The proposed list is shown to the user for approval and frozen at approval. Any change after this commit is recorded as a deviation with its reason.
