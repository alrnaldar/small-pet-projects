import requests
from bs4 import BeautifulSoup
import time
from tkinter import *
from tkinter import messagebox
import pyperclip
import webbrowser
tk = Tk()
tk.title("новости")
tk.geometry("600x300")

page = requests.get("https://ria.ru/world/")
soup = BeautifulSoup(page.content, 'html.parser')
data = soup.find_all("div", class_="list-item__date")
news_titles = soup.find_all('a', class_='list-item__title color-font-hover-only', href_="")
fourth = []
hrefs = []
datas = []
lbl = Label(tk, text="")
lbl.place(x=0,y=0)

for dat in data:
    first = dat.text
    datas.append(first)
for title in news_titles:
    href = title.get("href")
    hrefs.append(href)
    second = title.text
    third = f"{first} {second}"
    fourth.append(second)
count=0

def show():
    try:
        global count
        count+=1
        lbl.configure(text=f"{datas[count]}:{fourth[count]}")
        btn.configure(text="следующая")
        shoow.place(x=100,y=20)
    except IndexError: messagebox.showerror("ошибка","новости закончились")

def show_link():
    webbrowser.open_new_tab(hrefs[count])

shoow = Button(tk, text="перейти к публикации", command=show_link)
shoow.place(x=30,y=20)
shoow.place_forget()   
btn = Button(tk, text="смотреть новости",command=show)
btn.place(x=0,y=20)

tk.mainloop()