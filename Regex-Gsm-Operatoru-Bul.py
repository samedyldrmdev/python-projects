# Regex Module'u kullanarak basit bir Gsm Operatoru Bulma Fonksiyonu
# GSM OPERATORLERİ
# 54... : Vodafone
# 501,505,506 : AVEA
# 53... : Turkcell
import re

def gsm_operator_bul():
    patern = r"(\d{3})-\d{7}"
    eslesme = re.search(patern,tel_no)
    if eslesme:
        gsm_kod = eslesme.groups()[0]
        print(gsm_kod)
        if gsm_kod.startswith("54"):
            return "Vodafone'a aittir."
        elif gsm_kod.startswith("501") or gsm_kod.startswith("505") or gsm_kod.startswith("506"):
            return "Avea'ya aittir."
        elif gsm_kod.startswith("53"):
            return "Turkcell'e aittir."
        else:
            return "Şebeke bulunamadı."
    else:
        return "Patern bulunamadı."

tel_no = input("Telefon numaranızı XXXX-XXXXXXX şeklinde araya çizgi koyarak giriniz: ")

print(gsm_operator_bul())
