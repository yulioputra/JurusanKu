#!/usr/bin/env python3
"""Generator situs statis: templates/ + data/*.json -> halaman HTML (index, jurusan/*, jenjang/*, dst)."""
import html, json, os
from pathlib import Path
from util import slug_of

ROOT = Path(__file__).resolve().parent.parent
load = lambda n: json.loads((ROOT / "data" / n).read_text(encoding="utf-8"))
tpl = lambda n: (ROOT / "templates" / n).read_text(encoding="utf-8")
e = html.escape
traits, majors, faq, tips, questions = load("traits.json"), load("majors.json"), load("faq.json"), load("tips.json"), load("questions.json")
TR = {t["id"]: t for t in traits["traits"]}
for m in majors: m["slug"] = slug_of(m)
SITE = os.environ.get("SITE_URL", "https://USERNAME.github.io/JurusanKu/").rstrip("/") + "/"
NAV = [("index.html", "Beranda"), ("tes.html", "Tes"), ("jurusan/index.html", "Jurusan"), ("banding.html", "Banding"), ("favorit.html", "Favorit"), ("tips.html", "Tips"), ("tentang.html", "Tentang")]
COMMON = ["generated/data", "core/utils", "core/state", "ui/feedback", "ui/components", "core/events", "core/site"]
CSS = ["tokens", "base", "splash", "layout", "pages", "components", "animations", "responsive"]
SPLASH = '<div id="splash"><div class="orb"></div><b>JurusanKu</b><div class="ld"><i></i></div><small>Menyiapkan petualanganmu…</small></div>'
pages = []

def fill(t, **kw):
    for k, v in kw.items(): t = t.replace("{{" + k + "}}", str(v))
    return t

def render(path, title, desc, body, extra=(), splash=""):
    root = "../" * path.count("/")
    nav = "".join(f'<a href="{root}{h}"{" class=\"on\"" if h == path else ""}>{t}</a>' for h, t in NAV)
    css = "".join(f'<link rel="stylesheet" href="{root}css/{n}.css">\n' for n in CSS)
    scripts = "".join(f'<script src="{root}js/{s}.js"></script>\n' for s in COMMON + list(extra))
    out = fill(tpl("base.html"), title=e(title), desc=e(desc), canon=SITE + path, root=root, css=css, nav=nav, splash=splash, body=body, scripts=scripts)
    p = ROOT / path; p.parent.mkdir(parents=True, exist_ok=True); p.write_text(out, encoding="utf-8")
    if path != "404.html": pages.append(path)

def mini(m, root):
    return f'<a class="card rv" href="{root}jurusan/{m["slug"]}.html" style="text-decoration:none;color:inherit"><span class="big">{m["ic"]}</span><br><span class="tag">{m["lv"]}</span><h3>{e(m["n"])}</h3><p class="mut">{e(m["d"])}</p></a>'

# Beranda
trait_cards = "".join(f'<div class="card rv"><span class="big">{t["emoji"]}</span><h3>{e(t["label"])}</h3><p class="mut">Kamu {e(t["phrase"])}.</p></div>' for t in traits["traits"])
home = fill(tpl("home.html"), nsmk=sum(m["lv"] == "SMK" for m in majors), nkul=sum(m["lv"] == "Kuliah" for m in majors), nq=len(questions), traits=trait_cards, popular="".join(mini(m, "") for m in majors[:3] + majors[8:11]))
render("index.html", "Temukan Jurusan SMK dan Kuliah yang Cocok", "Tes minat dan panduan memilih jurusan SMK dan kuliah lengkap dengan profil, prospek, dan perbandingan.", home, splash=SPLASH)

# Detail tiap jurusan + halaman per jenjang
for m in majors:
    fits = "".join(f'<li>Kamu {e(TR[k]["phrase"])}.</li>' for k in sorted(m["w"], key=lambda k: -m["w"][k]))
    bars = "".join(f'<div>{TR[k]["emoji"]} {e(TR[k]["label"])}<div class="bar"><i data-w="{m["w"][k] * 33}"></i></div></div>' for k in m["w"])
    sim = [x for x in majors if x["id"] != m["id"] and any(m["w"].get(k, 0) >= 2 and x["w"].get(k, 0) >= 2 for k in TR)][:3]
    body = fill(tpl("detail.html"), root="../", lv=m["lv"], lvp=m["lv"].lower(), id=m["id"], ic=m["ic"], n=e(m["n"]), d=e(m["d"]), why=e(m["why"]), mp=e(m["mp"]), jobs=e(m["jobs"]), fits=fits, bars=bars, similar="".join(mini(x, "../") for x in sim))
    render(f'jurusan/{m["slug"]}.html', m["n"], m["d"], body, extra=["pages/detail"])
