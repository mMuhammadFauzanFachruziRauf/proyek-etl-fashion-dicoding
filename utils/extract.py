# utils/extract.py

import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import time

BASE_URL = "https://fashion-studio.dicoding.dev"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def scrape_page(page_number):
    """
    Fungsi untuk melakukan scraping pada satu halaman website dengan selektor yang benar.
    """
    products_on_page = []
    
    url = BASE_URL if page_number == 1 else f"{BASE_URL}/page{page_number}"
    
    try:
        response = requests.get(url, headers=HEADERS, timeout=15)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # --- SELEKTOR BARU BERDASARKAN HTML ASLI ---
        # Menargetkan setiap kartu produk dengan kelas 'collection-card'
        product_cards = soup.find_all('div', class_='collection-card')

        for card in product_cards:
            product_details = {}
            
            # Ekstrak Judul dari tag 'h3' dengan kelas 'product-title'
            title_element = card.find('h3', class_='product-title')
            product_details['title'] = title_element.get_text(strip=True) if title_element else 'Unknown Product'

            # Ekstrak Harga dari tag 'span' dengan kelas 'price'
            price_element = card.find('span', class_='price')
            product_details['price'] = price_element.get_text(strip=True) if price_element else 'Price Unavailable'

            # Ekstrak detail lain dari tag 'p'
            details_p = card.find_all('p')
            
            # Inisialisasi nilai default
            product_details['rating'] = 'Invalid Rating'
            product_details['colors'] = None
            product_details['size'] = None
            product_details['gender'] = None

            for p in details_p:
                text = p.get_text(strip=True)
                if 'Rating:' in text:
                    product_details['rating'] = text
                elif 'Colors' in text:
                    product_details['colors'] = text
                elif 'Size:' in text:
                    product_details['size'] = text
                elif 'Gender:' in text:
                    product_details['gender'] = text
            
            products_on_page.append(product_details)

    except requests.exceptions.RequestException as e:
        print(f"Error scraping page {page_number}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred on page {page_number}: {e}")
        
    return products_on_page


def extract_data():
    """
    Fungsi utama untuk mengorkestrasi proses scraping dari semua halaman.
    """
    all_products = []
    extraction_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    total_pages = 50
    
    print("Starting data extraction...")
    for page in range(1, total_pages + 1):
        print(f"Scraping page {page}/{total_pages}...")
        products = scrape_page(page)
        if products:
            for product in products:
                product['timestamp'] = extraction_timestamp
            all_products.extend(products)
        # Beri jeda 0.5 detik antar request untuk bersikap baik pada server
        time.sleep(0.5) 
    
    print(f"Extraction complete. Found {len(all_products)} products.")
    
    if not all_products:
        return pd.DataFrame()

    df = pd.DataFrame(all_products)
    return df
