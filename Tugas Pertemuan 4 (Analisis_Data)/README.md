# Tugas Pertemuan 4 - Analisis Data dengan ClickHouse

Tugas ini merupakan tahap analisis data setelah dataset Brazilian E-Commerce / Olist berhasil dimuat ke ClickHouse.

Analisis dilakukan menggunakan dua pendekatan:

1. SQL Native
2. Python Integration

## Tech Stack

- ClickHouse
- SQL
- Python
- Pandas
- SQLAlchemy
- VS Code

## Business Objectives

Analisis difokuskan pada tiga area utama:

### 1. Product Performance

Mengidentifikasi kategori produk dengan performa terbaik berdasarkan:

- Total barang terjual
- Total pendapatan

### 2. Seller Performance

Menganalisis kontribusi seller berdasarkan:

- Seller ID
- Kota asal
- Total pesanan
- Total pendapatan

### 3. Customer Satisfaction

Menganalisis distribusi `review_score` untuk melihat tingkat kepuasan pelanggan.

## SQL Analysis

File:

```text
analisis_olist.sql

digunakan untuk melakukan join dan agregasi langsung di ClickHouse.

Contoh alur analisis:

ClickHouse Tables
      |
      v
SQL JOIN
      |
      v
Aggregation
      |
      v
Business Metrics

Query mencakup analisis:

Performa produk
Performa seller
Kepuasan pelanggan
Python Integration

File:

analisis_python.py

digunakan untuk menjalankan query ke ClickHouse dari Python dan mengambil hasil analisis ke Pandas DataFrame.

Alur:

Python
   |
   v
SQLAlchemy
   |
   v
ClickHouse
   |
   v
SQL Query
   |
   v
Pandas DataFrame
Running

Pastikan ClickHouse aktif:

docker start clickhouse-server

SQL dapat dijalankan menggunakan SQL client atau editor yang terhubung ke ClickHouse.

Untuk Python:

python analisis_python.py
Project Files
Tugas Pertemuan 4 (Analisis_Data)/
├── analisis_olist.sql
├── analisis_python.py
├── .gitignore
└── README.md
Learning Outcomes

Melalui tugas ini saya mempelajari:

Analytical SQL
JOIN antar tabel
Aggregation
GROUP BY
ORDER BY
Analisis product performance
Analisis seller performance
Analisis customer review
Menjalankan query ClickHouse melalui Python
Mengambil hasil query ke Pandas DataFrame
