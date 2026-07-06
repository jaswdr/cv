#!/usr/bin/env python3
"""Local ATS checks for the CV PDF. Needs poppler (pdftotext, pdfinfo, pdfimages).

Usage: python3 ats_check.py Jonathan_Schweder_CV.pdf
Exit code 1 when any FAIL check fails. WARN checks only print.
"""
import os
import re
import subprocess
import sys

NAME = ("Jonathan", "Schweder")
SECTIONS = ["SUMMARY", "EXPERIENCE", "EDUCATION", "SKILLS"]  # expected reading order
MAX_BYTES = 200 * 1024
MAX_PAGES = 3
MIN_LAST_PAGE_FILL = 0.15


def run(*cmd):
    return subprocess.run(cmd, capture_output=True, text=True, check=True).stdout


def checks(pdf):
    info = dict(re.findall(r"^([^:]+):\s*(.*)$", run("pdfinfo", pdf), re.M))
    text = run("pdftotext", "-enc", "UTF-8", pdf, "-")
    pages = int(info["Pages"])
    w, h = map(float, re.match(r"([\d.]+) x ([\d.]+)", info["Page size"]).groups())
    images = run("pdfimages", "-list", pdf).splitlines()[2:]
    page_lines = [
        len(run("pdftotext", "-f", str(p), "-l", str(p), "-layout", pdf, "-").strip().splitlines())
        for p in (1, pages)
    ]
    upper = text.upper()
    positions = [upper.find(s) for s in SECTIONS]
    base = os.path.basename(pdf)

    # (level, description, passed, detail)
    yield "FAIL", "Text is extractable", len(text.split()) > 200, f"{len(text.split())} words"
    yield "FAIL", "Not encrypted", info.get("Encrypted", "no").startswith("no"), info.get("Encrypted")
    yield "FAIL", f"File size <= {MAX_BYTES // 1024} kB", os.path.getsize(pdf) <= MAX_BYTES, f"{os.path.getsize(pdf)} bytes"
    yield "FAIL", "Portrait orientation", h > w, info["Page size"]
    yield "FAIL", f"At most {MAX_PAGES} pages", pages <= MAX_PAGES, f"{pages} pages"
    yield "FAIL", "File name has first and last name", all(n.lower() in base.lower() for n in NAME), base
    yield "FAIL", "Full name in text", " ".join(NAME) in text, ""
    yield "FAIL", "Email present", bool(re.search(r"[\w.+-]+@[\w-]+\.[\w.-]+", text)), ""
    missing = [s for s, p in zip(SECTIONS, positions) if p < 0]
    yield "FAIL", "Standard section headings present", not missing, f"missing: {missing}" if missing else ""
    found = [p for p in positions if p >= 0]
    yield "FAIL", "Sections extract in reading order", found == sorted(found), dict(zip(SECTIONS, positions))
    yield "FAIL", "No photo or images", not images, f"{len(images)} images"
    bad = sorted({c for c in text if "ﬀ" <= c <= "ﬆ" or c == "�" or "" <= c <= ""})
    yield "FAIL", "No ligatures, replacement or private-use glyphs", not bad, [hex(ord(c)) for c in bad]
    # ponytail: line-based parsers see the layout text, where hyphenation splits keywords
    hyph = re.findall(r"\w+[­-]\n\s*\w+", run("pdftotext", "-layout", "-enc", "UTF-8", pdf, "-"))
    yield "FAIL", "No hyphenated (split) words", not hyph, [h.replace("­", "-").replace("\n", "") for h in hyph]
    yield "FAIL", "No date of birth or marital status", not re.search(r"date of birth|\bDOB\b|marital|married|single\b", text, re.I), ""
    yield "WARN", "Phone number in international format", bool(re.search(r"\+\d[\d\s().-]{7,}\d", text)), ""
    fill = page_lines[1] / page_lines[0] if pages > 1 else 1.0
    yield "WARN", f"Last page at least {MIN_LAST_PAGE_FILL:.0%} filled", fill >= MIN_LAST_PAGE_FILL, f"{fill:.0%} (line ratio vs page 1)"
    yield "WARN", "Has quantified results", len(re.findall(r"\d+%", text)) >= 3, f"{len(re.findall(r'\d+%', text))} percentages"


def main():
    pdf = sys.argv[1] if len(sys.argv) > 1 else "Jonathan_Schweder_CV.pdf"
    failed = False
    for level, desc, ok, detail in checks(pdf):
        status = "PASS" if ok else level
        failed |= status == "FAIL"
        print(f"[{status}] {desc}" + (f"  ({detail})" if detail and not ok else ""))
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
