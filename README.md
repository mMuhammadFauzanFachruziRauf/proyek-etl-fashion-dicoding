<div align="center">
<h1 align="center">🚀 Proyek Pipeline ETL Sederhana - Dicoding</h1>
<p align="center">
Sebuah pipeline ETL (Extract, Transform, Load) end-to-end yang dibangun dengan Python sebagai proyek akhir untuk kelas "Belajar Fundamental Pemrosesan Data" dari Dicoding.
</p>
</div>

<div align="center">

</div>

✨ Fitur Utama
Proyek ini mencakup seluruh alur kerja ETL dari ekstraksi data hingga pemuatan ke berbagai repositori data.

📄 Extract: Melakukan web scraping data produk dari situs e-commerce fiktif (fashion-studio.dicoding.dev) menggunakan requests dan BeautifulSoup.

🔄 Transform: Membersihkan dan mentransformasi data mentah menjadi dataset yang siap analisis. Proses ini mencakup konversi harga ke format numerik dan penyesuaian tipe data untuk konsistensi.

💾 Load: Memuat data yang telah bersih ke dalam tiga repositori berbeda untuk fleksibilitas penyimpanan dan analisis:

File CSV: Disimpan secara lokal sebagai products.csv.

Google Sheets: Dimuat ke lembar kerja Google untuk kolaborasi dan visualisasi mudah.

Database PostgreSQL: Dimasukkan ke dalam tabel database relasional untuk kueri yang lebih kompleks.

🧪 Testing: Dilengkapi dengan unit test menggunakan pytest untuk memastikan setiap modul (extract, transform, load) berfungsi sesuai harapan. Laporan test coverage menunjukkan cakupan kode di atas 80% untuk menjamin keandalan pipeline.

⚙️ Cara Menjalankan Proyek
Ikuti langkah-langkah di bawah ini untuk menjalankan pipeline ETL di lingkungan lokal Anda.

1. Clone Repositori
Pertama, clone repositori ini ke mesin lokal Anda menggunakan Git.

git clone [https://github.com/NAMA_USER_ANDA/proyek-etl-fashion-dicoding.git](https://github.com/NAMA_USER_ANDA/proyek-etl-fashion-dicoding.git)
cd proyek-etl-fashion-dicoding

2. Buat dan Aktifkan Virtual Environment
Sangat disarankan untuk menggunakan virtual environment agar dependensi proyek tidak bercampur dengan instalasi Python global Anda.

# Buat virtual environment
python -m venv venv

# Aktifkan (untuk MacOS/Linux)
source venv/bin/activate

# Aktifkan (untuk Windows)
.\venv\Scripts\activate

3. Instal Dependensi
Instal semua pustaka Python yang dibutuhkan yang tercantum dalam file requirements.txt.

pip install -r requirements.txt

4. Konfigurasi
Sebelum menjalankan pipeline, Anda perlu melakukan beberapa konfigurasi:

Google Sheets API: Siapkan file kredensial google-sheets-api.json Anda dan letakkan di direktori utama proyek. Pastikan akun layanan memiliki akses ke Google Sheet target.

Koneksi Database: Atur detail koneksi database PostgreSQL (host, nama database, user, password) di dalam file main.py.

URL Google Sheet: Pastikan URL Google Sheet yang akan dituju sudah benar di dalam main.py.

⚡ Menjalankan Pipeline
Setelah semua konfigurasi selesai, jalankan pipeline utama dengan perintah berikut:

python main.py

Skrip akan menjalankan proses ETL secara berurutan dan menampilkan log status di terminal.

🧪 Menjalankan Tes
Untuk memastikan semua fungsi berjalan dengan benar, Anda dapat menjalankan unit test yang telah disiapkan.

# Menjalankan semua unit test
python -m pytest tests/

# Menjalankan tes dan melihat laporan coverage
python -m pytest --cov=utils tests/
