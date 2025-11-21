"""
Script untuk Scraping Data Kos dari Website
============================================

Script ini adalah contoh template untuk scraping data kos-kosan
dari website seperti Mamikos.com atau platform lainnya.

Author: Data Science Portfolio
Date: November 2024

DISCLAIMER:
- Pastikan mematuhi robots.txt dan terms of service website
- Gunakan rate limiting untuk menghindari overload server
- Data dalam project ini adalah synthetic/generated data
"""

import pandas as pd
import time
from datetime import datetime

# Note: Import libraries untuk scraping
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from bs4 import BeautifulSoup
# import requests


class KosScraper:
    """
    Class untuk scraping data kos-kosan
    """
    
    def __init__(self, base_url, max_pages=10):
        """
        Initialize scraper
        
        Parameters:
        -----------
        base_url : str
            URL dasar website yang akan di-scrape
        max_pages : int
            Maksimum jumlah halaman yang akan di-scrape
        """
        self.base_url = base_url
        self.max_pages = max_pages
        self.data = []
        
    def scrape_listing(self, url):
        """
        Scrape single listing
        
        Parameters:
        -----------
        url : str
            URL listing kos
            
        Returns:
        --------
        dict
            Data kos yang di-scrape
        """
        # Template struktur data
        kos_data = {
            'nama_kos': '',
            'kota': '',
            'wilayah': '',
            'harga_per_bulan': 0,
            'tipe_kos': '',
            'ukuran_kamar': 0,
            'ac': 0,
            'kamar_mandi_dalam': 0,
            'wifi': 0,
            'listrik_include': 0,
            'parkir': 0,
            'dapur': 0,
            'laundry': 0,
            'security_24jam': 0,
            'jarak_ke_kampus_km': 0,
            'kampus_terdekat': '',
            'jarak_ke_transportasi_km': 0,
            'rating': 0,
            'jumlah_kamar': 0,
            'jumlah_review': 0
        }
        
        # TODO: Implement actual scraping logic
        # Example:
        # response = requests.get(url)
        # soup = BeautifulSoup(response.content, 'html.parser')
        # kos_data['nama_kos'] = soup.find('h1', class_='title').text
        # ... dst
        
        return kos_data
    
    def scrape_search_results(self, search_url):
        """
        Scrape hasil pencarian (multiple listings)
        
        Parameters:
        -----------
        search_url : str
            URL halaman pencarian
            
        Returns:
        --------
        list
            List of listing URLs
        """
        listing_urls = []
        
        # TODO: Implement logic untuk extract URLs dari search results
        # Example:
        # response = requests.get(search_url)
        # soup = BeautifulSoup(response.content, 'html.parser')
        # listings = soup.find_all('div', class_='listing-card')
        # for listing in listings:
        #     url = listing.find('a')['href']
        #     listing_urls.append(url)
        
        return listing_urls
    
    def scrape_all(self, search_query='Jakarta'):
        """
        Scrape semua data berdasarkan query
        
        Parameters:
        -----------
        search_query : str
            Query pencarian (lokasi, dll)
        """
        print(f"Memulai scraping untuk: {search_query}")
        print("=" * 80)
        
        for page in range(1, self.max_pages + 1):
            print(f"\nScraping halaman {page}...")
            
            # Construct search URL dengan pagination
            search_url = f"{self.base_url}/search?location={search_query}&page={page}"
            
            # Get listing URLs
            listing_urls = self.scrape_search_results(search_url)
            
            # Scrape each listing
            for idx, url in enumerate(listing_urls, 1):
                print(f"  Scraping listing {idx}/{len(listing_urls)}")
                
                try:
                    kos_data = self.scrape_listing(url)
                    self.data.append(kos_data)
                    
                    # Rate limiting - jangan overload server
                    time.sleep(1)  # Delay 1 detik antar request
                    
                except Exception as e:
                    print(f"    Error: {e}")
                    continue
        
        print(f"\nSelesai! Total data yang berhasil di-scrape: {len(self.data)}")
        
    def save_to_csv(self, filename='data_kos_scraped.csv'):
        """
        Save data ke CSV file
        
        Parameters:
        -----------
        filename : str
            Nama file output
        """
        if not self.data:
            print("Tidak ada data untuk disimpan!")
            return
        
        df = pd.DataFrame(self.data)
        df.to_csv(filename, index=False)
        print(f"Data berhasil disimpan ke: {filename}")
        
    def get_dataframe(self):
        """
        Get data sebagai pandas DataFrame
        
        Returns:
        --------
        pd.DataFrame
            DataFrame containing scraped data
        """
        return pd.DataFrame(self.data)


def example_usage():
    """
    Contoh penggunaan scraper
    """
    print("=" * 80)
    print("CONTOH PENGGUNAAN KOS SCRAPER")
    print("=" * 80)
    print("\nDISCLAIMER:")
    print("Script ini adalah TEMPLATE/CONTOH untuk scraping.")
    print("Untuk implementasi real:")
    print("1. Install dependencies: selenium, beautifulsoup4, requests")
    print("2. Pahami struktur HTML website target")
    print("3. Respect robots.txt dan rate limiting")
    print("4. Gunakan dengan bertanggung jawab")
    print("\n" + "=" * 80)
    
    # Example initialization
    scraper = KosScraper(
        base_url="https://example-kos-website.com",
        max_pages=5
    )
    
    # Note: Ini hanya contoh, tidak akan berjalan tanpa implementasi actual scraping
    # scraper.scrape_all(search_query="Jakarta Selatan")
    # scraper.save_to_csv('data_kos_jakarta.csv')
    
    print("\nUntuk project ini, data yang digunakan adalah synthetic data")
    print("yang di-generate untuk simulasi analisis.")


if __name__ == "__main__":
    example_usage()
    
    print("\n" + "=" * 80)
    print("TIPS SCRAPING:")
    print("=" * 80)
    print("1. Selalu check robots.txt website")
    print("2. Gunakan User-Agent headers yang proper")
    print("3. Implement rate limiting (delay antar request)")
    print("4. Handle errors dengan try-except")
    print("5. Save data incremental untuk avoid data loss")
    print("6. Validate data setelah scraping")
    print("=" * 80)
