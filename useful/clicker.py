from tkinter import *
import sys, keyboard
import pyautogui as pad

key = keyboard

win = Tk()
win.title("кликер")
win.geometry("400x250")

#def clicked2():
    #res2 = " {}".format(txt2.get())
    #res2 = int(txt2.get())
    #lbl2.configure(text=res2)
#def clicked():
    #res = " {}".format(txt.get())
    #res = (txt.get())
    #lbl.configure(text=res)
def clicked3():
    res = (txt.get())
    lbl.configure(text=res)
    res2 = int(txt2.get())
    lbl2.configure(text=res2)
    
    
    while True:  
        key.wait("8")
    
        while True:
            if key.is_pressed("9"):
                break
            pad.click(button=res, interval=res2)
    
lbl = Label(win, text="кнопка мыши")  
lbl.grid(column=0, row=0)
lbl2 = Label(win, text="скорость")  
lbl2.grid(column=0, row=1)
#btn = Button(win, text="начать", command=clicked)
#btn.grid(column=2, row=0)
#btn2 = Button(win, text="начать", command=clicked2)
#btn2.grid(column=2, row=1)
btn3 = Button(win, text="старт", command=clicked3)
btn3.grid(column=1, row=2)
txt = Entry(win,width=10)  
txt.grid(column=1, row=0)
txt2 = Entry(win,width=10)  
txt2.grid(column=1, row=1)





win.mainloop()
