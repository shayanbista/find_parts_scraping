import os
import json
from bs4 import BeautifulSoup
import requests
import time
from scraper.find_parts_scraping import PartsDetailScraper

def main():

    url="https://www.findchips.com/detail/rr142-bb-nn/Carling-Technologies"

    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')
    scrape=PartsDetailScraper(soup)
    scrape.parse()
    print(scrape.parse()) 

if __name__ == "__main__":
    main()
























    




    # response = requests.get(url)
    # soup = BeautifulSoup(response.content, "html5lib")

    # scrape = PartsDetailScraper(soup)
    # print(scrape.parse())


if __name__ == "__main__":
    main()
