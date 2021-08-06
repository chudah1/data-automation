
import requests
from bs4 import BeautifulSoup

class Scrape:
    """This class is responsible for communicating with the realtor website to find prices of houses, their addresses and the link to buy them"""
    def __init__(self):
        self.response = requests.get("https://www.realtor.com/apartments/San-Francisco_CA/beds-1-1/type-apartments/price-na-3000", headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0",
            "Accept-Language": "fr-CH, fr;q=0.9, en;q=0.8, de;q=0.7, *;q=0.5"})
        
    def make_soup(self):
        data = self.response.text
        self.soup = BeautifulSoup(data, "html.parser")

    def find_address(self):
        addresses = self.soup.find_all("div", class_="jsx-17763392 address ellipsis")
        return addresses

    
    def find_prices(self):
        prices = self.soup.find_all("div", class_="price")
        return prices

    
    def link_address(self):
        links = self.soup.find_all("div", class_="jsx-17763392 photo-wrap")
        return links
    
        






