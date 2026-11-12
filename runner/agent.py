"""Agent loop with a JSON action protocol, identical across conditions apart from the tool list."""
import json
import re
import time

from bench import common, scoring

SYSTEM = """You are a basketball analytics researcher deciding whether and how a research question should be studied.
You work only from the task statement and the tools listed below. Some tool lists include access to records of earlier
research by the same project; use them if listed. Do not assume facts you have not seen.

Tools:
{tools}

Protocol: every reply is exactly one JSON object and nothing else.
To call a tool: {{"action": "tool", "tool": "<name>", "args": {{...}}}}
To finish:      {{"action": "final", "output": <object following the schema below>}}
You may call at most {max_tools} tools; then you must finish.

Output schema:
{schema}

Risk codes (use only these): {codes}
Field guidance:
- testability.p_testable: probability that the question can be answered with the stated data at useful statistical power.
- prior_work.already_answered: whether earlier work you have seen already answered substantially the same question.
  Use "unknown" if you have seen no earlier work. List identifiers you relied on in prior_work.cited.
- predicted_outcome: probabilities (summing to 1) of what a competent test of the question as posed would conclude:
  supported, rejected (adequately powered null), untestable (cannot be tested with this data), artifact (apparent
  effect produced by a flaw), uncertain (inconclusive or inadequately tested).
- decision: proceed, proceed_with_changes (state the changes in design), or do_not_proceed.
- design: a pre-registration-quality plan even if the decision is do_not_proceed (then describe the minimum viable test).
"""

FINISH = "Tool budget exhausted. Reply now with the final action only."
REPAIR = "Your reply was not a valid action. Problems: {problems}. Reply with exactly one JSON object following the protocol."

# ---------------------------------------------------------------- protocol 2 (required retrieval)
RETRIEVAL_SCHEMA = {
    "research_question": "the research question in one sentence, in your own words",
    "retrieval_summary": {
        "prior_findings": [{"id": "identifier of the retrieved record", "status": "supported | rejected | untestable | artifact | uncertain",
                            "summary": "what it found"}],
        "failed_experiments": [{"id": "identifier", "status": "rejected | untestable | artifact | uncertain", "summary": "why it failed"}],
        "limitations": [{"id": "identifier", "text": "methodological or data limitation"}],
        "unresolved": [{"id": "identifier", "text": "question left open"}],
    },
    "evidence_use": "how the retrieved information (or its absence) changed your assessment",
}

SYSTEM_V2 = """You are a basketball analytics researcher deciding whether and how a research question should be studied.
You work only from the task statement and the tools listed below. Do not assume facts you have not seen.

Required procedure, in this order:
1. Identify the research question.
2. Perform the prescribed retrieval step: call retrieve_history with the research question and a search query. This
   step is mandatory and comes before any other tool. In some settings it returns no records; then say so.
3. Summarise the relevant prior findings, failed experiments, methodological limitations and unresolved questions
   that the retrieval returned. Cite only identifiers that appeared in tool results. Leave lists empty if nothing
   relevant was returned; never invent prior work.
4. Explain how that information (or its absence) affects your assessment.
5. Make your final research decision.

Tools:
{tools}

Protocol: every reply is exactly one JSON object and nothing else.
To call a tool: {{"action": "tool", "tool": "<name>", "args": {{...}}}}
To finish:      {{"action": "final", "output": <object following the schema below>}}
You may call at most {max_tools} tools; then you must finish. Check that every opening brace has a closing brace.

Output schema (all fields required):
{schema}

Risk codes (use only these): {codes}
Field guidance:
- testability.p_testable: probability that the question can be answered with the stated data at useful statistical power.
- prior_work.already_answered: whether retrieved earlier work already answered substantially the same question.
  Use "unknown" if no earlier work was retrieved. List identifiers you relied on in prior_work.cited.
- predicted_outcome: probabilities (summing to 1) of what a competent test of the question as posed would conclude:
  supported, rejected (adequately powered null), untestable (cannot be tested with this data), artifact (apparent
  effect produced by a flaw), uncertain (inconclusive or inadequately tested).
- decision: proceed, proceed_with_changes (state the changes in design), or do_not_proceed.
- design: a pre-registration-quality plan even if the decision is do_not_proceed (then describe the minimum viable test).
"""

