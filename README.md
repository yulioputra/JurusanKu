# JurusanKu

Website panduan memilih jurusan SMK dan kuliah: tes minat, grafik radar, rekomendasi beserta alasannya, daftar dan perbandingan jurusan, favorit, mode gelap.

## Menjalankan
Buka `index.html` (semua halaman sudah dibuat), atau `./scripts/serve.sh` lalu buka http://localhost:8000.

## Mengubah konten
Edit `data/*.json` atau `templates/`, lalu `./scripts/build.sh` (atau jalankan `tools/build_data.py` dan `tools/build_site.py`). Lihat `docs/CONTENT_GUIDE.md`.

## Build dan tes
`./scripts/build.sh` (generate data, jalankan tes Node, hasil di `dist/`).

## Struktur
`css/` (8 file), `js/` (core, ui, views, generated), `data/` (JSON), `tools/` (Python), `scripts/` (Bash), `tests/` (Node), `types/` (TypeScript), `assets/` (SVG), `docs/`, `.github/workflows/` (YAML).

Konten jurusan masih ringkas dan perlu diverifikasi sebelum dipakai sebagai acuan resmi.
