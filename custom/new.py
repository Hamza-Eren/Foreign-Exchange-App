# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 22:50:04 2023

@author: HamzaEren
"""

from tkinter import Tk, Label, Frame
import requests
from bs4 import BeautifulSoup as bs


def GetData():
    URL = "https://www.doviz.com"
    r = requests.get(URL)
    soup = bs(r.content, "html.parser")
    data = soup.find_all("div", attrs={"class":"item"})
    
    usd_list = [data[1].text.replace("\n", " ").strip().split()[1], data[1].text.replace("\n", " ").strip().split()[2]]
    eur_list = [data[2].text.replace("\n", " ").strip().split()[1], data[2].text.replace("\n", " ").strip().split()[2]]
    gbp_list = [data[3].text.replace("\n", " ").strip().split()[1], data[3].text.replace("\n", " ").strip().split()[2]]
    gold_list = [data[0].text.replace("\n", " ").strip().split()[2], data[0].text.replace("\n", " ").strip().split()[3]]

    return (usd_list, eur_list, gbp_list, gold_list)

def Update():
    data = GetData()
    if data:
        usd_value.config(text=data[0][0])
        if "-" in data[0][1]:
            usd_frame.configure(bg="red")
            usd_label.configure(bg="red")
            usd_value.configure(bg="red")
            usd_percent.configure(bg="red")
        else:
            usd_frame.configure(bg="green")
            usd_label.configure(bg="green")
            usd_value.configure(bg="green")
            usd_percent.configure(bg="green")
        usd_percent.config(text=data[0][1])
        
        eur_value.config(text=data[1][0])
        if "-" in data[1][1]:
            eur_frame.configure(bg="red")
            eur_label.configure(bg="red")
            eur_value.configure(bg="red")
            eur_percent.configure(bg="red")
        else:
            eur_frame.configure(bg="green")
            eur_label.configure(bg="green")
            eur_value.configure(bg="green")
            eur_percent.configure(bg="green")
        eur_percent.config(text=data[1][1])
        
        gbp_value.config(text=data[2][0])
        if "-" in data[2][1]:
            gbp_frame.config(bg="red")
            gbp_label.config(bg="red")
            gbp_value.config(bg="red")
            gbp_percent.config(bg="red")
        else:
            gbp_frame.configure(bg="green")
            gbp_label.configure(bg="green")
            gbp_value.configure(bg="green")
            gbp_percent.configure(bg="green")
        gbp_percent.config(text=data[2][1])
        
        gold_value.config(text=data[3][0])
        if "-" in data[3][1]:
            gold_frame.configure(bg="red")
            gold_label.configure(bg="red")
            gold_value.configure(bg="red")
            gold_percent.configure(bg="red")
        else:
            gold_frame.configure(bg="green")
            gold_label.configure(bg="green")
            gold_value.configure(bg="green")
            gold_percent.configure(bg="green")
        gold_percent.config(text=data[3][1])
        
    app.after(1000, Update)


def Extend(master):
    master.place(width=228)
    
def Shorten(master):
    master.place(width=60)


app = Tk()
app.title("Currency")
app.configure(bg="white")
app.geometry("228x128+0+695")
app.resizable(0, 0)


#USD/TL
usd_frame = Frame(app)
usd_frame.bind("<Enter>", lambda x: Extend(usd_frame))
usd_frame.bind("<Leave>", lambda x: Shorten(usd_frame))
usd_frame.place(x=0, y=10, height=20, width=60)
usd_label = Label(usd_frame, text="USD/TL  :", font=("courier", "10"))
usd_label.place(x=0, y=0, height=20)
usd_value = Label(usd_frame, text="", font=("courier", "10"))
usd_value.place(x=80, y=0, height=20)
usd_percent = Label(usd_frame, text="", font=("courier", "10"))
usd_percent.place(x=175, y=0, height=20)


#EUR/TL
eur_frame = Frame(app)
eur_frame.bind("<Enter>", lambda x: Extend(eur_frame))
eur_frame.bind("<Leave>", lambda x: Shorten(eur_frame))
eur_frame.place(x=0, y=40, height=20, width=60)
eur_label = Label(eur_frame, text="EUR/TL  :", font=("courier", "10"))
eur_label.place(x=0, y=0, height=20)
eur_value = Label(eur_frame, text="", font=("courier", "10"))
eur_value.place(x=80, y=0, height=20)
eur_percent = Label(eur_frame, text="", font=("courier", "10"))
eur_percent.place(x=175, y=0, height=20)


#GBP/TL
gbp_frame = Frame(app)
gbp_frame.bind("<Enter>", lambda x: Extend(gbp_frame))
gbp_frame.bind("<Leave>", lambda x: Shorten(gbp_frame))
gbp_frame.place(x=0, y=70, height=20, width=60)
gbp_label = Label(gbp_frame, text="GBP/TL  :", font=("courier", "10"))
gbp_label.place(x=0, y=0, height=20)
gbp_value = Label(gbp_frame, text="", font=("courier", "10"))
gbp_value.place(x=80, y=0, height=20)
gbp_percent = Label(gbp_frame, text="", font=("courier", "10"))
gbp_percent.place(x=175, y=0, height=20)


#Gold (gram)
gold_frame = Frame(app)
gold_frame.bind("<Enter>", lambda x: Extend(gold_frame))
gold_frame.bind("<Leave>", lambda x: Shorten(gold_frame))
gold_frame.place(x=0, y=100, height=20, width=60)
gold_label = Label(gold_frame, text="Gold(g) :", font=("courier", "10"))
gold_label.place(x=0, y=0, height=20)
gold_value = Label(gold_frame, text="", font=("courier", "10"))
gold_value.place(x=80, y=0, height=20)
gold_percent = Label(gold_frame, text="", font=("courier", "10"))
gold_percent.place(x=175, y=0, height=20)

Update()
app.overrideredirect(True)
app.wm_attributes("-transparentcolor", "white")
app.attributes("-topmost", True)
app.mainloop()