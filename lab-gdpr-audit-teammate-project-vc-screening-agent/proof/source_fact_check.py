"""Documentary fact check: which facts a source text states and which it leaves unspecified.
Usage: python -I source_fact_check.py <text_file> <case_filter|-> <term_file>
term_file lines: label|regex   (case-insensitive). Prints FOUND / NOT FOUND per label."""
import sys, re, pathlib
text = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")
flt = sys.argv[2]
if flt != "-":
    m = re.search(flt, text, re.S)
    text = m.group(0) if m else ""
print("chars_in_scope", len(text), "words_in_scope", len(text.split()))
for line in pathlib.Path(sys.argv[3]).read_text(encoding="utf-8").splitlines():
    if not line.strip() or line.startswith("#"): continue
    label, rx = line.split("|", 1)
    hits = re.findall(rx, text, re.I)
    print(("FOUND    " if hits else "NOT FOUND"), label, f"({len(hits)})")
