# main.py

from utils.extract import extract_data
from utils.transform import transform_data
from utils.load import load_to_csv, load_to_gdrive, load_to_postgres

# --- KONFIGURASI ---
CSV_FILENAME = "products.csv"
GOOGLE_SHEET_URL = "https://docs.google.com/spreadsheets/d/1cScrJycrAANmFCtUdP8dnkgskaXpyz40AtF_gG5p7rA/edit?usp=sharing"
GDRIVE_CREDS_PATH = "google-sheets-api.json"
POSTGRES_DB_URI = "postgresql://postgres:postgres123@localhost:5432/fashion_db"
POSTGRES_TABLE_NAME = "fashion_products"


if __name__ == "__main__":
    # Tahap 1: Ekstraksi
    raw_df = extract_data()
    
    if not raw_df.empty:
        # Tahap 2: Transformasi
        cleaned_df = transform_data(raw_df)

        if not cleaned_df.empty:
            print("\n--- Cleaned Data Sample (After Transformation) ---")
            print("Verifikasi output ini dengan gambar dari reviewer:")
            cleaned_df.info() # Menampilkan info DataFrame yang sudah bersih
            print(cleaned_df.head()) # Menampilkan 5 baris pertama

            print("\n--- Starting Load Process ---")
            # Tahap 3: Pemuatan Data
            load_to_csv(cleaned_df, CSV_FILENAME)
            load_to_gdrive(cleaned_df, GOOGLE_SHEET_URL, GDRIVE_CREDS_PATH)
            
            # --- PERBAIKAN URUTAN ARGUMEN DI SINI ---
            load_to_postgres(cleaned_df, POSTGRES_DB_URI, POSTGRES_TABLE_NAME)
            
            print("\n--- ETL Pipeline Complete ---")
        else:
            print("Data transformation resulted in an empty DataFrame.")
    else:
        print("Extraction failed, no data to load.")

