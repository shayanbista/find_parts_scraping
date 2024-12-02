import os
import json
from bs4 import BeautifulSoup
import requests
import time
from scraper.find_parts_scraping import PartsDetailScraper


def main():
    url = "https://www.findchips.com/detail/mpc8548vjavhd/NXP-Semiconductors"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    scrape = PartsDetailScraper(soup)
    scrape.parse()


if __name__ == "__main__":
    main()
