# //*[@id="main"]/div/div/div/div[2]/div[3]/div[3]/div[2]/div/div[2]/div[14]/button/div/div[6]/div/a/span

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

# <a class="sc-1pie21o-0 hmswhC sc-1xf18x6-0 eUySLC AccountLink--ellipsis-overflow"
# font-weight="400" href="/0x3C5D89E4Fd55980b1b9486A1d6BBe8DA901c937D">
# <span>3C5D89</span></a>

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://opensea.io/activity?search[eventTypes][0]=AUCTION_SUCCESSFUL&search[chains][0]=MATIC&search[chains][1]=ETHEREUM")
sleep(5)
selector = '#main > div > div > div > div.fresnel-container.fresnel-greaterThanOrEqual-xl.fill-remaining-height > div.sc-1xf18x6-0.sc-1twd32i-0.bdMwSd.kKpYwv > div.sc-1xf18x6-0.sc-1twd32i-0.sc-1wwz3hp-0.hRjaBd.kKpYwv.kuGBEl > div.sc-1xf18x6-0.cXZCEh > div > div:nth-child(2) > div:nth-child(19) > button > div > div:nth-child(6) > div > a'
button = browser.find_element("css selector", selector)
browser.execute_script("arguments[0].click();", button)
# button.execute_script("arguments[0].click();", button)
# button.click()
sleep(10)