RETRIEVE_FIRST = ("The prescribed retrieval step has not been performed. Call retrieve_history first: "
                  '{"action": "tool", "tool": "retrieve_history", "args": {"research_question": "...", "query": "..."}}')
FINAL_KEYS = ("testability", "decision", "predicted_outcome")


def system_prompt(toolbox, max_tools, protocol=1):
    if protocol >= 2:
        schema = {**RETRIEVAL_SCHEMA, **scoring.OUTPUT_SCHEMA}
        return SYSTEM_V2.format(tools=toolbox.describe(), max_tools=max_tools, schema=json.dumps(schema, indent=1),
                                codes=", ".join(common.RISK_CODES))
    return SYSTEM.format(tools=toolbox.describe(), max_tools=max_tools,
                         schema=json.dumps(scoring.OUTPUT_SCHEMA, indent=1), codes=", ".join(common.RISK_CODES))


def _loads_recovering(t):
    """Parse a JSON object, appending at most three missing closing braces. Returns (object, braces_added) or (None, None)."""
    dec = json.JSONDecoder()
    for extra in range(4):
        try:
            o, _ = dec.raw_decode(t + "}" * extra)
        except ValueError:
            continue
        return (o, extra) if isinstance(o, dict) else (None, None)
    return None, None


def parse_action_lenient(text):
    """Protocol 2 parser. Accepts, besides strict actions: a reply whose only defect is up to three missing closing
    braces at the end; a final output object sent without the action wrapper; a tool call without action='tool'.
    Returns (action, error, recovery_note). Anything else, including truncated strings or arrays, is rejected."""
    act, err = parse_action(text)
    if act is not None:
        return act, "", ""
    t = re.sub(r"^```(?:json)?|```$", "", text.strip(), flags=re.M).strip()
    start = t.find("{")
    if start < 0:
        return None, "no JSON object", ""
    o, added = _loads_recovering(t[start:])
    if o is None:
        return None, err, ""
    note = f"{added} closing brace(s) appended" if added else ""
    if o.get("action") == "final" and isinstance(o.get("output"), dict):
        return o, "", note or "accepted"
    if o.get("action") == "tool" and isinstance(o.get("tool"), str):
        return o, "", note or "accepted"
    if "action" not in o and isinstance(o.get("output"), dict) and all(k in o["output"] for k in FINAL_KEYS):
        return {"action": "final", "output": o["output"]}, "", (note + "; " if note else "") + "final without action field"
    if "action" not in o and all(k in o for k in FINAL_KEYS):
        return {"action": "final", "output": o}, "", (note + "; " if note else "") + "bare output object"
    if "action" not in o and isinstance(o.get("tool"), str):
        return {"action": "tool", "tool": o["tool"], "args": o.get("args", {})}, "", (note + "; " if note else "") + "tool call without action field"
    return None, "action must be 'tool' with a tool name or 'final' with an output object", ""


def parse_action(text):
    t = re.sub(r"^```(?:json)?|```$", "", text.strip(), flags=re.M).strip()
    start = t.find("{")
    if start < 0:
        return None, "no JSON object"
    depth, instr, esc = 0, False, False
    for i, ch in enumerate(t[start:], start):
        if instr:
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == '"':
                instr = False
            continue
        if ch == '"':
            instr = True
        elif ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                try:
                    a = json.loads(t[start:i + 1])
                except ValueError as e:
                    return None, f"invalid JSON: {e}"
                if a.get("action") == "tool" and isinstance(a.get("tool"), str):
                    return a, ""
                if a.get("action") == "final" and isinstance(a.get("output"), dict):
                    return a, ""
                return None, "action must be 'tool' with a tool name or 'final' with an output object"
    return None, "unterminated JSON object"


