import pandas as pd

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Fungsi untuk membersihkan dan mentransformasi DataFrame produk
    sesuai dengan kriteria Skilled (harga dalam Rupiah & ada timestamp).
    """
    try:
        print("Starting data transformation...")
        
        df_transformed = df.copy()

        # 1. Membersihkan kolom 'price' dan konversi ke Rupiah (int64)
        price_cleaned = df_transformed['price'].replace({r'\$': '', ',': ''}, regex=True)
        price_numeric = pd.to_numeric(price_cleaned, errors='coerce')
        # Kalikan dengan 16000 untuk konversi ke Rupiah
        df_transformed['price'] = price_numeric * 16000
        
        # 2. Membersihkan dan mengekstrak nilai numerik dari 'rating'
        df_transformed['rating'] = df_transformed['rating'].str.extract(r'(\d+\.\d+)').astype(float)
        
        # 3. Membersihkan dan mengekstrak jumlah warna dari 'colors'
        df_transformed['colors'] = df_transformed['colors'].str.extract(r'(\d+)').astype(int)
        
        # 4. Membersihkan kolom 'size' dan 'gender'
        df_transformed['size'] = df_transformed['size'].str.replace('Size: ', '', regex=False)
        df_transformed['gender'] = df_transformed['gender'].str.replace('Gender: ', '', regex=False)

        # 5. Mengubah nama kolom agar konsisten dan deskriptif
        df_transformed.rename(columns={'price': 'price_idr'}, inplace=True)

        # --- Tahap Pembersihan Kualitas Data ---
        df_transformed = df_transformed[df_transformed['title'] != 'Unknown Product']
        df_transformed.dropna(inplace=True)
        df_transformed.drop_duplicates(inplace=True)

        # 6. Menyesuaikan tipe data final, termasuk mempertahankan timestamp
        df_transformed = df_transformed.astype({
            'title': 'object',
            'price_idr': 'int64',
            'rating': 'float64',
            'colors': 'int64',
            'size': 'object',
            'gender': 'object',
            'timestamp': 'datetime64[ns]'
        })

        print("Data transformation complete.")
        return df_transformed.reset_index(drop=True)

    except Exception as e:
        print(f"An error occurred during data transformation: {e}")
        return pd.DataFrame()

