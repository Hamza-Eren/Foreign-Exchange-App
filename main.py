# -*- coding: utf-8 -*-
"""
@author: HamzaEren
"""

from tkinter import Tk, Label, Frame
import requests
from bs4 import BeautifulSoup as bs


def GetData():
    URL = "https://www.doviz.com"
    r = requests.get(URL)
    soup = bs(r.content, "lxml")
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


app = Tk()
app.iconbitmap(r"images/icon.ico")
app.title("Currency")
#app.configure(bg="black")
app.geometry("248x128+0+0")
app.resizable(0, 0)


#USD/TL
usd_frame = Frame(app)
usd_frame.place(x=0, y=10, height=20, width=248)
usd_label = Label(usd_frame, text="USD/TL  :", font=("courier", "10"))
usd_label.place(x=20, y=0, height=20)
usd_value = Label(usd_frame, text="", font=("courier", "10"))
usd_value.place(x=100, y=0, height=20)
usd_percent = Label(usd_frame, text="", font=("courier", "10"))
usd_percent.place(x=180, y=0, height=20)


#EUR/TL
eur_frame = Frame(app)
eur_frame.place(x=0, y=40, height=20, width=248)
eur_label = Label(eur_frame, text="EUR/TL  :", font=("courier", "10"))
eur_label.place(x=20, y=0, height=20)
eur_value = Label(eur_frame, text="", font=("courier", "10"))
eur_value.place(x=100, y=0, height=20)
eur_percent = Label(eur_frame, text="", font=("courier", "10"))
eur_percent.place(x=180, y=0, height=20)


#GBP/TL
gbp_frame = Frame(app)
gbp_frame.place(x=0, y=70, height=20, width=248)
gbp_label = Label(gbp_frame, text="GBP/TL  :", font=("courier", "10"))
gbp_label.place(x=20, y=0, height=20)
gbp_value = Label(gbp_frame, text="", font=("courier", "10"))
gbp_value.place(x=100, y=0, height=20)
gbp_percent = Label(gbp_frame, text="", font=("courier", "10"))
gbp_percent.place(x=180, y=0, height=20)


#Gold (gram)
gold_frame = Frame(app)
gold_frame.place(x=0, y=100, height=20, width=248)
gold_label = Label(gold_frame, text="Gold(g) :", font=("courier", "10"))
gold_label.place(x=20, y=0, height=20)
gold_value = Label(gold_frame, text="", font=("courier", "10"))
gold_value.place(x=100, y=0, height=20)
gold_percent = Label(gold_frame, text="", font=("courier", "10"))
gold_percent.place(x=180, y=0, height=20)

Update()
#app.overrideredirect(1)
#app.wm_attributes("-transparentcolor", "black")
app.mainloop()
