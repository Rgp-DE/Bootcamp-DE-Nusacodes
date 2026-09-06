# Tugas Pertemuan 5 - dbt Transformation

Project ini merupakan tugas bootcamp Data Engineering Nusacodes pada materi **dbt (data build tool)**.

Pada tugas ini, dbt digunakan untuk melakukan transformasi data Brazilian E-Commerce / Olist yang sebelumnya sudah dimuat ke ClickHouse.

Transformasi dibagi menjadi dua layer utama:

- Silver Layer
- Gold Layer

## Tech Stack

- Python
- dbt Core
- dbt-clickhouse
- ClickHouse
- Docker
- SQL
- VS Code

## Data Flow

```text
Raw Tables in ClickHouse
        |
        v
Silver Layer
        |
        v
Gold Layer
Silver Layer

Silver Layer digunakan untuk membaca dan menyiapkan data dari tabel raw ClickHouse.

Model yang digunakan:

silver_dim_customers
silver_dim_products
silver_dim_sellers
silver_fact_order_items
silver_fact_orders
silver_fact_payments
silver_fact_reviews
Gold Layer

Gold Layer digunakan untuk membentuk tabel yang lebih siap digunakan untuk kebutuhan analitik.

Model yang digunakan:

gold_dim_customers
gold_dim_products
gold_dim_sellers
gold_fct_orders
Source Data

Data source berasal dari tabel Olist yang sebelumnya sudah dimuat ke ClickHouse:

customers_dataset
orders_dataset
order_items_dataset
order_payments_dataset
order_reviews_dataset
products_dataset
sellers_dataset
product_category_name_translation

Source dbt didefinisikan melalui file YAML dan dipetakan ke tabel raw ClickHouse menggunakan source().

Contoh:

SELECT *
FROM {{ source('public', 'dim_customer') }}
Menjalankan Project

Aktifkan virtual environment:

source .venv/bin/activate

Load environment variables:

set -a
source .env
set +a

Set lokasi profile dbt:

export DBT_PROFILES_DIR="$(pwd)"

Validasi konfigurasi:

dbt debug

Parse project:

dbt parse

Melihat model yang terdaftar:

dbt ls

Menjalankan Silver Layer:

dbt run --select path:models/silver

Menjalankan Gold Layer:

dbt run --select path:models/gold

Menjalankan seluruh model:

dbt run
Project Structure
olist_transform/
├── analyses/
├── macros/
├── models/
│   ├── silver/
│   └── gold/
├── seeds/
├── snapshots/
├── tests/
├── dbt_project.yml
├── profiles.yml
├── .env
├── .gitignore
└── README.md

File .env, .venv, target, dan logs tidak disimpan ke repository karena merupakan konfigurasi lokal atau generated files.

Learning Outcomes

Dari tugas ini saya mempelajari:

Struktur project dbt
Menghubungkan dbt dengan ClickHouse
Mendefinisikan source menggunakan YAML
Menggunakan fungsi source() dan ref()
Membuat transformasi Silver dan Gold
Menjalankan model dbt melalui CLI
Memahami dependency antar-model
Menangani konfigurasi environment pada project dbt
Notes

Model Silver dan Gold pada tugas ini mengikuti materi dan query yang diberikan selama bootcamp Data Engineering Nusacodes, kemudian dijalankan dan diuji menggunakan environment lokal berbasis Docker dan ClickHouse.
