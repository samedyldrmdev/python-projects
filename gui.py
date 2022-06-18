# PART-1

from tkinter import *
from tkcalendar import DateEntry

master = Tk()

canvas = Canvas(master, height=450, width=750)
canvas.pack()
# pack, place, grid

# frame_ust = Frame(master, bg= "#add8e6", height=50,width=750)
# frame_ust.pack()
frame_ust = Frame(master, bg="#add8e6")
frame_ust.place(relx=0.10, rely=0.1, relwidth=0.8, relheight=0.1)

frame_alt_sol = Frame(master, bg="#add8e6")
frame_alt_sol.place(relx=0.10, rely=0.21, relwidth=0.245, relheight=0.55)

frame_alt_sag = Frame(master, bg="#add8e6")
frame_alt_sag.place(relx=0.35, rely=0.21, relwidth=0.55, relheight=0.55)

hatirlatma_tipi_etiket = Label(frame_ust, bg="#add8e6", text="Hatırlatma Tipi:", font="Verdana 12")
hatirlatma_tipi_etiket.pack(padx=10, pady=10, side=LEFT)

hatirlatma_tipi_opsiyon = StringVar(frame_ust)
hatirlatma_tipi_opsiyon.set("\t")

hatirlatma_tipi_acilir_menu = OptionMenu(
    frame_ust,
    hatirlatma_tipi_opsiyon,
    "Doğum Günü",
    "Alışveriş",
    "Ödeme")
hatirlatma_tipi_acilir_menu.pack(padx=10, pady=10, side=LEFT)

hatirlatma_tarih_secici = DateEntry(frame_ust, width=12, bg="orange", foreground="white")
hatirlatma_tarih_secici._top_cal.overrideredirect(False)
hatirlatma_tarih_secici.pack(padx=10, pady=10, side=RIGHT)

hatirlatma_tarihi_etiket = Label(frame_ust, bg="#add8e6", text="Hatırlatma Tarihi:", font="Verdana 12")
hatirlatma_tarihi_etiket.pack(padx=10, pady=10, side=RIGHT)

# PART-2

Label(frame_alt_sol, bg="#add8e6", text="Hatırlatma Yöntemi:", font="Verdana 10").pack(padx=10, pady=10, anchor=NW)

var = IntVar()
R1 = Radiobutton(frame_alt_sol, text="Sisteme Kaydet", variable=var, value=1, bg="#add8e6", font="Verdana 9")
R1.pack(padx=5, pady=10, anchor=NW)

R2 = Radiobutton(frame_alt_sol, text="E-posta Gönder", variable=var, value=2, bg="#add8e6", font="Verdana 9")
R2.pack(padx=5, pady=10, anchor=NW)

var1 = IntVar()
C1 = Checkbutton(frame_alt_sol, text= "Bir hafta önce", variable=var1, onvalue=1,offvalue=0,bg="#add8e6", font="Verdana 7")
C1.pack(padx=25, pady=3, anchor=NW)

var2 = IntVar()
C2 = Checkbutton(frame_alt_sol, text= "Bir gün önce", variable=var2, onvalue=1,offvalue=0,bg="#add8e6", font="Verdana 7")
C2.pack(padx=25, pady=3, anchor=NW)

var3 = IntVar()
C3 = Checkbutton(frame_alt_sol, text= "Aynı gün", variable=var3, onvalue=1,offvalue=0,bg="#add8e6", font="Verdana 7")
C3.pack(padx=25, pady=3, anchor=NW)

# PART-3
from tkinter import messagebox

def gonder():
    son_mesaj = ""
    try:
        if var.get():
            if var.get() == 1:
                son_mesaj += "Veriniz başarıyla sisteme kaydedilmiştir."
                tip = hatirlatma_tipi_opsiyon.get() if hatirlatma_tipi_opsiyon.get() == "" else "Genel"
                tarih = hatirlatma_tarih_secici.get()
                mesaj = text_alani.get("1.0", "end")
                messagebox.showinfo("Başarılı İşlem", son_mesaj)
                with open("C:/Users/user/Desktop/hatirlatmalar.txt","w") as dosya:
                    dosya.write(
                        "{} kategorisinde, {} tarihine ve {} notuyla hatırlatma ".format(tip,tarih,mesaj)
                    )
                    dosya.close()
            elif var.get() == 2:
                son_mesaj += "E-posta yoluyla hatırlatma size ulaşacaktır."
                messagebox.showinfo("Başarılı İşlem", son_mesaj)
        # if text_alani.get("1.0", "end") == "Mesajını buraya gir...":
        #     messagebox.showwarning("Yetersiz Bilgi!", "Lan boş!")
        else:
            messagebox.showwarning("Yetersiz Bilgi!", "Gerekli alanların doldurulduğundan emin olun!")
    except:
        messagebox.showerror("Başarısız İşlem!", "İşlem başarısız oldu!")
    finally:
        master.destroy()

Label(frame_alt_sag,bg="#add8e6", text="Hatırlatma Mesajı:", font="Verdana 10" ).pack(padx=10, pady=10, anchor=NW)

text_alani = Text(frame_alt_sag, height=9, width=45)
text_alani.tag_configure("style",foreground="#bfbfbf", font=("Verdana", 7, "bold"))
text_alani.pack()

karsilama_metni = "Mesajını buraya gir..."
text_alani.insert(END, karsilama_metni,"style")

gonder_butonu = Button(frame_alt_sag, text="Gönder Bakalım!", command=gonder)
gonder_butonu.pack(pady=10, anchor=S)


master.mainloop()
