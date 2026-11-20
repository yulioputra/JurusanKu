#!/usr/bin/env bash
# Generate data + halaman, jalankan tes, lalu salin hasil siap-publish ke dist/
set -euo pipefail
cd "$(dirname "$0")/.."
python3 tools/build_data.py
python3 tools/build_site.py
node --test tests/data.test.js
rm -rf dist && mkdir dist
cp -r assets css js jurusan jenjang dist/
cp ./*.html robots.txt sitemap.xml dist/
echo "Selesai: folder dist/ siap diunggah"
