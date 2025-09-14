import pandas as pd
import pytest
from unittest.mock import patch, MagicMock
from utils.load import load_to_csv, load_to_gdrive, load_to_postgres

@pytest.fixture
def clean_data_fixture():
    """Menyediakan DataFrame bersih sebagai sampel untuk pengujian load."""
    data = {
        'title': ['Test Product'],
        'price_idr': [250000],
        'rating': [4.5],
        'colors': [3],
        'size': ['M'],
        'gender': ['Unisex'],
        'timestamp': [pd.to_datetime('2025-09-09 15:00:00')]
    }
    return pd.DataFrame(data)

@patch('pandas.DataFrame.to_csv')
def test_load_to_csv(mock_to_csv, clean_data_fixture):
    """
    Menguji bahwa load_to_csv memanggil df.to_csv dengan argumen yang benar.
    """
    filename = "test.csv"
    load_to_csv(clean_data_fixture, filename)
    mock_to_csv.assert_called_once_with(filename, index=False)

@patch('utils.load.os.path.exists') # Tambahkan mock untuk os.path.exists
@patch('utils.load.gspread')
@patch('utils.load.ServiceAccountCredentials')
def test_load_to_gdrive(mock_creds, mock_gspread, mock_exists, clean_data_fixture):
    """
    Menguji bahwa load_to_gdrive berinteraksi dengan API gspread dengan benar.
    """
    # Atur agar os.path.exists selalu mengembalikan True selama tes ini
    mock_exists.return_value = True

    mock_client = MagicMock()
    mock_spreadsheet = MagicMock()
    mock_worksheet = MagicMock()

    mock_gspread.authorize.return_value = mock_client
    mock_client.open_by_url.return_value = mock_spreadsheet
    mock_spreadsheet.get_worksheet.return_value = mock_worksheet
    
    sheet_url = "dummy_url"
    creds_path = "dummy_creds.json"
    
    load_to_gdrive(clean_data_fixture, sheet_url, creds_path)
    
    mock_exists.assert_called_once_with(creds_path)
    mock_gspread.authorize.assert_called_once()
    mock_client.open_by_url.assert_called_once_with(sheet_url)
    
    mock_worksheet.clear.assert_called_once()
    mock_worksheet.update.assert_called_once()

@patch('utils.load.create_engine')
@patch('pandas.DataFrame.to_sql')
def test_load_to_postgres(mock_to_sql, mock_create_engine, clean_data_fixture):
    """
    Menguji bahwa load_to_postgres memanggil df.to_sql dengan argumen yang benar.
    """
    db_uri = "dummy_uri"
    table_name = "test_table"
    
    mock_engine = MagicMock()
    mock_create_engine.return_value = mock_engine
    
    load_to_postgres(clean_data_fixture, db_uri, table_name)
    
    mock_create_engine.assert_called_once_with(db_uri)
    mock_to_sql.assert_called_once_with(
        table_name,
        mock_engine,
        if_exists='replace',
        index=False
    )

