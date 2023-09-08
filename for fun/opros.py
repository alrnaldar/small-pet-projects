from tkinter import *
from tkinter import messagebox as mb
import time, random
import sys


tk = Tk()
tk.title("орос")
tk.geometry("400x250")

def Quit():
    mb.showerror('хитрюга','куда попер')
def ex():
    tk.destroy()
    

def clicked():
    #while False:
    nmb = [50,150,200]
    pos = random.randint(50,350)
    posy = random.choice(nmb)
    k1 = pos
    k2 = posy
    
    btn2.place(x=k1,y=k2)
def clicked2():
    btn3 = Button(tk, text="выход для лохича", font="header 20", command=ex)
    btn3.pack(side=LEFT)
    mb.showinfo('шооооооooоок','шоо мой брат лох')
     
    



lbl = Label(tk, text="ты лох?", font="header 30")
lbl.pack(side=TOP)

btn = Button(tk, text="да", font="header 20", command=clicked2)
btn.pack(side=LEFT)
btn2 = Button(tk, text="нет", font="header 20", command = clicked)
btn2.pack(side=RIGHT)

tk.attributes('-toolwindow', True)
tk.protocol("WM_DELETE_WINDOW", Quit)
tk.resizable(False, False)
tk.mainloop()
