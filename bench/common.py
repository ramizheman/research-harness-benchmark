"""Shared paths, loaders, keyword rules, date intervals and text similarity.

The topic, dataset, method, limitation and variable rules are copies of the lists in
scripts/01_build_inventory_and_memory.py; tests/test_common.py fails if the two drift apart.
"""
import csv
import json
import os
import re

HB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BB = os.path.dirname(HB)
LEDGER = os.path.join(BB, "Research Ledger")
APP = os.path.join(BB, "App", "Strategy")
MERGED = os.path.join(HB, "memory", "ledger_merged.jsonl")
FAMILY_REVIEW = os.path.join(HB, "audit", "study_family_review.csv")
INVENTORY = os.path.join(HB, "experiment_inventory.csv")

SLICE_RANK = {"PAP": 0, "TMP": 1, "APPA": 2, "APPM": 3, "APPS": 4, "CHT": 5}
ID_RE = re.compile(r"\b(?:APPA|APPM|APPS|PAP|TMP|CHT)-\d{3}\b")
PROJECT_START = "2026-03-01"
NR = "NOT RECORDED"

TOPIC_RULES = [
    ("NCAA tournament prediction", r"march madness|ncaa|kenpom|brier|\bseed|538|women'?s|men'?s 2025|bracket"),
    ("Play-type labeling and data quality", r"label|backfill|classifier|accuracy audit|distribution audit|insuff_evidence|patternquerylayer|pattern audit"),
    ("Playing time and luck response", r"luck|halftime minute|playing.time"),
    ("Strategy engine and AI agent evaluation", r"\bagent|llm|langgraph|debate|gemini|ablation|playsheet|engine|optimizer|blog replay|template|calibrat|shrinkage|alpha blend|feature stacking|residual feature|opener|conformance|routing|net-swing|training seasons|equilibrium|retrospective|backtest|app report"),
    ("Player absence and offensive reorganization", r"restor|absence|absorb|\bhub|spell|injur|scout|displacement|reorganiz"),
    ("Structural roles and influence", r"structural|load|influence|fragility|portability|coverage|connector|shaper|hasconn|concentration|wiring|role|identity|margbig|pci|gravity"),
    ("Defensive suppression and counter strategy (BEST/AVOID)", r"suppress|best vs avoid|best-avoid|avoid|counter|aftershock"),
    ("Lineup and matchup effects", r"lineup|substitution|five-|5-on-5|rapm|stint|matchup|synergy|kernel|on/off|onoff"),
    ("Possession sequences and transitions", r"sequence|sequential|transition matrix|8x8|8×8|chain|markov|brown|tatum|lag-1|lags|state persistence|epv"),
    ("In-game and series adaptation", r"within-game|within-series|series|adapt|\bh1\b|\bh2\b|crunch|clutch|run|pivot|trigger|playoff|halves"),
    ("Shot selection and shot quality", r"shot|xfg|pull_up|pull-up|three|3pa|rim"),
]
DATASET_RULES = [
    ("Play-type initiation records (Neo4j INITIATED edges / play-type possessions)", r"play.type|play-type|\bpt\b|pnr|\bcut\b|drive|post_up|spot_up|putback|initiat|neo4j|fingerprint|edges|transition"),
    ("NBA play-by-play possessions and reconstructed lineups", r"possession|play-by-play|pbp|stint|lineup|substitution|five"),
    ("Shot-level data with expected FG", r"\bshot|xfg|fga"),
    ("Box score and traditional stats", r"box|minutes|net rating|traditional|usage|ortg"),
    ("Player absence spells", r"absence|spell|injur"),
    ("Playoff series outcomes", r"series|playoff|upset"),
    ("NCAA tournament and ratings data", r"ncaa|kenpom|march madness|seed|538|elo|bracket"),
    ("LLM or agent outputs", r"\bagent|llm|gemini|langgraph|debate"),
]
METHOD_RULES = [
    ("difference-in-differences", r"\bdid\b|difference-in-difference"),
    ("placebo or permutation test", r"placebo|shuffle|permut"),
    ("split-half reliability", r"split-half|reliab|spearman-brown"),
    ("bootstrap interval", r"bootstrap"),
    ("matched control", r"matched|caliper|\bmatch"),
    ("regression", r"regression|\bols\b|r2\b|r²|logit|logistic|\blpm\b|lasso"),
    ("ridge or RAPM ratings", r"ridge|rapm"),
    ("holdout, backtest or replay", r"holdout|backtest|out-of-sample|\boos\b|loso|replay|retro|prospective|held-out"),
    ("ablation", r"ablation"),
    ("LLM agent run", r"\bagent|llm|langgraph|gemini|debate"),
    ("correlation", r"spearman|pearson|ρ|\brho\b|\br\s?=|correlat"),
    ("simulation", r"simulat|monte carlo|\bmc\b"),
    ("event study", r"event study|event-study"),
    ("case study", r"case stud"),
    ("calibration scoring", r"brier|calibrat"),
]
LIMIT_RULES = [
    ("small sample", r"\bn\s?=\s?\d{1,2}\b|small[- ]n|small sample|few |only \d+|underpowered"),
    ("low measurement reliability", r"reliab|split-half|spearman-brown|noisy"),
    ("insufficient exposure", r"exposure|median \d+ possessions|per pair|sparse"),
    ("low power / large MDE", r"\bmde\b|power"),
    ("selection or regression to the mean", r"regression to (the )?mean|\brtm\b|selection"),
    ("leakage", r"leak"),
    ("label or classification error", r"label|misclass|classifier"),
    ("drift", r"drift"),
    ("multiple testing", r"multiple test|holm|bonferroni|\bfdr\b|benjamini"),
    ("confounding", r"confound"),
    ("implementation bug", r"\bbug|error in|wrong sign|miscod"),
]
VARIABLE_RULES = [
    ("PPP (points per possession)", r"\bppp\b|points per possession"),
    ("play-type share / mix", r"share|mix"),
    ("structural influence / load (L)", r"\bload\b|influence|\bl_pre|\bl\(p\)|l_pred"),
    ("restoration R / reorganization", r"restor|reorgani"),
    ("expected FG / shot value", r"xfg|expected (shot|fg|points)"),
    ("three-point attempts or luck", r"three|3pa|3p\b|luck"),
    ("minutes / playing time", r"minutes|playing time"),
    ("net rating / ORtg", r"net rating|ortg|drtg"),
    ("win probability / series outcome", r"win%|win pct|series win|upset|outcome"),
    ("Brier score", r"brier"),
    ("turnovers", r"\btov|turnover"),
    ("free throws / fouls", r"foul|free throw"),
]

