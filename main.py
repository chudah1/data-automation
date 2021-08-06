from scrape import *
from form import *
import time

# Making an object from the scrape module
scraper = Scrape()
scraper.make_soup()
address = scraper.find_address()
address_list = [i.text for i in address]
prices = scraper.find_prices()
prices_list = [price.span.text.split("+")[0] for price in prices]
links = scraper.link_address()
links_list = [link.a["href"] for link in links]
f_links = [f"https://www.realtor.com {link}" for link in links_list]

# making an object from the form module

e = Bot()
e.get_form()
for n in range(len(address_list)):
    time.sleep(3)
    e.fill_q1().send_keys(address_list[n])
    e.fill_q2().send_keys(prices_list[n])
    e.fill_q3().send_keys(links_list[n])
    e.submit().click()
    time.sleep(3)
    e.find_by_link().click()
