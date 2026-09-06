# Tugas Pertemuan 2 - ETL dengan Pandas & SQLite

Tugas ini merupakan implementasi ETL sederhana pada Bootcamp Data Engineering Nusacodes menggunakan dataset Brazilian E-Commerce / Olist.

Pada tugas ini, data review pelanggan diekstrak dari file CSV, dibersihkan dan ditransformasi menggunakan Pandas, kemudian hasil akhirnya dimuat ke database SQLite.

## Tech Stack

- Python
- Pandas
- SQLAlchemy
- SQLite
- VS Code

## Data Flow

```text
order_reviews_dataset.csv
          |
          v
       Extract
          |
          v
      Transform
          |
          v
        Load
          |
          v
tugas_de2.db
cleaned_reviews
Extract

Data dibaca dari file:

order_reviews_dataset.csv

menggunakan Pandas.

Transform

Transformasi yang dilakukan:

Menyeragamkan nama kolom menjadi lowercase
Menghapus data dengan review_comment_message kosong
Membuat kolom panjang_karakter
Menghitung jumlah karakter pada setiap review
Memfilter review dengan panjang komentar lebih dari 50 karakter

Contoh logika transformasi:

df.columns = [col.lower() for col in df.columns]

df_clean = df.dropna(
    subset=['review_comment_message']
).copy()

df_clean['panjang_karakter'] = (
    df_clean['review_comment_message']
    .astype(str)
    .apply(len)
)

df_clean = df_clean[
    df_clean['panjang_karakter'] > 50
]
Load

Data hasil transformasi dimuat ke SQLite:

Database : tugas_de2.db
Table    : cleaned_reviews

Proses load dilakukan menggunakan SQLAlchemy dan Pandas.

Project Files
Tugas Pertemuan 2/
├── etl_tugas2.py
├── order_reviews_dataset.csv
├── tugas_de2.db
└── README.md
Running

Jalankan script:

python etl_tugas2.py
Learning Outcomes

Melalui tugas ini saya mempelajari:

Dasar proses ETL
Membaca CSV dengan Pandas
Data cleaning
Membuat derived column
Filtering data
Menghubungkan Python dengan SQLite
Menyimpan DataFrame ke database menggunakan SQLAlchemy
