"""Claim registration with a hash chain, registry closure, the validation-data gate and claim validation.

Each entry stores the SHA-256 of the previous entry, so editing or deleting a registered claim breaks verify().
Closing the registry appends a final entry; validation data may be released only after closure and after D2.
For an external timestamp, the closing hash can additionally be published (for example in a commit or e-mail);
that step is optional and outside this module.
"""
import datetime as _dt
import hashlib
import json
import os
import subprocess
import sys


def _canon(obj):
    return json.dumps(obj, sort_keys=True, ensure_ascii=False, separators=(",", ":"))


def _hash(entry):
    body = {k: v for k, v in entry.items() if k != "hash"}
    return hashlib.sha256(_canon(body).encode("utf-8")).hexdigest()


def _now():
    return _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds")


def read(path):
    if not os.path.exists(path):
        return []
    return [json.loads(l) for l in open(path, encoding="utf-8") if l.strip()]


REQUIRED = ("estimand", "direction", "test", "pass_rule", "script")


def register(path, run_blind_id, claim, now=None):
    """Append one claim. Refuses if the registry is closed or the claim lacks required fields."""
    entries = read(path)
    if entries and entries[-1].get("kind") == "close":
        raise PermissionError("registry is closed; no further claims")
    missing = [k for k in REQUIRED if not claim.get(k)]
    if missing:
        raise ValueError("claim missing " + ", ".join(missing))
    script = claim["script"]
    if os.path.exists(script):
        claim = dict(claim, script_sha256=hashlib.sha256(open(script, "rb").read()).hexdigest())
    e = {"kind": "claim", "n": len(entries), "run": run_blind_id, "claim": claim, "registered_at": now or _now(),
         "prev": entries[-1]["hash"] if entries else "0" * 64}
    e["hash"] = _hash(e)
    with open(path, "a", encoding="utf-8") as fh:
        fh.write(_canon(e) + "\n")
    return e


def close(path, now=None):
    entries = read(path)
    if entries and entries[-1].get("kind") == "close":
        return entries[-1]
    e = {"kind": "close", "n": len(entries), "n_claims": sum(1 for x in entries if x["kind"] == "claim"),
         "registered_at": now or _now(), "prev": entries[-1]["hash"] if entries else "0" * 64}
    e["hash"] = _hash(e)
    with open(path, "a", encoding="utf-8") as fh:
        fh.write(_canon(e) + "\n")
    return e


def verify(path):
    """(ok, problems): checks each entry's hash, the chain links, script hashes where scripts still exist."""
    entries, problems = read(path), []
    prev = "0" * 64
    for i, e in enumerate(entries):
        if e.get("prev") != prev:
            problems.append(f"entry {i}: broken link")
        if _hash(e) != e.get("hash"):
            problems.append(f"entry {i}: content does not match its hash")
        c = e.get("claim") or {}
        if c.get("script_sha256") and os.path.exists(c["script"]):
            if hashlib.sha256(open(c["script"], "rb").read()).hexdigest() != c["script_sha256"]:
                problems.append(f"entry {i}: analysis script changed after registration")
        prev = e.get("hash")
    return not problems, problems


def release_allowed(path, d2, today=None):
    """Validation data may be fetched only when the registry verifies, is closed, and today is after D2."""
    ok, problems = verify(path)
    entries = read(path)
    closed = bool(entries) and entries[-1].get("kind") == "close"
    today = today or _dt.date.today().isoformat()
    reasons = ([] if ok else problems) + ([] if closed else ["registry not closed"]) + ([] if today > d2 else [f"today {today} is not after D2 {d2}"])
    return not reasons, reasons


def evaluate(result, pass_rule):
    """pass_rule: {'direction': 'positive'|'negative', 'min_abs_effect': float}; result: estimate and 95% interval."""
    est, lo, hi = float(result["estimate"]), float(result["ci_low"]), float(result["ci_high"])
    m = float(pass_rule.get("min_abs_effect", 0.0))
    if pass_rule.get("direction") == "negative":
        return hi < 0 and est <= -m
    return lo > 0 and est >= m


def run_script(script, data_dir, timeout=600):
    """Run a registered analysis script: `python script data_dir` must print one JSON object with estimate, ci_low, ci_high."""
    p = subprocess.run([sys.executable, script, data_dir], capture_output=True, text=True, timeout=timeout,
                       env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
    if p.returncode != 0:
        return None, p.stderr[-2000:]
    try:
        return json.loads(p.stdout.strip().splitlines()[-1]), ""
    except (ValueError, IndexError):
        return None, "script output is not JSON"


def validate(registry, dev_dir, val_dir, d2, today=None):
    """Re-run every registered claim on development data (reproducibility) and on validation data (survival)."""
    ok, reasons = release_allowed(registry, d2, today)
    if not ok:
        raise PermissionError("validation data not released: " + "; ".join(reasons))
    out = []
    for e in read(registry):
        if e["kind"] != "claim":
            continue
        c = e["claim"]
        dev, dev_err = run_script(c["script"], dev_dir)
        val, val_err = run_script(c["script"], val_dir)
        out.append({"run": e["run"], "n": e["n"], "estimand": c["estimand"],
                    "reproduces_on_development": dev is not None and evaluate(dev, c["pass_rule"]) == bool(c.get("dev_passed", True)),
                    "survives_validation": val is not None and evaluate(val, c["pass_rule"]),
                    "validation_result": val, "errors": (dev_err + " " + val_err).strip()})
    return out
