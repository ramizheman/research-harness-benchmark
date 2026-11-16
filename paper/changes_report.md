# Changes report: paper1_readable.tex

Branch `paper1-readable`, from `paper1-with-1b` (7b3fc6f). Source file `paper/ssrn_research_memory_basketball.tex` is untouched; the rewrite is `paper/paper1_readable.tex`. No model or API call was run. No Study 2, prereg, run or frozen file was touched.

## Added
- Plain-language "Overview in plain language" box right after the abstract (question, the two studies, what was found; no p-values).
- New introduction: the story (months on in-game adaptation, biased question, dozens of failed rescue questions, archive of 319 families), the question ("can the corpses help you avoid other corpses?"), why memory might and might not help, and the pun ("The corpses become the corpus").
- "What the agent is asked to do": two plain sentences on the tasks, definition of flag, and RT-012 versus RT-147 as a worked example.
- Table `tab:tasks_plain`: one plain line per task, plus a note defining PNR, AVOID and calibrated labels (PPP is defined where it first appears, Section 4).
- One-sentence openers for Study 1 (design section) and Study 1b (stating that Study 1 could not separate "search failed" from "model misjudged", and that 1b removes the first).
- One plain-language answer sentence at the top of each results section (primary, secondary, transfer, extended thinking, Study 1b results).
- Limitations callback in "Archive and domain".
- New Appendix `app:scoring` (see below).

## Moved (relocated, text unchanged; main text keeps one sentence and a pointer)
| What | From | To |
|---|---|---|
| Scoring-rule mechanics (invalid-output rule, 32/31/1 counts) and bootstrap / sign-flip / Holm sentence | Section 5.4 | App. `app:scoring` |
| Sensitivity paragraph and Table `tab:sensitivity` | Primary results | App. `app:scoring` |
| Invalid-output paragraph and Table `tab:invalid` | Primary results | App. `app:scoring` |
| Repair-turn counts | Secondary results | App. `app:scoring` |
| Gemini-series (Pilot 1, Pilot 2, Experiment 1) paragraph | Primary results | App. `app:scoring` |
| AUC paragraph | Secondary results | App. `app:scoring` |
| Sabres/SprintAI, Spurs and "analytical capital" sentences | Introduction | Related work, "AI in sports operations" |

The hedging sentences about interval width ("about 0.6 wide ... cannot be ruled out") and about bootstrap intervals on ten units stay in the main text.

## Proof of number match (`paper/check_readable.py`)
```
distinct numeric tokens: original 306 readable 306
numbers only in original: []
numbers only in readable: []
original tables not verbatim in readable: []
new tables: ['tab:tasks_plain']
bibliography identical: True
equation environments: 0 0
labels removed: [] labels added: ['app:scoring', 'tab:tasks_plain']
undefined refs: []
words before appendix, excluding tables: original 8596 readable 9200
```
All 11 original tables are present verbatim. The bibliography is byte-identical. The paper has no equations. The new plain table has no digits (it uses `tabularx`, so it adds no width numbers either).

## Compile
Not done. No LaTeX compiler exists on this machine, and I did not install one. Errors, warnings and page counts are therefore unmeasured. Please compile once on a machine with LaTeX (new package used: `tabularx`, which is standard). Checked by script instead: no undefined `\ref`, no removed labels.

## Length target: not met by word count
Main text before the bibliography (tables excluded) grew from 8,596 to 9,200 words (+7%). Two tables left the main text and one small table was added. Whether the page count ends up higher or lower cannot be measured without a compiler. If you want it shorter, the next candidates to move are the Pilots table and Study 1b's limits paragraph.

## Sentences that might claim more than the original (flag for review)
None added knowingly. Please look at:
1. Intro: "a graveyard of ideas, with some survivors." The original says the archive is "a mixed body of work, not a collection of failures" (57 supported). I softened your "mostly failures" to match.
2. Intro and overview: the story (months, biased question, dozens of failed questions) comes from your brief; nothing in the repo verifies it.
3. Plain task table: paraphrases of each task and the "go ahead / stop" labels. Check the wording of RT-014 and RT-146.
4. Related work: the Spurs sentence is cited to Sports Business Journal 2025, because the original cited both sources together for the three examples. I could not tell which source covers which.
5. Overview: "it fixed about as many decisions as it broke" restates the 47 versus 46 tally.

## Judgment calls
- You asked for "three studies"; this paper has Study 1 and Study 1b only, so the overview says two and omits Study 2.
- The abstract is unchanged (no jokes, and it states claims I should not reword).
- I moved two paragraphs beyond your list (Gemini series and AUC) to offset added text.
- `RT-012` glossary: I defined calibrated labels only as far as the record does, not further.
- The file you called `paper1.tex` is `ssrn_research_memory_basketball.tex` in the repo.
- Not merged and not pushed.
