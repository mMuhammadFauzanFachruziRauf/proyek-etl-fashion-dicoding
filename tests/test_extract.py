import pandas as pd
from unittest.mock import patch, Mock
from utils.extract import scrape_page, extract_data

# Contoh potongan HTML palsu untuk digunakan dalam tes.
# Ini meniru struktur HTML dari website target.
FAKE_HTML_PAGE_1 = """
<html>
<body>
    <div class="collection-grid">
        <div class="collection-card">
            <h3 class="product-title">Test T-Shirt</h3>
            <div class="price-container"><span class="price">$50.00</span></div>
            <p>Rating: ⭐ 4.5 / 5</p>
            <p>3 Colors</p>
            <p>Size: M</p>
            <p>Gender: Unisex</p>
        </div>
        <div class="collection-card">
            <h3 class="product-title">Test Hoodie</h3>
            <div class="price-container"><span class="price">$120.50</span></div>
            <p>Rating: ⭐ 4.8 / 5</p>
            <p>2 Colors</p>
            <p>Size: L</p>
            <p>Gender: Men</p>
        </div>
    </div>
</body>
</html>
"""

# HTML palsu untuk halaman kedua, untuk menguji looping
FAKE_HTML_PAGE_2 = """
<html>
<body>
    <div class="collection-grid">
        <div class="collection-card">
            <h3 class="product-title">Test Pants</h3>
            <div class="price-container"><span class="price">$85.00</span></div>
            <p>Rating: ⭐ 4.2 / 5</p>
            <p>4 Colors</p>
            <p>Size: S</p>
            <p>Gender: Women</p>
        </div>
    </div>
</body>
</html>
"""

# Menguji fungsi scrape_page
# @patch memberitahu pytest untuk mengganti 'requests.get' di dalam modul 'utils.extract'
# dengan objek mock selama tes ini berjalan.
@patch('utils.extract.requests.get')
def test_scrape_page_success(mock_get):
    """Menguji bahwa scrape_page berhasil mem-parsing HTML dan mengembalikan data yang benar."""
    # Siapkan mock: saat requests.get dipanggil, kembalikan response palsu
    mock_response = Mock()
    mock_response.text = FAKE_HTML_PAGE_1
    mock_response.raise_for_status.return_value = None  # Pura-pura tidak ada HTTP error
    mock_get.return_value = mock_response

    # Panggil fungsi yang ingin diuji
    products = scrape_page(1)

    # Lakukan asersi (penegasan) untuk memeriksa hasilnya
    assert len(products) == 2
    assert products[0]['title'] == 'Test T-Shirt'
    assert products[0]['price'] == '$50.00'
    assert products[0]['rating'] == 'Rating: ⭐ 4.5 / 5'
    assert products[1]['title'] == 'Test Hoodie'
    assert products[1]['gender'] == 'Gender: Men'

# Menguji fungsi extract_data
@patch('utils.extract.scrape_page') # Kali ini kita mock fungsi kita sendiri, scrape_page
def test_extract_data(mock_scrape_page):
    """Menguji bahwa extract_data mengoordinasikan scraping dengan benar."""
    # Atur agar panggilan pertama ke scrape_page mengembalikan 2 produk,
    # panggilan kedua mengembalikan 1 produk, dan sisanya kosong.
    mock_scrape_page.side_effect = [
        [{'title': 'Product A'}, {'title': 'Product B'}], # Hasil untuk halaman 1
        [{'title': 'Product C'}],                          # Hasil untuk halaman 2
    ] + [[]] * 48                                       # Halaman sisanya kosong

    # Panggil fungsi utama
    df = extract_data()

    # Periksa hasilnya
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 3
    assert 'timestamp' in df.columns
    assert list(df['title']) == ['Product A', 'Product B', 'Product C']
