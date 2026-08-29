import pandas as pd
from sqlalchemy import create_engine

def analisis_review():
    # Nyambungin Python ke ClickHouse
    engine = create_engine('clickhouse+native://default:admin123@localhost/default')
    
    # Query SQL yang mau dieksekusi
    query = """
    SELECT 
        review_score AS bintang,
        COUNT(review_id) AS jumlah_ulasan,
        ROUND((COUNT(review_id) * 100.0 / (SELECT COUNT(*) FROM order_reviews_dataset)), 2) AS persentase
    FROM order_reviews_dataset
    GROUP BY review_score
    ORDER BY review_score DESC;
    """
    
    # Pandas narik data dari ClickHouse berdasarkan query di atas
    df_hasil = pd.read_sql(query, con=engine)
    
    print("=== HASIL ANALISIS KEPUASAN PELANGGAN OLIST ===")
    print(df_hasil.to_string(index=False))
    print("===============================================")

if __name__ == "__main__":
    analisis_review()