# Deploy ke GitHub Pages
Opsi A (paling mudah): unggah seluruh isi folder ke repository, lalu Settings → Pages → Deploy from a branch → `main` / root. Semua halaman HTML sudah dibuat dan tersimpan di folder ini.

Opsi B (otomatis): Settings → Pages → Source: GitHub Actions. Setiap push menjalankan `.github/workflows/deploy.yml` (generate, tes, publish `dist/`).

Sitemap: isi alamat situs sebelum build, contoh `SITE_URL=https://namakamu.github.io/JurusanKu/ python3 tools/build_site.py`.
