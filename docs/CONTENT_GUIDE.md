# Menambah konten
1. Tambah jurusan di `data/majors.json` (id harus unik, `lv` = SMK atau Kuliah, bobot `w` bernilai 1 sampai 3).
2. Tambah pertanyaan di `data/questions.json` (trait harus salah satu id di `traits.json`).
3. Jalankan `python3 tools/build_data.py python3 tools/build_data.py` lalupython3 tools/build_data.py` lalu python3 tools/build_site.py` lalu `node --test tests/data.test.js`.
4. Muat ulang browser.