for lv in ("SMK", "Kuliah"):
    items = "".join(mini(m, "../") for m in majors if m["lv"] == lv)
    render(f"jenjang/{lv.lower()}.html", f"Jurusan {lv}", f"Daftar jurusan {lv} beserta profil dan prospeknya.", f'<h1>Jurusan {lv}</h1><div class="grid">{items}</div><p><a class="btn" href="../tes.html">Cari yang cocok lewat tes</a></p>')

# Halaman interaktif (diisi JavaScript)
shell = lambda h, n="": f'<h1>{h}</h1><div id="app">{n}</div><noscript><div class="card">Halaman ini membutuhkan JavaScript.</div></noscript>'
render("tes.html", "Tes Minat Jurusan", "Jawab 14 pertanyaan untuk menemukan jurusan SMK atau kuliah yang cocok.", '<div id="app"></div><noscript><div class="card">Tes membutuhkan JavaScript.</div></noscript>', extra=["pages/tes"])
render("hasil.html", "Hasil Tes", "Hasil tes minat jurusanmu.", '<div id="app"></div>', extra=["pages/hasil"])
render("jurusan/index.html", "Semua Jurusan", "Telusuri semua jurusan SMK dan kuliah, cari, urutkan, dan bandingkan.", '<h1>Semua Jurusan</h1><div id="app"></div>', extra=["pages/jurusan"])
render("banding.html", "Bandingkan Jurusan", "Bandingkan sampai 3 jurusan berdampingan.", '<div id="app"></div>', extra=["pages/banding"])
render("favorit.html", "Jurusan Favorit", "Jurusan yang kamu simpan.", '<div id="app"></div>', extra=["pages/favorit"])

# Halaman statis
tip_cards = "".join(f'<div class="card rv"><span class="big">{t["emoji"]}</span><h3>{e(t["title"])}</h3><p class="mut">{e(t["text"])}</p></div>' for t in tips)
faq_cards = "".join(f'<div class="card rv"><details><summary>{e(f["q"])}</summary><div><p>{e(f["a"])}</p></div></details></div>' for f in faq)
render("tips.html", "Tips dan FAQ", "Tips memilih jurusan dan pertanyaan yang sering diajukan.", f'<h1>Tips dan FAQ</h1><div class="grid">{tip_cards}</div><h2>Pertanyaan umum</h2>{faq_cards}')
render("tentang.html", "Tentang JurusanKu", "Tentang proyek JurusanKu dan cara kerja tesnya.", '<h1>Tentang JurusanKu</h1><div class="card"><p>JurusanKu adalah proyek belajar untuk membantu pelajar mengenali minat dan memilih jurusan SMK atau kuliah.</p><p><b>Cara kerja:</b> setiap jawaban menambah skor pada 7 bidang minat. Tiap jurusan punya bobot bidang yang berbeda, lalu dicocokkan dengan profil minatmu.</p><p><b>Privasi:</b> favorit, tema, dan hasil terakhir hanya disimpan di browser perangkatmu.</p><p><b>Catatan:</b> konten jurusan masih ringkas dan perlu diverifikasi sebelum dipakai sebagai acuan resmi.</p></div>')
render("404.html", "Halaman tidak ditemukan", "Halaman tidak ditemukan.", '<div class="card"><h1>404</h1><p>Halaman yang kamu cari tidak ada.</p><a class="btn" href="index.html">Kembali ke beranda</a></div>')

(ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"<url><loc>{SITE}{p}</loc></url>\n" for p in pages) + "</urlset>\n", encoding="utf-8")
(ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE}sitemap.xml\n", encoding="utf-8")
print(f"OK: {len(pages) + 1} halaman HTML dibuat")
