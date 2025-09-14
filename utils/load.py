# utils/load.py

import pandas as pd
from sqlalchemy import create_engine
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

def load_to_csv(df: pd.DataFrame, filename: str):
    """Menyimpan DataFrame ke file CSV."""
    try:
        df.to_csv(filename, index=False)
        print(f"Data successfully loaded to {filename}")
    except Exception as e:
        print(f"Error loading data to CSV: {e}")

def load_to_gdrive(df: pd.DataFrame, sheet_url: str, creds_path: str):
    """Menyimpan DataFrame ke Google Sheets dengan konversi data yang aman."""
    try:
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
        
        if not os.path.exists(creds_path):
            print(f"Error: Credentials file not found at '{creds_path}'")
            return
            
        creds = ServiceAccountCredentials.from_json_keyfile_name(creds_path, scope)
        client = gspread.authorize(creds)
        
        spreadsheet = client.open_by_url(sheet_url)
        worksheet = spreadsheet.get_worksheet(0) # Menggunakan sheet pertama
        
        worksheet.clear()
        
        df_str = df.astype(str)
        
        # Menulis header dan data yang sudah diubah ke string
        worksheet.update([df_str.columns.values.tolist()] + df_str.values.tolist())
        
        print(f"Data successfully loaded to Google Sheet: {sheet_url}")

    except gspread.exceptions.SpreadsheetNotFound:
        print("Error: Spreadsheet not found. Please check the URL.")
    except gspread.exceptions.APIError as e:
        print(f"Google API Error: {e}. This might be an issue with permissions or API enablement.")
    except Exception as e:
        print(f"An unexpected error occurred with Google Sheets: {e}")


def load_to_postgres(df: pd.DataFrame, db_uri: str, table_name: str):
    """Menyimpan DataFrame ke tabel PostgreSQL."""
    try:
        engine = create_engine(db_uri)
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        print(f"Data successfully loaded to PostgreSQL table '{table_name}'")
    except Exception as e:
        print(f"Error loading data to PostgreSQL: {e}")