# ---------------------------------------------------------------- protocol 3 (retrieval before any assessment)
SYSTEM_V3 = """You are a basketball analytics researcher deciding whether and how a research question should be studied.
You work only from the task statement and the tools listed below. Do not assume facts you have not seen.

The work has two stages, in this order.
Stage 1, retrieval:
1. Read the research objective and the data description.
2. Identify the research concepts and methodological questions the task raises.
3. Retrieve historical evidence by calling retrieve_history.
In stage 1 do not assess the question, predict outcomes or decide. Your only stage-1 reply is the retrieve_history call.
Stage 2, assessment, after the retrieval result is returned:
4. Summarise the relevant historical findings and failed approaches.
5. State what the historical evidence does and does not establish.
6. Assess whether the research question is testable.
7. Identify methodological risks and potential confounders.
8. Make the final research decision.
9. Explain whether and how the historical evidence changed the decision.
The stage-2 output format is given together with the retrieval result.

Evidence rules: keep what a retrieved record states (historical_evidence and failed_approaches, each citing the
identifier of a returned record and its status exactly as recorded) separate from your own inference and from
uncertainty or missing information. Cite only identifiers returned by a tool, and never describe an earlier study that
no tool returned. In some settings retrieval returns no records; then state that no historical evidence was available.

Tools:
{tools}

Protocol: every reply is exactly one JSON object and nothing else.
To call a tool: {{"action": "tool", "tool": "<name>", "args": {{...}}}}
To finish (stage 2 only): {{"action": "final", "output": <object following the stage-2 schema>}}
You may call at most {max_tools} tools; then you must finish. Check that every opening brace has a closing brace.

Risk codes (use only these): {codes}
"""

STAGE1 = ('\n\nStage 1. Reply only with the retrieval call: {"action": "tool", "tool": "retrieve_history", "args": '
          '{"research_concepts": ["..."], "methodological_questions": ["..."], "query": "..."}}')

EVIDENCE_SCHEMA = {
    "research_concepts": ["concept"],
    "methodological_questions": ["question"],
    "historical_evidence": [{"id": "identifier of a record returned by a tool",
                             "status_as_recorded": "outcome status exactly as stated in the record (supported | rejected | inconclusive | untestable | artifact | not a hypothesis test | no result recorded)",
                             "finding": "what the record states, in its own terms"}],
    "failed_approaches": [{"id": "identifier of a returned record", "what_failed": "approach", "why": "failure mechanism or limitation as recorded"}],
    "evidence_establishes": ["what the retrieved evidence establishes for this question"],
    "evidence_does_not_establish": ["what it leaves open or cannot show"],
    "own_inferences": ["your inference, not stated in any record"],
    "uncertainties": ["uncertainty or missing information"],
    "historical_effect": {"changed_decision": "yes | no | no_historical_evidence", "explanation": "whether and how the historical evidence changed the decision"},
}

STAGE2 = """Stage 2. Using the retrieval result above (follow-up tools are allowed within the tool budget), complete steps 4 to 9
and reply with the final action. Output schema (all fields required):
{schema}
Field guidance:
- historical_evidence and failed_approaches: only records returned by a tool, with the status as recorded; empty lists
  if nothing relevant was returned.
- testability.p_testable: probability that the question can be answered with the stated data at useful statistical power.
- prior_work.already_answered: whether retrieved earlier work already answered substantially the same question.
  Use "unknown" if no earlier work was retrieved. List identifiers you relied on in prior_work.cited.
- predicted_outcome: probabilities (summing to 1) of what a competent test of the question as posed would conclude:
  supported, rejected (adequately powered null), untestable (cannot be tested with this data), artifact (apparent
  effect produced by a flaw), uncertain (inconclusive or inadequately tested).
- decision: proceed, proceed_with_changes (state the changes in design), or do_not_proceed.
- design: a pre-registration-quality plan even if the decision is do_not_proceed (then describe the minimum viable test)."""

RETRIEVE_FIRST_V3 = ("Stage 1 is not complete. Do not assess the question yet. Reply only with the retrieval call: "
                     '{"action": "tool", "tool": "retrieve_history", "args": {"research_concepts": ["..."], '
                     '"methodological_questions": ["..."], "query": "..."}}')
CORRECTION = ("Citation check failed: {problems}. Cite only identifiers returned by a tool and give each record's status "
              "exactly as recorded, or remove the item. Reply with the corrected complete final action.")
