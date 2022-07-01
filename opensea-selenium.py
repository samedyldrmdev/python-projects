from asyncio import selector_events
from selenium import webdriver
from time import sleep
import requests
from bs4 import BeautifulSoup
import re
import time

browser = webdriver.Chrome()
browser.maximize_window()
url = "https://opensea.io/activity?search[eventTypes][0]=AUCTION_SUCCESSFUL&search[chains][0]=MATIC&search[chains][1]=ETHEREUM"
browser.get(url)

def Browser():

    sleep(5)
    selector = 'div.AccountLink--ellipsis-overflow > a'
    # button = browser.find_element("css selector", selector)
    username = browser.find_element("css selector", selector).text

    def kullanici():
        header = {"user-agent": "Mozilla/5.0"}
        url = "https://opensea.io/" + username
        content = requests.get(url, headers=header).content
        soup = BeautifulSoup(content, "html.parser")
        titles = soup.find_all("a", {"class": "sc-1pie21o-0 elyzfO"})
        titles = str(titles)
        twitter = re.findall("(https://twitter\.com/\S+)", titles)
        instagram = re.findall("(https://instagram\.com/\S+)", titles)

        print(username)
        if twitter != []:
            print(twitter)
        if instagram != []:
            print(instagram)
        else:
            print("Social media account not found!")
    return kullanici()

while True:
    Browser()
    sleep(10)
