"""Checks for score.py that need no LLM. Usage: python3 test_score.py"""
from score import median, score, verify

CV = "- **Languages:** Go, Elixir\n- Owned Lambda services   in Java and Go.\nBachelor’s Degree"


def req(status, quote="", kind="must"):
    return {"requirement": "r", "kind": kind, "status": status, "cv_quote": quote, "gap": ""}


# A quote that is in the CV keeps "met". Markdown emphasis, case, spacing and apostrophe style do not matter.
assert verify([req("met", "languages: go, elixir")], CV)[0]["status"] == "met"
assert verify([req("met", "Owned Lambda services in Java and Go.")], CV)[0]["status"] == "met"
assert verify([req("met", "Bachelor's Degree")], CV)[0]["status"] == "met"
# An invented quote or an empty quote does not count as "met".
assert verify([req("met", "Expert in Rust")], CV)[0]["status"] == "partial"
assert verify([req("met", "")], CV)[0]["status"] == "partial"
# "partial" and "missing" do not change.
assert [r["status"] for r in verify([req("partial", "x"), req("missing")], CV)] == ["partial", "missing"]
# The median of three judgments drops one verdict that differs. Three different verdicts give the middle one.
assert median([[req("met")], [req("partial")], [req("met")]])[0]["status"] == "met"
assert median([[req("missing")], [req("partial")], [req("missing")]])[0]["status"] == "missing"
assert median([[req("met")], [req("missing")], [req("partial")]])[0]["status"] == "partial"
assert [r["status"] for r in median([[req("met"), req("missing")]] * 3)] == ["met", "missing"]
# The score counts must-have items only: met = 1, partial = 0.5, missing = 0.
assert score([req("met"), req("partial"), req("missing"), req("missing", kind="nice")])[0] == 50
assert score([req("met"), req("met")])[0] == 100
assert score([req("missing")])[0] == 0
# No must-have items: all items count.
assert score([req("met", kind="nice"), req("missing", kind="nice")])[0] == 50
print("✓ score.py checks passed!")
