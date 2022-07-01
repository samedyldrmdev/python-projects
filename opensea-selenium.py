from selenium import webdriver
from time import sleep


browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://opensea.io/activity?search[eventTypes][0]=AUCTION_SUCCESSFUL&search[chains][0]=MATIC&search[chains][1]=ETHEREUM")
sleep(5)
selector = '#main > div > div > div > div.fresnel-container.fresnel-greaterThanOrEqual-xl.fill-remaining-height > div.sc-1xf18x6-0.sc-1twd32i-0.bdMwSd.kKpYwv > div.sc-1xf18x6-0.sc-1twd32i-0.sc-1wwz3hp-0.hRjaBd.kKpYwv.kuGBEl > div.sc-1xf18x6-0.cXZCEh > div > div:nth-child(2) > div:nth-child(19) > button > div > div:nth-child(6) > div > a'
button = browser.find_element("css selector", selector)
browser.execute_script("arguments[0].click();", button)
sleep(10)
