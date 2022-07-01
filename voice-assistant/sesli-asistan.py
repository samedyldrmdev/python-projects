from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os
import time
from datetime import datetime
import random
from random import choice
import locale
import webbrowser
from time import sleep
import requests
from bs4 import BeautifulSoup
import re

locale.setlocale(locale.LC_ALL, '')
r = sr.Recognizer()

# speech_recognition ile dinleme ve konuşma
def record(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio, language="tr-TR")
        except sr.UnknownValueError:
            speak("Anlayamadım!")
        except sr.RequestError:
            speak("Sistem çalışmıyor.")
        return voice


# BeautifulSoup ile opensea satış ve taban fiyatı kazıma
header = {"user-agent": "Mozilla/5.0"}
url = "https://opensea.io/collection/wearemetahuman"
content = requests.get(url, headers=header).content
soup = BeautifulSoup(content, "html.parser")
titles = soup.find_all("span", {"class": "sc-1xf18x6-0"})
satis = str(titles)
eth = re.findall("(</div></button></div>(\S+)</div>)", satis)
satisimiz = eth[1][1]
floorprice = eth[0][1]

# BeautifulSoup ile hava durumu kazıma
def Havadurumu(il):
    header = {"user-agent": "Mozilla/5.0"}
    url = "https://www.ntvhava.com/{}-hava-durumu".format(il)
    content = requests.get(url, headers=header).content
    soup = BeautifulSoup(content, "html.parser")
    havadurumu = soup.find_all("div", {"class": "daily-report-tab-content-pane-item-text"})
    havadurumu = str(havadurumu).split(">")[1].split("<")[0]
    derece = soup.find_all("div", {"class": "daily-report-tab-content-pane-item-box-bottom-degree-big"})
    derece = str(derece).split(">")[1].split("<")[0]
    return havadurumu, derece

# Tepkiler
def response(voice):
    myname = ""
    if "selam" in voice or "merhaba" in voice:
        speak("Sana da merhaba patron.")
    if "hava" in voice:
        speak("Hangi şehirdesin patron?")
        il = record()
        il.lower()
        hava_durumu_tepki = ""
        if "güneş" in Havadurumu(il)[0].lower():
            hava_durumu_tepki = "Bugün hava güzel. İyi gezmeler patron!"
        if "bulut" in Havadurumu(il)[0].lower():
            hava_durumu_tepki = "Bulutları seyret patron!"
        if "sağanak" in Havadurumu(il)[0].lower():
            hava_durumu_tepki = "Yağmur çok fena! Şemsiyeni almayı unutma patron!"
        elif "yağmur" in Havadurumu(il)[0].lower():
            hava_durumu_tepki = "Şemsiyeni almayı unutma patron!"

        speak("{}'da hava bugün {} derece, {}!{}"
              .format(il.capitalize(), Havadurumu(il)[1], Havadurumu(il)[0], hava_durumu_tepki))
    if "şaka" in voice or "espri" in voice or "fıkra" in voice:
        espriler = open("espriler.txt", "r", encoding="utf8")
        espriler = espriler.readlines()
        speak(random.choice(espriler))
    if "adın ne" in voice:
        speak("Benim adım Sesli Asistan!")
    if "güzel" in voice:
        speak("Başka yapmamı istediğin bir şey varsa lütfen söyle.")
    if "yapıyorsun" in voice or "yaptın" in voice:
        speak("Çalışıyoz! Ne yapalım!")
    if "ne haber" in voice or "nasılsın" in voice:
        speak("İyi be nolsun.")
    if "metahuman" in voice or "satış" in voice or "opensea" in voice:
        speak("Hemen kontrol ediyorum patron! {} ethereum kadar satış yapılmış. İyi para!".format(satisimiz))
    if "taban" in voice:
        speak("Taban fiyatımız şu an {} ethereum patron!".format(floorprice))
    if "teşekkür" in voice:
        speak("Ne demek, her zaman patron!")
    if "gün" in voice:
        today = time.strftime("%A")
        speak("Bugün günlerden {}".format(today))
    if "saat" in voice:
        selection = ["Hemen bakıyorum", "Saat şu an", "Hmm. Dur bakalım. Saat:"]
        saat = datetime.now().strftime("%H:%M")
        selection = random.choice(selection)
        speak("{}{}".format(selection, saat))
    if "hangi ay" in voice or "aylar" in voice:
        ay = time.strftime("%B")
        speak("{} ayındayız patron.".format(ay))
    if "google'da ara" in voice:
        speak("Ne arayayım?")
        search = record()
        url = "https://www.google.com/search?q={}".format(search)
        webbrowser.get().open(url)
        speak("{} için Google'da bulabildiklerimi listeliyorum patron!".format(search))
    if "twitter" in voice:
        webbrowser.get().open("https://www.twitter.com/wearemetahuman")
        speak("Açtım bile patron!")
    if "görüşürüz" in voice:
        speak("Görüşürüz patron! Allah'a emanet ol.")
        exit()
    if "uyku" in voice:
        speak("Hadi biraz dinlen patron!")
        exit()
    if "uyu " in voice:
        speak("Tamam bi' 15 saniye kestireceğim!")
        sleep(15)


# Text to Speech
def speak(string):
    # dil = ""
    tts = gTTS(text=string, lang="tr", slow=False)
    file = "answer.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)

speak("Merhaba patron!")

while True:
    voice = record()
    if voice != '':
        voice = voice.lower()
        print("Patron:", voice.capitalize())
        response(voice)
