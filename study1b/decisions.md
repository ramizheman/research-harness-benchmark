# Study 1b decisions log

## 2026-11-11 (Phase 0 and Phase 1 setup)
- Repo path confirmed: Research Harness Benchmark. Freeze method: git. pytest installed in supp_audit_venv.
- Gold sizing: at most 4 families per task by the rule in gold_rule.md (committed before the list was computed). O and OS follow-up tools: read_family limited to gold families, plus glossary and data_catalog; no free search.
- Pre-existing test failure left as is: tests/test_reasoning_models.py::test_cost_cap expects the Study 1 reasoning config's cap >= 15; the config says 12. Study 1 is fixed.

## 2026-11-12 (user approvals)
- Gold families approved as frozen in gold_families_frozen.json, with SF-CHT-025 a declared manual addition (replaces SF02 in RT-012). RT-065, RT-101 and RT-146 have no gold families and stay in O and OS (empty retrieval).
- Process approved: git repo, one annotation text per family across tasks, mechanical leakage check, no model calls before approval.
- Scope annotations approved after three edits (scope_annotations_frozen.json):
  1. SF-APPS-085: "true r 0.30 attenuates to 0.179" is literally in the record (observed_result), but the Applies-to sentence containing it was removed.
  2. Applies-to sentences: removed on SF-APPS-085 (stable-trait sentence) and SF07 (uniform / generic dead-ball sentence), the two flagged as bearing directly on their tasks. The other Applies-to sentences are kept and are annotator inference; OS is labelled exploratory.
  3. Disclosure: the annotator knew the answer key and Study 1 results; record-faithful sentence selection may still be steered and the mechanical check cannot detect it. OS results are descriptive, not confirmatory. This must be stated in the write-up.

## Notes for the preregistration (Phase 2), recorded 2026-11-12
- SF-CHT-025 cannot separate RT-012 from RT-147: its record and annotation fit both tasks equally. The expected outcome on that pair is a null for OS. Dated prediction to state: O helps RT-012; OS does not rescue RT-147.
- OS may therefore not test the scope-condition idea from paper 1: a record-faithful annotation cannot carry the effect-size information that separated RT-012 from RT-147. State this plainly.
