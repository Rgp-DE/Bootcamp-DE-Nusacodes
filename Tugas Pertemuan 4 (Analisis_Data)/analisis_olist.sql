-- 1. Performa Produk (Terlaris & Paling Menguntungkan)
SELECT 
    p.product_category_name AS kategori_produk,
    COUNT(oi.order_id) AS total_barang_terjual,
    SUM(oi.price) AS total_pendapatan
FROM order_items_dataset oi
JOIN products_dataset p ON oi.product_id = p.product_id
WHERE p.product_category_name != ''
GROUP BY p.product_category_name
ORDER BY total_pendapatan DESC
LIMIT 10;

-- 2. Performa Seller / Penjual
SELECT 
    s.seller_id,
    s.seller_city AS asal_kota,
    COUNT(oi.order_id) AS total_pesanan,
    SUM(oi.price) AS total_pendapatan
FROM order_items_dataset oi
JOIN sellers_dataset s ON oi.seller_id = s.seller_id
GROUP BY s.seller_id, s.seller_city
ORDER BY total_pendapatan DESC
LIMIT 10;

-- 3. Analisis Review / Kepuasan Pelanggan
SELECT 
    review_score AS bintang,
    COUNT(review_id) AS jumlah_ulasan,
    ROUND((COUNT(review_id) * 100.0 / (SELECT COUNT(*) FROM order_reviews_dataset)), 2) AS persentase_keseluruhan
FROM order_reviews_dataset
GROUP BY review_score
ORDER BY review_score DESC;