ASSESSMENT_KEYS = ("decision", "testability", "predicted_outcome", "risks", "design", "prior_work", "historical_effect")
STATUS_ALIASES = {"uncertain": "inconclusive", "not_a_test": "not a hypothesis test", "no_result": "no result recorded"}


def system_prompt_v3(toolbox, max_tools):
    return SYSTEM_V3.format(tools=toolbox.describe(), max_tools=max_tools, codes=", ".join(common.RISK_CODES))


def stage2_text():
    return STAGE2.format(schema=json.dumps({**EVIDENCE_SCHEMA, **scoring.OUTPUT_SCHEMA}, indent=1))


def has_assessment(o):
    if isinstance(o, dict):
        return any(k in ASSESSMENT_KEYS for k in o) or any(has_assessment(v) for v in o.values())
    if isinstance(o, list):
        return any(has_assessment(v) for v in o)
    return False


def cited_ids(final):
    ids = []
    for f in ("historical_evidence", "failed_approaches"):
        for x in (final.get(f) or []) if isinstance(final.get(f), list) else []:
            if isinstance(x, dict) and str(x.get("id", "")).strip():
                ids.append(str(x["id"]).strip())
    pw = final.get("prior_work") if isinstance(final.get("prior_work"), dict) else {}
    ids += [str(x).strip() for x in (pw.get("cited") or []) if isinstance(x, (str, int)) and str(x).strip()]
    return list(dict.fromkeys(ids))


PLACEHOLDER = re.compile(r"^(?:n/?a|none|null|-+|unknown|not applicable)$", re.I)


def citation_problems(final, toolbox):
    """Identifiers not returned by any tool, and stated statuses that differ from the returned record."""
    seen = set(getattr(toolbox, "returned", []))
    probs = []
    for i in cited_ids(final):
        if PLACEHOLDER.match(i):
            continue
        fid = i if i.startswith("FAM:") else "FAM:" + i
        if fid not in seen:
            probs.append(f"{i} was not returned by any tool")
    for x in final.get("historical_evidence") or [] if isinstance(final.get("historical_evidence"), list) else []:
        if not isinstance(x, dict):
            continue
        i = str(x.get("id", "")).strip()
        fid = i if i.startswith("FAM:") else "FAM:" + i
        if fid in seen:
            rec = next((o for p, o, _ in toolbox.facts.get(fid, []) if p == "auto_outcome_status"), None)
            said = str(x.get("status_as_recorded", "")).strip().lower()
            said = STATUS_ALIASES.get(said, said)
            if rec and said != rec:
                probs.append(f"{i} status is recorded as '{rec}', not '{x.get('status_as_recorded')}'")
    return probs


