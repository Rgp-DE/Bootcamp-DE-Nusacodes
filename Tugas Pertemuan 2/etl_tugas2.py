import pandas as pd
from sqlalchemy import create_engine

def run_etl():
    print("Mulai proses ETL dari file order_reviews_dataset.csv...")

    # ==========================================
    # 1. EXTRACT
    # ==========================================
    print("Extracting data dari CSV...")
    # Membaca dataset 
    df = pd.read_csv("order_reviews_dataset.csv") 
    
    # ==========================================
    # 2. TRANSFORM
    # ==========================================
    print("Transforming data...")
    # Menormalkan nama kolom jadi lowercase 
    df.columns = [col.lower() for col in df.columns]

    # Memfilter dan membuang baris yang nilai komentarnya null/kosong
    df_clean = df.dropna(subset=['review_comment_message']).copy()

    # Membuat kolom baru untuk menghitung jumlah karakter dari komentar
    df_clean['panjang_karakter'] = df_clean['review_comment_message'].astype(str).apply(len)
    
    # Memfilter dataset dan hanya menyisakan data dengan panjang karakter > 50
    df_clean = df_clean[df_clean['panjang_karakter'] > 50]
    print(f"Total baris bersih setelah difilter (> 50 karakter): {len(df_clean)}")

    # ==========================================
    # 3. LOAD
    # ==========================================
    print("Loading data ke Database SQLite...")
    # Menyimpan data ke database lokal dengan nama tugas_de2.db
    engine = create_engine('sqlite:///tugas_de2.db')
    
    # Tulis data ke tabel 'cleaned_reviews'
    df_clean.to_sql('cleaned_reviews', con=engine, if_exists='replace', index=False)
    
    print("Proses ETL Selesai. Data udah tersimpan di tugas_de2.db.")

if __name__ == "__main__":
    run_etl()