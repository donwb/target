from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from sys import platform

import urllib, os, urllib.request
import time

print(platform)

if platform == "linux" or platform =="linux2":
    print('Using Linux driver...')
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument("window-size=1024,768")
    chrome_options.add_argument("--no-sandbox")

    #driver = webdriver.Chrome(chrome_options=chrome_options)
else:
    print('Using MacOS driver...')
    driver = webdriver.Safari()

driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()

print('here')
