# 🚀 Proyek Pipeline ETL Sederhana - Dicoding

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15%2B-blue?logo=postgresql)
![Google Sheets](https://img.shields.io/badge/Google%20Sheets-API-orange?logo=google-sheets)
![Coverage](https://img.shields.io/badge/Test%20Coverage-80%25%2B-brightgreen)
![License](https://img.shields.io/badge/License-MIT-green)

Sebuah pipeline ETL (Extract, Transform, Load) end-to-end yang dibangun dengan Python sebagai proyek akhir untuk kelas "Belajar Fundamental Pemrosesan Data" dari Dicoding.

[📖 Dokumentasi](#-dokumentasi) • [🚀 Cara Menggunakan](#-cara-menggunakan) • [🧪 Testing](#-testing) • [📁 Struktur Proyek](#-struktur-proyek)

</div>

## ✨ Fitur Utama

- **📄 Extract**: Web scraping data produk dari situs e-commerce fiktif menggunakan Requests dan BeautifulSoup
- **🔄 Transform**: Pembersihan dan transformasi data dengan Pandas
- **💾 Load**: Penyimpanan data ke berbagai repositori:
  - File CSV lokal
  - Google Sheets API
  - Database PostgreSQL
- **🧪 Testing**: Unit test komprehensif dengan coverage >80%
- **⚡ Otomatisasi**: Pipeline ETL terintegrasi penuh

## 🚀 Cara Menggunakan

### 1. Kloning Repositori

```bash
git clone https://github.com/mMuhammadFauzanFachruziRauf/proyek-etl-fashion-dicoding.git
cd proyek-etl-fashion-dicoding
```

### 2. Setup Environment

```bash
# Buat virtual environment
python -m venv venv

# Aktifkan virtual environment
# Untuk Windows:
.\venv\Scripts\activate
# Untuk MacOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Konfigurasi

1. **Google Sheets API**:
   - Siapkan file kredensial `google-sheets-api.json`
   - Letakkan di direktori utama proyek
   - Pastikan akun layanan memiliki akses ke Google Sheet target

2. **Database PostgreSQL**:
   - Atur koneksi database di file `main.py`
   - Sesuaikan parameter: host, database, user, password

3. **Google Sheet URL**:
   - Pastikan URL Google Sheet sudah benar di `main.py`

### 4. Menjalankan Pipeline

```bash
python main.py
```

## 🧪 Testing

Jalankan test suite untuk memastikan semua fungsi bekerja dengan benar:

```bash
# Menjalankan semua test
python -m pytest tests/

# Menjalankan test dengan coverage report
python -m pytest --cov=utils tests/

# Menghasilkan detailed coverage report
python -m pytest --cov=utils --cov-report=html tests/
```

## 📁 Struktur Proyek

```
proyek-etl-fashion-dicoding/
├── main.py                 # Skrip utama pipeline ETL
├── requirements.txt        # Dependencies Python
├── google-sheets-api.json  # Kredensial Google API (diabaikan di git)
├── utils/
│   ├── __init__.py
│   ├── extract.py         # Modul ekstraksi data
│   ├── transform.py       # Modul transformasi data
│   └── load.py           # Modul loading data
├── tests/
│   ├── __init__.py
│   ├── test_extract.py    # Test untuk modul extract
│   ├── test_transform.py  # Test untuk modul transform
│   └── test_load.py      # Test untuk modul load
├── products.csv          # Output file CSV (dihasilkan otomatis)
└── README.md            # Dokumentasi proyek
```

## 📖 Dokumentasi

### Modul Extract
Melakukan web scraping dari website fashion-studio.dicoding.dev untuk mendapatkan data produk fashion.

### Modul Transform
Membersihkan dan memproses data mentah:
- Konversi format harga ke numerik
- Penyesuaian tipe data
- Pembersihan nilai kosong/rusak

### Modul Load
Menyimpan data yang telah diproses ke:
- **CSV File**: `products.csv` di lokal
- **Google Sheets**: Untuk kolaborasi tim
- **PostgreSQL**: Untuk analisis data lanjutan

## 🤝 Kontribusi

Kontribusi selalu diterima! Silakan:
1. Fork project ini
2. Buat branch fitur Anda (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan Anda (`git commit -m 'Add AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

## 📝 Lisensi

Distributed under the MIT License. Lihat `LICENSE` untuk informasi lebih lanjut.

## 🙏 Penghargaan

Proyek ini dikembangkan sebagai bagian dari kelas [Belajar Fundamental Pemrosesan Data](https://www.dicoding.com/academies/630) di Dicoding Indonesia.

---

<div align="center">
Dibuat dengan ❤️ oleh Muhammad Fauzan Fachruzi Rauf
</div>
