# Bu programda Tkinter ve Sqlite3 kütüphaneleri ile yapılacak listesi kodladık.
# SQL ile arayüzden aldığımız verileri database'e gönderiyoruz.

# Tkinter ve SQL ile To Do List

import tkinter as tk
import sqlite3


def baglanti():
    conn = sqlite3.connect("yapilacaklar.db")
    if conn:
        print("Bağlantı başarılı.")
    else:
        print("Bağlantı kurulamadı!")
    return conn


def ekle():
    box.insert(tk.END, e.get())
    e.delete(0, tk.END)


def sil():
    if len(box.curselection()) > 0:
        index = box.curselection()[0]
        box.delete(index)


def kaydet():
    f = open("yapilacaklar.db", "w", encoding="utf-8")
    gorevler = box.get(0, tk.END)
    f.writelines("\n".join(gorevler))
    f.close()


def cikis():
    print("Listeden çıkış yapıldı.")
    window.after(20, window.destroy)


dbconnect = baglanti()

window = tk.Tk()
window.title("Yapılacaklar Listesi")

f = tk.Frame(window)
f.pack()

e = tk.Entry(window, width=40)
e.pack()

box = tk.Listbox(f, width=50, height=10)
box.pack(side=tk.LEFT)

scroll = tk.Scrollbar(f,command=box.yview)
scroll.pack(side=tk.RIGHT,fill=tk.Y)

bekle = tk.Button(window, text="Görev Ekle", width=40, command=ekle)
bekle.pack()

bsil = tk.Button(window, text="Görev Sil", width=40, command=sil)
bsil.pack()

bkaydet = tk.Button(window, text="Kaydet", width=40, command=kaydet)
bkaydet.pack()

bcikis = tk.Button(window, text="Çıkış Yap", width=40, command=cikis)
bcikis.pack()

window.mainloop()
dbconnect.close()