# Limitation categories that belong to the data (they constrain any design on that data) versus to a design choice.
DATA_LEVEL_LIMITS = {"insufficient exposure", "low measurement reliability", "label or classification error", "drift"}
DESIGN_LEVEL_LIMITS = {"selection or regression to the mean", "leakage", "multiple testing", "confounding", "implementation bug"}
# "small sample" and "low power / large MDE" are data-level when the record says the data cannot supply more units.
DATA_SCARCITY_RE = re.compile(r"only \d+ (?:\w+ )?(?:exist|available|in the data|team-seasons|seasons|series|spells)|"
                              r"cannot be (?:enlarged|increased)|all (?:available|existing)|max(?:imum)? available|"
                              r"(?:not|never) (?:in|recorded in) the data|no (?:field|column|data) for|data (?:do|does) not (?:record|contain)|"
                              r"coverage|exposure|sparse|too few", re.I)

# Methodological-risk taxonomy shared by the answer key and the scorer. Agents tag each risk they raise with one code.
RISK_RULES = [
    ("SAMPLE_SIZE_POWER", "Too few independent units or too little power for the effect size of interest",
     r"\bn\s?=\s?\d{1,2}\b|small[- ]n|small sample|underpowered|\bpower\b|\bmde\b|too few|wide ci|ci (?:includes|spans)"),
    ("EXPOSURE_SPARSITY", "Units (pairs, lineups, cells) observed for too few possessions",
     r"exposure|sparse|per pair|small cells?|cell sizes?|few possessions|median \d+ possessions"),
    ("MEASURE_RELIABILITY", "The measure is too noisy to rank or compare units",
     r"reliab|split-half|spearman-brown|noisy|noise floor|unstable"),
    ("RTM_SELECTION", "Selecting units on extreme early values, so later values regress to the mean",
     r"regression to (?:the )?mean|\brtm\b|selected on|selection on|conditioning on (?:a )?slump|extreme"),
    ("OUTCOME_DERIVED_LABEL", "Labels, triggers or features computed from the outcome being predicted",
     r"circular|outcome-derived|derived from the outcome|defined by the outcome|mechanical(?:ly)? (?:linked|related)|same possessions"),
    ("LEAKAGE_LOOKAHEAD", "Information from the evaluation period used in fitting, tuning or calibration",
     r"leak|look-?ahead|in-sample|same-season|tuned on|calibrated on|future (?:data|games)"),
    ("MECHANICAL_FLOOR", "An apparent effect produced by construction, such as deleting a player's own rows",
     r"mechanical|floor|by construction|identity|deletion"),
    ("BASE_RATE", "A gap that reflects league-wide base rates rather than game-specific information",
     r"base rate|base-rate|league[- ]wide ranking|fixed ranking|league ppp ranking|cut-heavy|composition"),
    ("CONFOUNDING", "Team quality, opponent, game state or garbage time not controlled",
     r"confound|team quality|opponent strength|garbage|blowout|game state|score margin"),
    ("LABEL_ERROR", "Play-type or event labels misclassified or backfilled",
     r"label|misclass|classifier|backfill|tagging"),
    ("PLACEBO_DEPENDENCE", "A placebo or permutation that shares noise with the test or ignores clustering",
     r"placebo|permut|shuffle|cluster"),
    ("MULTIPLE_TESTING", "Many tests or specifications without correction",
     r"multiple test|holm|bonferroni|\bfdr\b|benjamini|specification search|forking"),
    ("IMPLEMENTATION_BUG", "A code or data-processing error",
     r"\bbug|error in|wrong sign|miscod|off-by-one|join error"),
    ("DRIFT_NONSTATIONARITY", "Behaviour or data definitions change across seasons or within a season",
     r"drift|nonstationar|season-to-season|rule change|era"),
]
RISK_CODES = [c for c, _, _ in RISK_RULES]


