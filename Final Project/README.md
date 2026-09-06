# Final Project - End-to-End Data Engineering Pipeline

Final Project ini merupakan bagian dari **Bootcamp Data Engineering Nusacodes**.

Project ini membangun pipeline Data Engineering end-to-end menggunakan dataset Brazilian E-Commerce / Olist dengan proses ingestion, transformation, orchestration, dan data validation.

Pipeline diorkestrasi menggunakan Apache Airflow, sedangkan ClickHouse digunakan sebagai OLAP database dan dbt digunakan untuk membangun transformasi data pada layer Silver dan Gold.

---

## Architecture

```text
                    Apache Airflow
                         |
                         v
                check_clickhouse
                         |
                         v
                 ingest_raw_data
                         |
                         v
                     ClickHouse
                   Raw / Bronze
                         |
                         v
                    dbt Silver
                         |
                         v
                     dbt Gold
                         |
                         v
                  validate_data

Pipeline berjalan secara berurutan:

Olist CSV
   |
   v
Python Ingestion
   |
   v
ClickHouse Raw Tables
   |
   v
dbt Silver Layer
   |
   v
dbt Gold Layer
   |
   v
Data Validation
Tech Stack
Python
Pandas
SQLAlchemy
ClickHouse
dbt Core
dbt-clickhouse
Apache Airflow
PostgreSQL
Docker
Docker Compose
SQL
VS Code
DBeaver
Git
GitHub
Dataset

Dataset yang digunakan adalah Brazilian E-Commerce / Olist.

Dataset terdiri dari 9 file CSV:

customers_dataset.csv
geolocation_dataset.csv
order_items_dataset.csv
order_payments_dataset.csv
order_reviews_dataset.csv
orders_dataset.csv
product_category_name_translation.csv
products_dataset.csv
sellers_dataset.csv

Dataset lokal disimpan di:

data/

Dataset tidak disimpan ke repository karena sudah dimasukkan ke .gitignore.

Pipeline Stages
1. Extract / Ingestion

File:

ingestion/load_to_clickhouse.py

Script ingestion melakukan:

Membaca seluruh CSV menggunakan Pandas
Menormalisasi nama kolom
Mendeteksi tipe data
Menangani nilai null
Membuat tabel ClickHouse
Memuat data ke ClickHouse

Raw tables yang dihasilkan antara lain:

customers_dataset
geolocation_dataset
order_items_dataset
order_payments_dataset
order_reviews_dataset
orders_dataset
product_category_name_translation
products_dataset
sellers_dataset
2. Silver Layer

Transformasi Silver dilakukan menggunakan dbt.

Directory:

dbt/olist_transform/models/silver/

Model:

silver_dim_customers
silver_dim_products
silver_dim_sellers
silver_fact_order_items
silver_fact_orders
silver_fact_payments
silver_fact_reviews

Silver Layer digunakan untuk membersihkan dan menyiapkan data dari raw tables.

Pada silver_fact_orders, kolom waktu diproses menggunakan parsing DateTime yang aman terhadap nilai kosong.

3. Gold Layer

Directory:

dbt/olist_transform/models/gold/

Model:

gold_dim_customers
gold_dim_products
gold_dim_sellers
gold_fct_orders

Gold Layer digunakan untuk menghasilkan tabel yang lebih siap digunakan untuk kebutuhan analitik.

4. Data Validation

File:

scripts/validate_data.py

Validation script memeriksa beberapa tabel utama dan memastikan tabel tidak kosong.

Contoh hasil validation:

customers_dataset: 99,441 rows
orders_dataset: 99,441 rows
silver_dim_customers: 99,441 rows
silver_fact_orders: 99,441 rows
gold_dim_customers: 99,441 rows
gold_fct_orders: 98,207 rows

All validation checks passed.
Airflow Orchestration

Airflow digunakan sebagai workflow orchestrator.

DAG:

olist_end_to_end_pipeline

File:

airflow/dags/olist_pipeline.py

Task flow:

check_clickhouse
       |
       v
ingest_raw_data
       |
       v
dbt_silver
       |
       v
dbt_gold
       |
       v
validate_data

Semua task dijalankan secara dependency-based. Jika sebuah task gagal, task berikutnya tidak akan dijalankan.

DAG dijadwalkan menggunakan schedule harian:

@daily
Docker Services

Infrastructure dijalankan menggunakan Docker Compose.

Services:

PostgreSQL
ClickHouse
Airflow API Server
Airflow Scheduler
Airflow DAG Processor

PostgreSQL digunakan sebagai metadata database untuk Airflow.

ClickHouse digunakan sebagai OLAP database utama.

Project Structure
Final Project/
│
├── airflow/
│   └── dags/
│       └── olist_pipeline.py
│
├── data/
│
├── dbt/
│   └── olist_transform/
│       ├── models/
│       │   ├── silver/
│       │   └── gold/
│       ├── macros/
│       ├── analyses/
│       ├── seeds/
│       ├── snapshots/
│       ├── tests/
│       ├── dbt_project.yml
│       └── profiles.yml
│
├── ingestion/
│   └── load_to_clickhouse.py
│
├── scripts/
│   └── validate_data.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
Environment Variables

Copy:

cp .env.example .env

Contoh konfigurasi:

CLICKHOUSE_HOST=clickhouse
CLICKHOUSE_HTTP_PORT=8123
CLICKHOUSE_NATIVE_PORT=9000
CLICKHOUSE_USER=default
CLICKHOUSE_PASSWORD=your_password
CLICKHOUSE_DATABASE=default

AIRFLOW_UID=50000

File .env tidak disimpan ke repository.

Running the Project
1. Build Docker images
docker compose build
2. Initialize Airflow
docker compose up airflow-init
3. Start services
docker compose up -d
4. Check services
docker compose ps
5. Check ClickHouse
curl http://localhost:8123/ping

Expected:

Ok.
6. Open Airflow UI
http://localhost:8080
7. Run DAG

Cari DAG:

olist_end_to_end_pipeline

Kemudian trigger DAG melalui Airflow UI.

Manual Testing

Ingestion:

docker compose exec airflow-scheduler \
python /opt/airflow/project/ingestion/load_to_clickhouse.py

dbt debug:

docker compose exec airflow-scheduler \
bash -c '
cd /opt/airflow/project/dbt/olist_transform &&
dbt debug
'

Run Silver:

docker compose exec airflow-scheduler \
bash -c '
cd /opt/airflow/project/dbt/olist_transform &&
dbt run --select path:models/silver
'

Run Gold:

docker compose exec airflow-scheduler \
bash -c '
cd /opt/airflow/project/dbt/olist_transform &&
dbt run --select path:models/gold
'

Validation:

docker compose exec airflow-scheduler \
python /opt/airflow/project/scripts/validate_data.py
Database Access

ClickHouse dapat diakses melalui DBeaver menggunakan:

Host     : localhost
Port     : 8123
Database : default
User     : default
Password : sesuai konfigurasi .env
Result

Final pipeline berhasil menjalankan seluruh task:

check_clickhouse     SUCCESS
ingest_raw_data      SUCCESS
dbt_silver           SUCCESS
dbt_gold             SUCCESS
validate_data        SUCCESS

Pipeline berhasil mengintegrasikan proses ingestion, transformation, orchestration, dan validation dalam satu workflow.

Learning Outcomes

Melalui Final Project ini saya mempelajari:

Mendesain pipeline Data Engineering end-to-end
Menjalankan ClickHouse menggunakan Docker
Mengelola multi-file ingestion
Menggunakan dbt untuk transformasi data
Membangun Silver dan Gold Layer
Menggunakan Apache Airflow sebagai workflow orchestrator
Membuat dependency antar task
Mengimplementasikan scheduling
Menggunakan PostgreSQL sebagai Airflow metadata database
Menangani environment variables
Menangani komunikasi antar Docker containers
Melakukan data validation
Melakukan troubleshooting pada pipeline terorkestrasi
Bootcamp

Project ini dibuat sebagai Final Project pada:

Bootcamp Data Engineering - Nusacodes
