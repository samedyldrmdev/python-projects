import requests

from collections import Counter
class SucRaporu():
    def __init__(self, bolge, tarih, suc_tipi="all-crime"):
        self.bolge = bolge
        self.tarih = tarih
        self.suc_tipi = suc_tipi
        self.suclar = self.suclari_bul()

    def suclari_bul(self):
        suc_url = "https://data.police.uk/api/crimes-no-location"

        payload = {
            "category": self.suc_tipi,
            "force": self.bolge,
            "date": self.tarih}
        response = requests.get(suc_url, params=payload)

        if response.status_code == 200:
            return response.json()
        else:
            return None

    def suclari_raporla(self):
        suclar_listesi = []
        if self.suclar is not None:
            for suc in self.suclar:
                suclar_listesi.append(suc['category'])
            return Counter(suclar_listesi)


sr = SucRaporu("norfolk", "2022-02", "violent-crime") #suç kısmı default bir değer yani "all-crime"

print(sr.suclari_raporla())
