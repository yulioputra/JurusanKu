# JurusanKu

Website pemandu khusus **lulusan SMP** yang bingung memilih sekolah (**SMA, SMK, atau MAN**) dan jurusannya. Tes adaptif berhenti sendiri saat hasilnya jelas (10 sampai 18 pertanyaan), hasil memuat nama dan sekolah, bisa disimpan jadi PDF dan dibagikan.

## Fitur
Form data (tersimpan hanya di perangkat), tes adaptif (10–18 dari 50 pertanyaan), hasil dengan persen kecocokan dan penanganan hasil seri, hasil dalam 4 tab, grafik radar, tipe minat, PDF, WhatsApp, kartu gambar, versi orang tua, perbandingan SMA vs SMK vs MAN, **43 jurusan** (SMA, SMK, MAN; jurusan SMK dibatasi yang umum di Jawa) dengan lama belajar dan kelanjutan, filter jurusan menurut jenjang dan bidang minat, halaman **Jalur Masuk dan Bantuan Biaya** (SPMB, PIP), **Persiapan Kelas 9**, favorit, bandingkan jurusan, mode gelap, offline (PWA).

## Menu
Enam bagian, sama di HP dan desktop: **Beranda** (pilih yang bikin bingung), **Tes** (2 tes), **Jurusan** (daftar dan filter), **Info** (jalur masuk, bandingkan, glosarium, tips, orang tua, pengaturan), **Riwayat** (hasil tes dan favorit), **Profil** (nama, bio, asal sekolah, avatar).

## Fitur tambahan v18
Tes Jurusan (14 pertanyaan untuk SMK, SMA, atau MAN), Riwayat hasil, Glosarium 28 istilah, Pengaturan (tema, ukuran teks, cadangan dan pemulihan data, ukuran penyimpanan, hapus data), jejak halaman (breadcrumb) di semua halaman dalam.

## Menjalankan
Buka `index.html`, atau `./scripts/serve.sh` lalu buka http://localhost:8000.

## Mengubah konten
Edit `data/*.json` atau `templates/`, lalu jalankan `./scripts/build.sh` (atau `python3 tools/build_data.py` dan `python3 tools/build_site.py`).

## Deploy
Lihat `docs/DEPLOY.md`. Untuk domain sendiri: `SITE_URL=https://jurusanku.my.id/ python3 tools/build_site.py` (sudah jadi nilai bawaan).

## Struktur
`css/` (termasuk `fx.css`), `js/` (core, ui, pages, generated), `data/` (JSON), `templates/` (HTML), `tools/` (Python), `scripts/` (Bash), `tests/` (Node), `types/` (TypeScript), `assets/` (SVG), `docs/`, `.github/workflows/` (YAML).

Konten jurusan bersifat ringkas dan umum. Isi `data/jalur.json` harus diperiksa ulang tiap tahun. Tes tidak merekomendasikan sekolah tertentu.


Folder `dist/` dibuat oleh `./scripts/build.sh` dan tidak ikut di zip (ada di `.gitignore`); jalankan skrip itu untuk membuatnya.

## Efek visual (v24)
`js/ui/fx.js` dan `css/fx.css`: aurora latar, medan partikel yang menjauhi kursor, kilau kartu, riak sentuhan, kursor cincin dan percikan bintang, tombol magnet, kata berganti diketik, angka berhitung, garis langkah, parallax, konfeti di halaman hasil. Tingkat efek dipilih di Pengaturan (Otomatis, Penuh, Hemat, Mati). HP berspek rendah dan pengguna "kurangi gerakan" otomatis memakai Hemat atau Mati.

## Surga efek (v25)
`js/ui/surga.js` dan `css/surga.css`: meteor dan kunang-kunang di layar, kembang api tiap klik atau sentuhan, jejak komet pelangi di kursor, orbit tujuh ikon bidang minat di beranda, judul yang diacak lalu tersusun, kartu muncul dengan balik 3D, tombol berdenyut neon, dan telur paskah (ketuk logo 5 kali untuk pertunjukan kembang api). Pilih Surga di Pengaturan; Otomatis memakai Surga di perangkat kuat dan Hemat di HP lemah.
