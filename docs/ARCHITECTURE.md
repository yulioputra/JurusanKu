# Arsitektur
`data/*.json` → `tools/build_data.py` (validasi, buat `js/generated/data.js`) → `tools/build_site.py` + `templates/*.html` (buat 27+ halaman statis: beranda, 16 detail jurusan, halaman jenjang, tips, tentang, 404, sitemap).
Halaman interaktif (tes, hasil, daftar jurusan, banding, favorit) memuat JavaScript per halaman di `js/pages/`; kode bersama ada di `js/core/` dan `js/ui/`.
Data pengguna (favorit, hasil, tema) disimpan di localStorage.
