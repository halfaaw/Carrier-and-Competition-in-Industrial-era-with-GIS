# Studi Kasus Sesi 3: Automasi Analisis Spasial dan Manajemen Aset dengan GIS

## 1. Latar Belakang
PT Maju Bersama (perusahaan fiktif) berencana memperluas jangkauan layanan logistik dan penempatan aset cabang baru. Perusahaan membutuhkan analisis geografis untuk memastikan titik-titik cabang berada di dalam radius pelayanan yang optimal dari pusat distribusi, serta mempermudah pemetaan infrastruktur kota. Studi kasus ini membuat alur analitik spasial yang dapat diulang menggunakan Python.

Keterkaitan dengan seminar: Proyek ini terinspirasi dari materi "Career and Competition in Industrial era with GIS" oleh narasumber Widi Primadepa. Proyek ini menekankan peran sarjana IT sebagai *GIS Developer* yang mengautomasi pemrosesan data spasial menggunakan pustaka *open-source*, alih-alih hanya bergantung pada perangkat lunak GUI berbayar. Proyek ini juga mengutamakan validasi koordinat spasial (*data preparation* geospatial).

## 2. Tujuan
- Memvalidasi dan menyiapkan data koordinat geospasial (*Point* dan *Polygon*) sebelum analisis.
- Melakukan transformasi data spasial dan pembuatan *buffer* radius pelayanan.
- Melatih logika pemrograman untuk mengecek apakah suatu aset berada di dalam wilayah jangkauan (*spatial join/within*).
- Menghasilkan evaluasi berupa visualisasi peta spasial yang bisa diperiksa kembali.
- Menuliskan batasan analisis bahwa pemetaan otomatis ini memerlukan verifikasi lapangan (*ground checking*) untuk memastikan akurasi data di dunia nyata.

## 3. Data
File `data/assets_data.csv` berisi data sintetis yang dibuat khusus untuk latihan, bukan data geospasial perusahaan atau kota sungguhan. Setiap baris adalah satu catatan aset/cabang.

| Kolom | Arti |
|---|---|
| `asset_id` | ID unik untuk setiap aset atau titik cabang |
| `latitude` | Garis lintang koordinat geografis |
| `longitude` | Garis bujur koordinat geografis |
| `category` | Kategori fasilitas (misal: Hub, Cabang, Gudang) |
| `status_operational` | Status aktual operasional (Active / Inactive) sebagai parameter |

Konsep yang digunakan:
- Koordinat spasial divalidasi dan diubah menjadi objek geometri Shapely/GeoPandas.
- Evaluasi jangkauan = Pengecekan apakah titik aset berada di dalam batasan poligon *buffer* radius.
- Visualisasi digunakan untuk membedah seberapa banyak titik cabang yang terlayani vs di luar jangkauan.

## 4. Struktur Proyek
studi-kasus-sesi-3-gis/
├── data/
│   └── assets_data.csv
├── src/
│   └── spatial_analysis.py
├── tests/
│   └── test_spatial.py
├── outputs/
│   └── charts/             # peta spasial dibuat ketika program dijalankan
├── README.md
└── requirements.txt
