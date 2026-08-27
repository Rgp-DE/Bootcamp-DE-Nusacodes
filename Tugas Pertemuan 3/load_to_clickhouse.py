import pandas as pd
import os
from sqlalchemy import create_engine, text

def load_all_csv_to_clickhouse():
    print("Mulai proses ELT ke ClickHouse...")
    
    # Bikin koneksi ke ClickHouse
    engine = create_engine('clickhouse+native://default:admin123@localhost/default')
    
    csv_files = [
        'customers_dataset.csv', 'geolocation_dataset.csv',
        'order_items_dataset.csv', 'order_payments_dataset.csv',
        'order_reviews_dataset.csv', 'orders_dataset.csv',
        'product_category_name_translation.csv', 'products_dataset.csv',
        'sellers_dataset.csv'
    ]
    
    for file in csv_files:
        if os.path.exists(file):
            print("=========================================")
            print(f"1. Extracting {file}...")
            
            # Baca CSV
            df = pd.read_csv(file)
            df.columns = [col.lower() for col in df.columns]
            table_name = file.replace('.csv', '')
            
            # [JURUS NUKLIR] Mapping Tipe Data & Sapu Bersih Null Sekaligus!
            kolom_db = []
            for col_name in df.columns:
                dtype = str(df[col_name].dtype)
                
                if "int" in dtype:
                    # Paksa jadi int64 dan isi null dengan 0
                    df[col_name] = df[col_name].fillna(0).astype('int64')
                    kolom_db.append(f"{col_name} Int64")
                elif "float" in dtype:
                    # Paksa jadi float64 dan isi null dengan 0.0
                    df[col_name] = df[col_name].fillna(0.0).astype('float64')
                    kolom_db.append(f"{col_name} Float64")
                else:
                    # SELAIN ANGKA, PAKSA JADI STRING MUTLAK!
                    df[col_name] = df[col_name].fillna("").astype(str)
                    kolom_db.append(f"{col_name} String")
            
            # Rakit query CREATE TABLE
            create_query = f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                {', '.join(kolom_db)}
            ) ENGINE = MergeTree()
            ORDER BY tuple()
            """
            
            # Eksekusi bikin tabel
            with engine.begin() as conn:
                conn.execute(text(f"DROP TABLE IF EXISTS {table_name}"))
                conn.execute(text(create_query))
            
            # Load datanya
            print(f"2. Loading {len(df)} baris ke {table_name}...")
            df.to_sql(table_name, con=engine, if_exists='append', index=False)
            print(f">>> Sukses load {table_name}!\n")
            
        else:
            print(f"WARNING: File {file} tidak ditemukan di folder ini.\n")

if __name__ == "__main__":
    load_all_csv_to_clickhouse()