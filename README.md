# JurusanKu

Website pemandu bagi pelajar yang mau lulus dan bingung lanjut ke mana: **SMA, SMK, atau MAN**, lalu jurusannya. Tes adaptif berhenti sendiri saat hasilnya jelas (10 sampai 18 pertanyaan), hasil memuat nama dan sekolah, bisa disimpan jadi PDF dan dibagikan.

## Fitur
Form data (nama, sekolah, alamat, email, HP opsional, tersimpan hanya di perangkat), tes adaptif, hasil dengan persen kecocokan, grafik radar, tipe kepribadian minat, Simpan PDF, bagikan dan WhatsApp, perbandingan SMA vs SMK vs MAN, 22 jurusan, setelah lulus, favorit, bandingkan jurusan, mode gelap, animasi.

## Menjalankan
Buka `index.html`, atau `./scripts/serve.sh` lalu buka http://localhost:8000.

## Mengubah konten
Edit `data/*.json` atau `templates/`, lalu jalankan `./scripts/build.sh` (atau `python3 tools/build_data.py` dan `python3 tools/build_site.py`).

## Deploy
Lihat `docs/DEPLOY.md`. Untuk domain sendiri: `SITE_URL=https://jurusanku.my.id/ python3 tools/build_site.py`.

## Struktur
`css/` (8 file), `js/` (core, ui, pages, generated), `data/` (JSON), `templates/` (HTML), `tools/` (Python), `scripts/` (Bash), `tests/` (Node), `types/` (TypeScript), `assets/` (SVG), `docs/`, `.github/workflows/` (YAML).

Konten jurusan masih ringkas dan perlu diverifikasi sebelum dipakai sebagai acuan resmi. Tes tidak merekomendasikan sekolah tertentu.
