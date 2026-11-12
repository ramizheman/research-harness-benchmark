"""Redaction of condition-revealing content and blinded identifiers for review."""
import hashlib
import hmac
import re

from . import common

PATTERNS = [
    (common.ID_RE, "[prior work]"),
    (re.compile(r"\bSF(?:-[A-Z]+-\d{3}|\d{2})\b"), "[prior work]"),
    (re.compile(r"\b(?:RQC|RT|PC|FG)-[\w-]+\b"), "[id]"),
    (re.compile(r"\b(?:EXP|RES|FAM|HYP|FIND|RQC|FG|DS|METH|LIM|VAR|PAPER|FOLLOW):[\w\-]+"), "[prior work]"),
    (re.compile(r"[A-Za-z]:\\[^\s\"']+|(?:/[\w.\-]+){2,}"), "[path]"),
    (re.compile(r"\b(?:search_documents|read_document|query_graph|graph_query|memory tool|document search)\b", re.I), "[tool]"),
    (re.compile(r"\b(?:knowledge graph|research graph|graph memory|the graph|graph node|nodes?|edges?|neighbou?rs?)\b", re.I), "[source]"),
    (re.compile(r"\b(?:research (?:history|memory|ledger)|the (?:history|memory|ledger|documents?|records?)|"
                r"prior records?|memory (?:shows|contains|records|says)|documented (?:history|records?)|"
                r"(?:document|record) (?:store|collection))\b", re.I), "[prior work]"),
]


def redact(text):
    n = 0
    for pat, rep in PATTERNS:
        text, k = pat.subn(rep, text)
        n += k
    return text, n


def redact_obj(obj):
    """Redact every string in a JSON-like object; returns (object, count)."""
    if isinstance(obj, str):
        return redact(obj)
    if isinstance(obj, list):
        out, n = [], 0
        for x in obj:
            y, k = redact_obj(x)
            out.append(y)
            n += k
        return out, n
    if isinstance(obj, dict):
        out, n = {}, 0
        for k_, v in obj.items():
            y, k = redact_obj(v)
            out[k_] = y
            n += k
        return out, n
    return obj, 0


def blind_id(secret, run_id):
    return "R" + hmac.new(secret.encode("utf-8"), run_id.encode("utf-8"), hashlib.sha256).hexdigest()[:12]