def load_records(path=MERGED):
    return [json.loads(l) for l in open(path, encoding="utf-8") if l.strip()]


def load_families(records, path=FAMILY_REVIEW):
    """Return (family_of, members, kind, note); records outside a reviewed family become singleton families."""
    family_of, members, kind, note = {}, {}, {}, {}
    for fr in csv.DictReader(open(path, encoding="utf-8")):
        ms = [m.strip() for m in fr["members"].split(";") if m.strip()]
        members[fr["family_id"]] = ms
        kind[fr["family_id"]] = fr["kind"]
        note[fr["family_id"]] = (fr["evidence"] + (" | " + fr["note"] if fr["note"] else "")).strip()
        for m in ms:
            family_of[m] = fr["family_id"]
    for r in records:
        if r["id"] not in family_of:
            f = "SF-" + r["id"]
            family_of[r["id"]], members[f], kind[f], note[f] = f, [r["id"]], "single_record", ""
    return family_of, members, kind, note


def representative(member_ids):
    return min(member_ids, key=lambda i: (SLICE_RANK[i.split("-")[0]], i))


def load_inventory(path=INVENTORY):
    return {row["experiment_id"]: row for row in csv.DictReader(open(path, encoding="utf-8-sig"))}


def text(r, *fields):
    return " ".join(str(r.get(f) or "") for f in fields).lower()


def tags(rules, s):
    return [name for name, pat in rules if re.search(pat, s)]


def topic_of(r):
    s = text(r, "title", "hypothesis", "project")
    for name, pat in TOPIC_RULES:
        if re.search(pat, s):
            return name
    return "Other / unclassified"


def risk_codes(s):
    s = s.lower()
    return [code for code, _, pat in RISK_RULES if re.search(pat, s)]


