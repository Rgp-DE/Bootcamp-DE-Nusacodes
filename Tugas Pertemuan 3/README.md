# Tugas Pertemuan 3 - ELT Pipeline ke ClickHouse

Tugas ini merupakan implementasi ingestion pipeline untuk memuat dataset Brazilian E-Commerce / Olist ke ClickHouse.

ClickHouse dijalankan menggunakan Docker, sedangkan proses ingestion dibuat menggunakan Python, Pandas, SQLAlchemy, dan ClickHouse driver.

## Tech Stack

- Python
- Pandas
- SQLAlchemy
- ClickHouse
- Docker
- clickhouse-driver
- clickhouse-sqlalchemy
- VS Code

## Architecture

```text
Olist CSV Files
      |
      v
Python Ingestion Script
      |
      v
Schema Mapping
& Null Handling
      |
      v
ClickHouse
MergeTree Tables
Dataset

Pipeline memuat 9 dataset Olist:

customers_dataset.csv
geolocation_dataset.csv
order_items_dataset.csv
order_payments_dataset.csv
order_reviews_dataset.csv
orders_dataset.csv
product_category_name_translation.csv
products_dataset.csv
sellers_dataset.csv
Infrastructure

ClickHouse dijalankan sebagai Docker container.

Port utama:

8123 - HTTP Interface
9000 - Native Protocol

Container dapat dicek menggunakan:

docker ps
Pipeline Process

Script load_to_clickhouse.py melakukan proses:

Membaca setiap CSV menggunakan Pandas
Menormalisasi nama kolom
Mendeteksi tipe data setiap kolom
Melakukan handling terhadap nilai null
Membuat tabel ClickHouse secara dinamis
Menggunakan engine MergeTree
Memuat seluruh data ke ClickHouse
Schema Mapping

Tipe data dipetakan secara otomatis menjadi tipe yang sesuai untuk ClickHouse, seperti:

Integer -> Int64
Float   -> Float64
Other   -> String

Nilai null juga ditangani sebelum proses load untuk menghindari error saat insertion.

Running

Install dependency:

pip install -r requirements.txt

Pastikan ClickHouse container hidup:

docker start clickhouse-server

Kemudian jalankan:

python load_to_clickhouse.py
Output

Setelah pipeline berhasil dijalankan, seluruh dataset tersedia sebagai tabel ClickHouse dan dapat digunakan untuk kebutuhan analitik selanjutnya.

Project Files
Tugas Pertemuan 3/
├── load_to_clickhouse.py
├── requirements.txt
├── .gitignore
└── README.md

Dataset lokal tidak harus disimpan di repository apabila ukurannya besar.

Learning Outcomes

Melalui tugas ini saya mempelajari:

Menjalankan ClickHouse menggunakan Docker
Konsep OLAP database
Data ingestion multi-file
Dynamic schema mapping
Handling null values
ClickHouse MergeTree
Python dan SQLAlchemy integration
Membuat pipeline ingestion yang dapat memproses banyak file secara otomatis
