# APPM-036: Paper numbers audit (Same Menu, Different Wiring)

- Project: Structural Influence (Paper 1)
- Date: 2026-07-14 (doc)
- Topic: Structural roles and influence
- Pre-specified: yes
- Verdict: tool_eval_pass
- Failure type: D_positive
- Knowable in advance: unclear
- Runs: 1
- Dataset tags: 
- Method tags: 
- Limitation tags: 
- Variable tags: 
- Paper: Structural Influence (published)

## Hypothesis
Every numeric result in paper.tex reproduces from cached artifacts.

## Design
Recompute 160 claims from paper2_output artifacts with tolerances.

## Result
160/160 PASS, 0 FAIL.

## Failure evidence
160/160 PASS.

## Power and reliability


## Related


## Notes
Caveats: organizer +2.24 not persisted in CSV; Fig1 cosines not re-verified offline; 186 vs 187 positive delta discrepancy.

## Sources
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\PAPER_NUMBERS_SHEET.md
- C:\Users\lisas\OneDrive\Documents\Basketball\App\Strategy\_paper_numbers_audit.py
