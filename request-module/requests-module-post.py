import requests as r
from PIL import Image
from io import BytesIO

# RADAR CHART

class Futbolcu():
    def __init__(self, isim, hiz, sut, pas, top_surus, defans, fizik):
        self.isim = isim
        self.hiz = hiz
        self.sut = sut
        self.pas = pas
        self.top_surus = top_surus
        self.defans = defans
        self.fizik = fizik

    def yetenek_hazirla(self):
        return ",".join(
            [str(self.hiz), str(self.sut), str(self.pas), str(self.top_surus), str(self.defans), str(self.fizik),str(self.hiz)])

    def yetenek_gorsellestir(self):
        grafik_url = "https://image-charts.com/chart"

        payload = {
            "chco": "3092de",
            "chd": "t:" + self.yetenek_hazirla(),
            "chl": "hiz|sut|pas|top surus|defans|fizik",
            "chdl": self.isim,
            "chs": "900x900",
            "cht": "r",
            "chtt": "Futbolcu Özellikleri",
            "chxl": "0:|0|20|40|60|80|100",
            "chxt": "x",
            "chxr": "0,0.0,100.0",
            "chm": "B,AAAAAABB,0,0,0",
        }
        response = r.post(grafik_url, data=payload)
        image = Image.open(BytesIO(response.content))
        image.show()

    def yetenek_kiyaslama_goster(self, hedef_futbolcu):
        self.hedef_futbolcu = hedef_futbolcu

        grafik_url = "https://image-charts.com/chart"

        payload = {
            "chco": "3092de,027182",
            "chd": "t:" + self.yetenek_hazirla() + "|" + hedef_futbolcu.yetenek_hazirla(),
            "chl": "hiz|sut|pas|top surus|defans|fizik",
            "chdl": self.isim + "|" + hedef_futbolcu.isim,
            "chs": "900x900",
            "cht": "r",
            "chtt": "Futbolcu Özellikleri",
            "chxl": "0:|0|20|40|60|80|100",
            "chxt": "x",
            "chxr": "0,0.0,100.0",
            "chm": "B,AAAAAABB,0,0,0|B,0073CFBB,1,0,0",
        }
        response = r.post(grafik_url, data=payload)
        image = Image.open(BytesIO(response.content))
        image.show()


messi = Futbolcu("Messi", 85, 92, 91, 95, 34, 65)
ronaldo = Futbolcu("Ronaldo", 87, 93, 82, 88, 34, 75)

ronaldo.yetenek_kiyaslama_goster(messi)