def run_v3(client, toolbox, statement, seed, budgets):
    max_tools = budgets.get("max_tool_calls", 12)
    max_turns = max_tools + budgets.get("max_repairs", 2) + 2 + 2 + 1
    system = system_prompt_v3(toolbox, max_tools)
    messages = [{"role": "user", "content": statement + STAGE1}]
    log, usage = [], {"input_tokens": 0, "output_tokens": 0, "cost_usd": 0.0, "cost_known": True}
    n_tools = n_repairs = n_gate = n_prelim = n_corr = 0
    stop, final, error, retrieved = "turn_limit", None, "", False
    precorrection, initial_problems = None, []
    t0 = time.time()
    for turn in range(max_turns):
        if time.time() - t0 > budgets.get("max_wall_seconds", 900):
            stop = "wall_clock"
            break
        if usage["input_tokens"] + usage["output_tokens"] > budgets.get("max_total_tokens", 250000):
            stop = "token_budget"
            break
        try:
            text, u = client.chat(system, messages, seed=seed)
        except Exception as e:  # noqa: BLE001
            stop, error = "api_error", repr(e)[:1000]
            break
        usage["input_tokens"] += u.get("input_tokens") or 0
        usage["output_tokens"] += u.get("output_tokens") or 0
        if u.get("cost_usd") is None:
            usage["cost_known"] = False
        else:
            usage["cost_usd"] += u["cost_usd"]
        asst_msg = {"role": "assistant", "content": text}
        if u.get("reasoning_details"):  # Claude extended-thinking: must be passed back in subsequent turns
            asst_msg["reasoning_details"] = u["reasoning_details"]
        messages.append(asst_msg)
        act, err, note = parse_action_lenient(text)
        if act is None and not retrieved:
            t = re.sub(r"^```(?:json)?|```$", "", text.strip(), flags=re.M).strip()
            o, _ = _loads_recovering(t[t.find("{"):]) if "{" in t else (None, None)
            if isinstance(o, dict) and "action" not in o and "query" in o and ("research_concepts" in o or "methodological_questions" in o):
                act, err, note = {"action": "tool", "tool": "retrieve_history", "args": o}, "", "retrieval arguments without action wrapper"
        entry = {"turn": turn, "stage": 2 if retrieved else 1, "reply": text, "usage": u, "parse_error": err, "parse_recovery": note}
        log.append(entry)
        if act is None:
            n_repairs += 1
            if n_repairs > budgets.get("max_repairs", 2):
                stop = "unparseable"
                break
            messages.append({"role": "user", "content": REPAIR.format(problems=err)})
            continue
        if not retrieved:
            is_retrieve = act["action"] == "tool" and act.get("tool") == "retrieve_history"
            prelim = act["action"] == "final" or has_assessment(act.get("args") if is_retrieve else act)
            if prelim:
                n_prelim += 1
                entry["preliminary_answer"] = True
            if prelim or not is_retrieve:
                n_gate += 1
                entry["gate"] = "retrieval required before any assessment"
                if n_gate > 2:
                    stop = "no_retrieval"
                    break
                messages.append({"role": "user", "content": RETRIEVE_FIRST_V3})
                continue
        if act["action"] == "final":
            probs = citation_problems(act["output"], toolbox)
            entry["citation_problems"] = probs
            if probs and n_corr < 1:
                n_corr += 1
                precorrection, initial_problems = act["output"], probs
                messages.append({"role": "user", "content": CORRECTION.format(problems="; ".join(probs))})
                continue
            final, stop = act["output"], "final"
            break
        if n_tools >= max_tools:
            messages.append({"role": "user", "content": FINISH})
            continue
        tt = time.time()
        res = toolbox.call(act["tool"], act.get("args", {}))
        n_tools += 1
        entry["tool"] = {"name": act["tool"], "args": act.get("args", {}), "result_chars": len(res),
                         "result_tokens_est": len(res) // 4, "latency_seconds": round(time.time() - tt, 3),
                         "returned_ids": list(toolbox.last_ids), "trace": toolbox.last_trace}
        first_retrieval = act["tool"] == "retrieve_history" and not retrieved
        retrieved = retrieved or act["tool"] == "retrieve_history"
        tail = ("\n\n" + stage2_text()) if first_retrieval else ""
        messages.append({"role": "user", "content": f"TOOL_RESULT {act['tool']}:\n{res}{tail}" + ("\n" + FINISH if n_tools >= max_tools else "")})
    tool_calls = [l["tool"] for l in log if "tool" in l]
    versions = sorted({l["usage"].get("model_version") for l in log if l["usage"].get("model_version")})
    return {"final": final, "stop_reason": stop, "api_error": error, "model_versions": versions, "turns": len(log),
            "tool_calls": tool_calls, "n_tool_calls": len(tool_calls),
            "memory_tool_calls": sum(1 for c in tool_calls if c["name"] not in ("glossary", "data_catalog") and c["returned_ids"]),
            "protocol": 3, "repair_turns": n_repairs, "gate_turns": n_gate, "preliminary_answers": n_prelim,
            "correction_turns": n_corr, "final_precorrection": precorrection, "initial_citation_problems": initial_problems,
            "parse_recoveries": [l["parse_recovery"] for l in log if l.get("parse_recovery") and l["parse_recovery"] != "accepted"],
            "usage": usage, "wall_seconds": round(time.time() - t0, 2), "system_prompt": system, "messages": messages, "log": log}