def date_interval(r):
    """Return (lo, hi, reliable) for when the record's experiment happened.

    doc and transcript dates are taken as exact. A file modification time only bounds the experiment from above,
    because a file can be edited after the work it records; the lower bound is then the project start.
    """
    d, basis = (r.get("date") or "").strip(), (r.get("date_basis") or "").strip()
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", d):
        return PROJECT_START, "9999-12-31", False
    if basis in ("doc", "transcript"):
        return d, d, True
    return PROJECT_START, d, False


def strictly_before(a, b):
    """True when record a certainly happened before record b (date intervals do not overlap)."""
    return date_interval(a)[1] < date_interval(b)[0]


def order(a, b):
    """'before', 'after' or 'unknown' for record a relative to record b."""
    if strictly_before(a, b):
        return "before"
    if strictly_before(b, a):
        return "after"
    return "unknown"


SYNONYMS = [(r"pick[- ]and[- ]roll|\bp&r\b|\bpnr\b", " pnr "), (r"points per possession", " ppp "),
            (r"regression to (?:the )?mean", " rtm "), (r"play[- ]types?", " playtype "),
            (r"\bh1\b|first half", " firsthalf "), (r"\bh2\b|second half", " secondhalf ")]
STOP = set("""a an the of and or to in on for with by from at as is are was were be been being that this these those it its
than then there their they them which who whom whose what when where why how not no yes into over under after before
between during per vs versus via also more most less least each any all same other such only can could would should
will may might does do did has have had test tested testing hypothesis effect effects result results predicts predict
prediction whether higher lower than greater smaller larger significant significantly evidence""".split())


def norm_text(s):
    s = ID_RE.sub(" ", s).lower()
    for pat, rep in SYNONYMS:
        s = re.sub(pat, rep, s)
    s = re.sub(r"[-+−]?\d+(?:[.,]\d+)*%?", " ", s)
    s = re.sub(r"[^a-z_ ]+", " ", s)
    return " ".join(w for w in s.split() if w not in STOP and len(w) > 2)


def tfidf_matrix(texts, vocabulary_texts=None):
    """TF-IDF (word 1-2 grams) fitted on vocabulary_texts (default: texts). Returns (vectorizer, matrix)."""
    from sklearn.feature_extraction.text import TfidfVectorizer
    vec = TfidfVectorizer(preprocessor=norm_text, ngram_range=(1, 2), min_df=1, sublinear_tf=True, token_pattern=r"(?u)\b\w+\b")
    vec.fit(vocabulary_texts if vocabulary_texts is not None else texts)
    return vec, vec.transform(texts)


def write_csv(path, rows, fields=None):
    fields = fields or list(rows[0].keys())
    with open(path, "w", newline="", encoding="utf-8-sig") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def write_jsonl(path, rows):
    with open(path, "w", encoding="utf-8") as fh:
        for r in rows:
            fh.write(json.dumps(r, ensure_ascii=False, sort_keys=False) + "\n")


def rmtree_retry(path, attempts=8, delay=1.5):
    """Remove a generated directory, retrying while OneDrive or an indexer briefly holds a file open."""
    import shutil
    import time
    for i in range(attempts):
        if not os.path.exists(path):
            return
        try:
            shutil.rmtree(path)
            return
        except PermissionError:
            if i == attempts - 1:
                raise
            time.sleep(delay)


def safe_path(path):
    """Refuse to overwrite a file that existed before this benchmark revision (pre-revision files are listed in PROTECTED)."""
    rel = os.path.relpath(path, HB).replace("\\", "/")
    if rel in PROTECTED:
        raise PermissionError(f"refusing to overwrite pre-existing file {rel}")
    return path


PROTECTED = {
    "benchmark_design.md", "data_quality_and_classification_audit.md", "experiment_inventory.csv", "failure_analysis.md",
    "README.md", "research_history_map.md", "research_memory_schema.md", "memory/graph_edges.jsonl",
    "memory/graph_nodes.jsonl", "memory/ledger_merged.jsonl", "memory/merge_log.tsv", "audit/study_family_review.csv",
}
