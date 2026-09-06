# Bootcamp Data Engineering - Nusacodes

Repository ini berisi kumpulan tugas dan Final Project yang saya kerjakan selama mengikuti **Bootcamp Data Engineering Nusacodes**.

Materi dan project dalam repository ini mencakup proses Data Engineering mulai dari fundamental ETL, data ingestion, OLAP database, analytical query, dbt transformation, hingga workflow orchestration menggunakan Apache Airflow.

---

## Learning Journey

```text
Data Engineering Fundamentals
          |
          v
ETL with Pandas & SQLite
          |
          v
Data Ingestion to ClickHouse
          |
          v
SQL & Python Analytics
          |
          v
dbt Transformation
Silver -> Gold
          |
          v
Apache Airflow Orchestration
          |
          v
End-to-End Final Project
Repository Structure
Bootcamp-DE-Nusacodes/
│
├── Tugas Pertemuan 2/
│   └── ETL menggunakan Pandas dan SQLite
│
├── Tugas Pertemuan 3/
│   └── Ingestion dataset Olist ke ClickHouse
│
├── Tugas Pertemuan 4 (Analisis_Data)/
│   └── Analisis data dengan SQL dan Python
│
├── Tugas Pertemuan 5 (Dbt)/
│   └── Transformasi data menggunakan dbt
│
├── Final Project/
│   └── End-to-End Data Engineering Pipeline
│
└── README.md
Pertemuan 1 - Data Engineering Fundamentals

Pertemuan pertama berisi pengenalan dan fundamental Data Engineering.

Materi bersifat teori sehingga tidak terdapat practical task pada repository.

Pertemuan 2 - ETL with Pandas & SQLite

Membangun pipeline ETL sederhana menggunakan dataset review dari Brazilian E-Commerce / Olist.

Pipeline:

CSV
 |
 v
Pandas
 |
 v
Data Cleaning
 |
 v
Transformation
 |
 v
SQLite

Topik:

Extract CSV
Data cleaning
Null handling
Derived column
Filtering
Load ke SQLite
SQLAlchemy

Directory:

Tugas Pertemuan 2/
Pertemuan 3 - ClickHouse Data Ingestion

Membangun ingestion pipeline untuk memuat beberapa dataset Olist ke ClickHouse.

Pipeline:

Multiple CSV
     |
     v
Python + Pandas
     |
     v
Schema Mapping
     |
     v
ClickHouse

Topik:

Docker
ClickHouse
OLAP database
Multi-file ingestion
Schema mapping
Null handling
MergeTree
SQLAlchemy

Directory:

Tugas Pertemuan 3/
Pertemuan 4 - Data Analytics

Melakukan analisis terhadap data Olist yang sudah dimuat ke ClickHouse.

Analisis mencakup:

Product performance
Seller performance
Customer satisfaction

Pendekatan:

SQL Native
    +
Python / Pandas

Directory:

Tugas Pertemuan 4 (Analisis_Data)/
Pertemuan 5 - dbt Transformation

Menggunakan dbt untuk membangun data transformation secara modular.

Pipeline:

Raw ClickHouse Tables
        |
        v
Silver Layer
        |
        v
Gold Layer

Topik:

dbt Core
dbt-clickhouse
Sources
Models
Jinja
source()
ref()
Silver Layer
Gold Layer

Directory:

Tugas Pertemuan 5 (Dbt)/
Final Project - End-to-End Data Engineering Pipeline

Final Project menggabungkan materi yang dipelajari sebelumnya menjadi sebuah pipeline Data Engineering end-to-end.

Architecture:

Olist CSV
   |
   v
Apache Airflow
   |
   v
Python Ingestion
   |
   v
ClickHouse Raw
   |
   v
dbt Silver
   |
   v
dbt Gold
   |
   v
Data Validation

Airflow menjalankan pipeline dengan dependency:

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

Seluruh task berhasil dijalankan melalui Airflow.

Directory:

Final Project/
Final Project Tech Stack
Python
Pandas
SQL
SQLAlchemy
ClickHouse
dbt
Apache Airflow
PostgreSQL
Docker
Docker Compose
DBeaver
Git
GitHub
Final Project Architecture
                    Apache Airflow
                         |
                         v
                  Python Ingestion
                         |
                         v
                     ClickHouse
                   Raw / Bronze
                         |
                         v
                      dbt
                         |
              +----------+----------+
              |                     |
              v                     v
           Silver                 Gold
                                      |
                                      v
                               Data Validation
Dataset

Sebagian besar practical task menggunakan:

Brazilian E-Commerce / Olist Dataset

Dataset digunakan secara bertahap untuk:

ETL
Data ingestion
OLAP storage
SQL analysis
Python analysis
dbt transformation
Airflow orchestration

Penggunaan dataset yang sama membuat setiap tugas membentuk tahapan Data Engineering yang saling berhubungan.

Bootcamp Progress
[✓] Data Engineering Fundamentals
[✓] ETL with Pandas & SQLite
[✓] ClickHouse Data Ingestion
[✓] SQL & Python Analytics
[✓] dbt Silver & Gold Transformation
[✓] Apache Airflow Orchestration
[✓] End-to-End Final Project
What I Learned

Selama bootcamp ini saya mempelajari:

Fundamental Data Engineering
ETL dan ELT
Data ingestion
Data cleaning
Python for Data Engineering
Pandas
SQL
SQLite
ClickHouse
OLAP database
Docker
SQLAlchemy
Analytical SQL
dbt
Silver & Gold Layer
Workflow orchestration
Apache Airflow
Scheduling
Docker Compose
Data validation
Git & GitHub
Troubleshooting pipeline end-to-end
About

Repository ini merupakan dokumentasi perjalanan belajar saya dalam Bootcamp Data Engineering Nusacodes, mulai dari fundamental hingga membangun pipeline Data Engineering end-to-end menggunakan Apache Airflow, dbt, ClickHouse, Python, dan Docker.
