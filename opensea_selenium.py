# ABOUT
# I have an account where I produce and sell nft. And I needed to reach people for the nft sale. 
# I was doing this by reaching social media accounts. This is a really time consuming process. 
# I have developed a project that saves social media accounts in .txt file by coding with Python. 
# Made my job a lot easier. The fact that the program continues to run as I write these lines excites me for my software future!

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

twitter_accounts = []
instagram_accounts = []

def Browser():
    sleep(5)
    selector = 'div > button > div > div:nth-child(6) > div'
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

        print("username:", username)
        if twitter != []:
            print(twitter)
            if twitter not in twitter_accounts:
                twitter_accounts.append(twitter)
                with open("twitterhesaplari.txt", "a+") as dosya:
                    dosya_icerigi = dosya.readlines()
                    for t in twitter_accounts:
                        if t not in dosya_icerigi:
                            dosya.write(str(t)+"\n")
        if instagram != []:
            print(instagram)
            if instagram not in instagram_accounts:
                instagram_accounts.append(instagram)
                with open("instagramhesaplari.txt", "a+") as dosya:
                    dosya_icerigi = dosya.readlines()
                    for i in instagram_accounts:
                        if i not in dosya_icerigi:
                            dosya.write(str(i)+"\n")
        else:
            print("Social media account not found!")

    return kullanici()

while True:
    try:
        Browser()
        sleep(10)
    except Exception as e:
        print(e)
        browser = webdriver.Chrome()
        browser.maximize_window()
        url = "https://opensea.io/activity?search[eventTypes][0]=AUCTION_SUCCESSFUL&search[chains][0]=MATIC&search[chains][1]=ETHEREUM"
        browser.get(url)
        twitter_accounts = []
        instagram_accounts = []
    finally:
        pass
