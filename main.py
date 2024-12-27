import os
import json
from bs4 import BeautifulSoup
import requests
import time
from scraper.find_parts_scraping import PartsDetailScraper
from selenium import webdriver
from selenium.webdriver.common.by import By

def main():

    url="https://www.findchips.com/detail/rr142-bb-nn/Carling-Technologies"
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)  
    html = driver.page_source
    # response = requests.get(url)

    soup = BeautifulSoup(html, 'html.parser')
    scrape=PartsDetailScraper(soup)
    scrape.parse()
    print(scrape.parse()) 

if __name__ == "__main__":
    main()
