import pandas as pd
import pytest
from utils.transform import transform_data

@pytest.fixture
def raw_data_fixture():
    """
    Menyediakan data mentah sebagai "fixture" atau sampel untuk digunakan dalam tes.
    """
    data = {
        'title': ['Valid T-Shirt', 'Unknown Product', 'Valid T-Shirt'],
        'price': ['$15.50', '$100.00', '$15.50'],
        'rating': ['Rating: ⭐ 4.2 / 5', 'Rating: ⭐ Invalid Rating / 5', 'Rating: ⭐ 4.2 / 5'],
        'colors': ['3 Colors', '5 Colors', '3 Colors'],
        'size': ['Size: L', 'Size: M', 'Size: L'],
        'gender': ['Gender: Women', 'Gender: Men', 'Gender: Women'],
        'timestamp': ['2025-09-09 14:00:00', '2025-09-09 14:00:00', '2025-09-09 14:00:00']
    }
    return pd.DataFrame(data)

def test_transform_data(raw_data_fixture):
    """
    Menguji fungsi transform_data dengan logika konversi ke Rupiah dan timestamp.
    """
    transformed_df = transform_data(raw_data_fixture)

    # 1. Asersi Kualitas Data: Memastikan data tidak valid dan duplikat dihapus
    assert len(transformed_df) == 1, "Data tidak valid atau duplikat tidak terhapus."

    # 2. Asersi Nama Kolom: Memastikan nama kolom sudah benar
    expected_columns = ['title', 'price_idr', 'rating', 'colors', 'size', 'gender', 'timestamp']
    assert list(transformed_df.columns) == expected_columns, "Nama kolom tidak sesuai."

    # 3. Asersi Isi Data: Memeriksa nilai-nilai setelah transformasi
    first_row = transformed_df.iloc[0]
    assert first_row['title'] == 'Valid T-Shirt'
    # Harga harus dikonversi ke Rupiah: 15.50 * 16000 = 248000
    assert first_row['price_idr'] == 248000
    assert first_row['rating'] == 4.2
    assert first_row['colors'] == 3
    assert first_row['size'] == 'L'
    assert first_row['gender'] == 'Women'

    # 4. Asersi Tipe Data: Memastikan semua kolom memiliki tipe data yang benar
    assert str(transformed_df.dtypes['title']) == 'object'
    assert str(transformed_df.dtypes['price_idr']) == 'int64'
    assert str(transformed_df.dtypes['rating']) == 'float64'
    assert str(transformed_df.dtypes['colors']) == 'int64'
    assert str(transformed_df.dtypes['size']) == 'object'
    assert str(transformed_df.dtypes['gender']) == 'object'
    assert str(transformed_df.dtypes['timestamp']) == 'datetime64[ns]'

