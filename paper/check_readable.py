"""Compare paper1-with-1b version with paper1_readable.tex. Run from the repo root."""
import re, subprocess, collections, sys

o = subprocess.run(["git", "show", "paper1-with-1b:paper/ssrn_research_memory_basketball.tex"],
                   capture_output=True).stdout.decode("utf-8")
n = open("paper/ssrn_research_memory_basketball.tex", encoding="utf-8").read()
num = re.compile(r"\d+(?:[.,]\d+)*")


def nums(t):
    t = re.sub(r"\\(label|ref)\{[^}]*\}", "", t)
    return collections.Counter(num.findall(t))


so, sn = nums(o), nums(n)
only_o, only_n = sorted(set(so) - set(sn)), sorted(set(sn) - set(so))
print("distinct numeric tokens: original", len(so), "readable", len(sn))
print("numbers only in original:", only_o)
print("numbers only in readable:", only_n)
tabs = lambda t: re.findall(r"\\begin\{table\}.*?\\end\{table\}", t, re.S)
lab = lambda e: re.search(r"\\label\{([^}]*)\}", e).group(1)
bad = [lab(e) for e in tabs(o) if e not in n]
print("original tables not verbatim in readable:", bad)
print("new tables:", [lab(e) for e in tabs(n) if e not in o])
b = lambda t: t[t.index("\\begin{thebibliography}"):t.index("\\end{thebibliography}")]
print("bibliography identical:", b(o) == b(n))
print("equation environments:", len(re.findall(r"\\begin\{(equation|align)", o)),
      len(re.findall(r"\\begin\{(equation|align)", n)))
lo = set(re.findall(r"\\label\{([^}]*)\}", o)); ln = set(re.findall(r"\\label\{([^}]*)\}", n))
print("labels removed:", sorted(lo - ln), "labels added:", sorted(ln - lo))
refs = set(re.findall(r"\\ref\{([^}]*)\}", n))
print("undefined refs:", sorted(refs - ln))


def words(t, upto):
    t = t.split(upto)[0]
    t = re.sub(r"\\begin\{table\}.*?\\end\{table\}", "", t, flags=re.S)
    return len(re.sub(r"\\[a-zA-Z]+|[{}$]", " ", t).split())


print("words before appendix, excluding tables: original", words(o, "\\begin{thebibliography}"),
      "readable", words(n, "\\begin{thebibliography}"))
sys.exit(1 if (only_o or bad) else 0)
