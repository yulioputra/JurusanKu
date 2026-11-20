#!/usr/bin/env python3
"""Validasi data/*.json lalu hasilkan js/generated/data.js (dipakai browser tanpa fetch)."""
import json, sys
from pathlib import Path
from util import slug_of

ROOT = Path(__file__).resolve().parent.parent
load = lambda n: json.loads((ROOT / "data" / n).read_text(encoding="utf-8"))

def fail(msg):
    print("ERROR:", msg); sys.exit(1)

traits, questions, majors = load("traits.json"), load("questions.json"), load("majors.json")
faq, tips = load("faq.json"), load("tips.json")
ids = [t["id"] for t in traits["traits"]]
for q in questions:
    if q["trait"] not in ids: fail(f"trait tidak dikenal di pertanyaan: {q['text']}")
for t in ids:
    if not any(q["trait"] == t for q in questions): fail(f"bidang {t} belum punya pertanyaan")
seen = set()
for m in majors:
    if m["id"] in seen: fail(f"id jurusan ganda: {m['id']}")
    seen.add(m["id"])
    if m["lv"] not in ("SMK", "Kuliah"): fail(f"jenjang salah: {m['n']}")
    for k in ("n", "ic", "d", "why", "jobs", "mp"):
        if not m.get(k): fail(f"{m['n']} belum punya field {k}")
    for k, v in m["w"].items():
        if k not in ids or v not in (1, 2, 3): fail(f"bobot salah di {m['n']}: {k}={v}")

for m in majors: m["slug"] = slug_of(m)
js = lambda v: json.dumps(v, ensure_ascii=False)
out = "// FILE HASIL GENERATE. Jangan diedit; ubah data/*.json lalu jalankan tools/build_data.py\n"
out += "const TR=" + js({t["id"]: [t["emoji"], t["label"], t["phrase"]] for t in traits["traits"]}) + ";\n"
out += "const Q=" + js([[q["text"], q["trait"]] for q in questions]) + ";\n"
out += "const O=" + js([[a["label"], a["value"]] for a in traits["answers"]]) + ";\n"
out += "const J=" + js(majors) + ";\n"
out += "const FAQ=" + js([[f["q"], f["a"]] for f in faq]) + ";\n"
out += "const TIPS=" + js([[t["emoji"], t["title"], t["text"]] for t in tips]) + ";\n"
(ROOT / "js" / "generated" / "data.js").write_text(out, encoding="utf-8")
print(f"OK: {len(majors)} jurusan, {len(questions)} pertanyaan, {len(ids)} bidang minat")