def run(client, toolbox, statement, seed, budgets, protocol=1):
    max_tools = budgets.get("max_tool_calls", 12)
    max_turns = max_tools + budgets.get("max_repairs", 2) + 2 + (2 if protocol >= 2 else 0)
    system = system_prompt(toolbox, max_tools, protocol)
    retrieved, n_gate = False, 0
    messages = [{"role": "user", "content": statement}]
    log, usage = [], {"input_tokens": 0, "output_tokens": 0, "cost_usd": 0.0, "cost_known": True}
    n_tools, n_repairs, stop, final, error = 0, 0, "turn_limit", None, ""
    t0 = time.time()
    for turn in range(max_turns):
        if time.time() - t0 > budgets.get("max_wall_seconds", 900):
            stop = "wall_clock"
            break
        if usage["input_tokens"] + usage["output_tokens"] > budgets.get("max_total_tokens", 250000):
            stop = "token_budget"
            break
        try:
            text, u = client.chat(system, messages, seed=seed)
        except Exception as e:  # noqa: BLE001
            stop, error = "api_error", repr(e)[:1000]
            break
        usage["input_tokens"] += u.get("input_tokens") or 0
        usage["output_tokens"] += u.get("output_tokens") or 0
        if u.get("cost_usd") is None:
            usage["cost_known"] = False
        else:
            usage["cost_usd"] += u["cost_usd"]
        asst_msg = {"role": "assistant", "content": text}
        if u.get("reasoning_details"):  # Claude extended-thinking: must be passed back in subsequent turns
            asst_msg["reasoning_details"] = u["reasoning_details"]
        messages.append(asst_msg)
        if protocol >= 2:
            act, err, note = parse_action_lenient(text)
        else:
            (act, err), note = parse_action(text), ""
        log.append({"turn": turn, "reply": text, "usage": u, "parse_error": err, "parse_recovery": note})
        if act is None:
            n_repairs += 1
            if n_repairs > budgets.get("max_repairs", 2):
                stop = "unparseable"
                break
            messages.append({"role": "user", "content": REPAIR.format(problems=err)})
            continue
        gate = protocol >= 2 and not retrieved and not (act["action"] == "tool" and act["tool"] == "retrieve_history")
        if gate and n_gate < 2:
            n_gate += 1
            log[-1]["gate"] = "retrieval required first"
            messages.append({"role": "user", "content": RETRIEVE_FIRST})
            continue
        if act["action"] == "final":
            final, stop = act["output"], "final" if not gate else "final_without_retrieval"
            break
        if n_tools >= max_tools:
            messages.append({"role": "user", "content": FINISH})
            continue
        tt = time.time()
        res = toolbox.call(act["tool"], act.get("args", {}))
        if protocol >= 2 and not isinstance(res, str):
            res = json.dumps(res)
        n_tools += 1
        retrieved = retrieved or act["tool"] == "retrieve_history"
        log[-1]["tool"] = {"name": act["tool"], "args": act.get("args", {}), "result_chars": len(res),
                           "latency_seconds": round(time.time() - tt, 3), "returned_ids": getattr(toolbox, "last_ids", [])}
        messages.append({"role": "user", "content": f"TOOL_RESULT {act['tool']}:\n{res}" + ("\n" + FINISH if n_tools >= max_tools else "")})
    tool_calls = [l["tool"] for l in log if "tool" in l]
    versions = sorted({l["usage"].get("model_version") for l in log if l["usage"].get("model_version")})
    return {"final": final, "stop_reason": stop, "api_error": error, "model_versions": versions, "turns": len(log), "tool_calls": tool_calls, "n_tool_calls": len(tool_calls),
            "memory_tool_calls": sum(1 for c in tool_calls if c["name"] not in ("glossary", "data_catalog")
                                     and not (c["name"] == "retrieve_history" and not c["returned_ids"])),
            "protocol": protocol, "repair_turns": n_repairs, "gate_turns": n_gate,
            "parse_recoveries": [l["parse_recovery"] for l in log if l.get("parse_recovery") and l["parse_recovery"] != "accepted"],
            "usage": usage, "wall_seconds": round(time.time() - t0, 2), "system_prompt": system, "messages": messages, "log": log}
