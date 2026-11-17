# Relevant families in memory

Supports Appendix D of Paper 1. The same values are in `table16_retrieval.csv`.

Q and L are the numbers of question-tier and lesson-tier relevant families in the task's snapshot. Fam is the mean number of families returned per run, including follow-up calls. Ment, Ret, and Used are shares of the 15 runs per cell (five models, three seeds) in which at least one relevant family of either tier was mentioned, returned, or used. The question-tier families for RT-147 and RT-183 are their prior same-question studies, SF07 and SF-CHT-057.

B is document search. C is graph search.

| Task | Stratum | Q | L | B Fam | B Ment | B Ret | B Used | C Fam | C Ment | C Ret | C Used |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| RT-012 | artifact | 1 | 5 | 4.3 | 0.27 | 0.27 | 0.27 | 4.0 | 0.27 | 0.27 | 0.27 |
| RT-014 | artifact | 0 | 8 | 4.3 | 0.20 | 0.20 | 0.20 | 4.0 | 0.13 | 0.07 | 0.07 |
| RT-065 | rejected | 0 | 0 | 4.8 | 0.00 | 0.00 | 0.00 | 4.2 | 0.00 | 0.00 | 0.00 |
| RT-066 | rejected | 0 | 49 | 5.6 | 0.80 | 0.27 | 0.27 | 4.0 | 0.80 | 0.53 | 0.53 |
| RT-101 | supported | 0 | 0 | 5.3 | 0.00 | 0.00 | 0.00 | 4.0 | 0.00 | 0.00 | 0.00 |
| RT-112 | supported | 0 | 9 | 4.0 | 1.00 | 1.00 | 0.87 | 4.0 | 0.13 | 0.13 | 0.13 |
| RT-146 | uncertain | 0 | 0 | 4.5 | 0.00 | 0.00 | 0.00 | 4.0 | 0.00 | 0.00 | 0.00 |
| RT-147 | uncertain | 1 | 0 | 4.1 | 0.27 | 0.07 | 0.07 | 4.0 | 0.13 | 0.13 | 0.13 |
| RT-179 | untestable | 0 | 7 | 4.5 | 1.00 | 1.00 | 0.93 | 4.0 | 1.00 | 1.00 | 0.87 |
| RT-183 | untestable | 1 | 43 | 4.8 | 0.80 | 0.53 | 0.53 | 3.7 | 0.67 | 0.40 | 0.33 |
