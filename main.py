# import os
# import json
# from bs4 import BeautifulSoup
# import requests
# import time
from scraper.find_parts_scraping import PartsDetailScraper
# import html5lib


# def main():

#     api_key="354fd1c76a664404bb4ac2f912f4cda2bb8ccacc68a"
#     url = "https://api.scrape.do/scrape" 

#     params = {
#     "url": "https://www.findchips.com/detail/mmbt3904lt1g/ON-Semiconductor",  
#     "api_key": api_key, 
#     }

#     response = requests.get(url, params=params)


#     soup=BeautifulSoup(response.content,"html.parser")

#     with open("1.html", "w") as file:
#         file.write(soup.prettify())



from bs4 import BeautifulSoup
import requests
import urllib.parse

def main():
    
    # token = "354fd1c76a664404bb4ac2f912f4cda2bb8ccacc68a"  
    # targetUrl = urllib.parse.quote("https://www.findchips.com/detail/rr142-bb-nn/Carling-Technologies")
    # url = "http://api.scrape.do?token={}&url={}".format(token, targetUrl)

    # Sending request to the Scrape.do API
    # response = requests.request("GET", url)


    with open("2.html", "r") as file:
        soup = BeautifulSoup(file, 'html5lib')
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
