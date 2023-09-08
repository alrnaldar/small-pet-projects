from tkinter import *
import pyautogui
import keyboard
from tkinter import ttk
import time
import threading
from tkinter import messagebox
start = True
key = "2"
tk = Tk()
tk.title("clicker")
tk.geometry("400x300")
# @
clicker_options = Label(tk, text='clicker options',font="header 8")
clicker_options.place(x=0,y=0)
# @
button_label = Label(tk, text="click button")
button_label.place(x=0,y=25)
bs=["left","right"]
strvar = StringVar(value=bs[0])
buttonlist = ttk.Combobox(textvariable=strvar,values=bs,width=4)
buttonlist.place(x=75,y=25)
howm = ["single","double"]
howmvar = StringVar(value=howm[0])
howm_combo = ttk.Combobox(values=howm, textvariable=howmvar,width=6)
howm_combo.place(x=150,y=25)
# @
click_interval = Label(tk, text="interval")
click_interval.place(x=0,y=50)
click_interval_entry = Entry(tk, width=7)
click_interval_entry.place(x=75,y=50)
times = ["millisecs", "secs","mins"]
mili = StringVar(value=times[0])
times_combo = ttk.Combobox(value=times,textvariable=mili,width=7)
times_combo.place(x=150,y=50)
# @
# def off():
#     global start
#     start = False
#     m()
# def on():
#     global start
#     start = True
#     m()

def m():
    global start
    print("ffff")
    while start:
        
        a1 = times_combo.get()
        a2 = int(click_interval_entry.get())
        a4 = buttonlist.get()
        a5 = howm_combo.get()
        if a1 == "millisecs":
            a3 = a2/1000
        if a1 == "secs":
            a3 = a2
        if a1 == "mins":
            print("dfd")
            a3 = a2*60
        print("there are")
        while True:
            if a5 == "single":       
                pyautogui.click(interval=a3,button=a4)
            if a5 == "double":
                pyautogui.doubleClick(interval=a3,button=a4)
            if keyboard.is_pressed(key):
                return
            
def n():
    th1 = threading.Thread(target=m)
    th1.start()            
def on():
    print("dfsdf")        
    keyboard.add_hotkey("f6", m)
on()
# @
def rebind():
    global key
    messagebox.showinfo("rebind", "stop-key has been reseted")
    if bindkeys.get() == 0:
        print("aaaaaa")
        key = "2"
    elif bindkeys.get() == 1:
        print('BBBBBBBBBB')
        key = "f5"
pressf = Label(tk, text="f6 to start", font="13")
pressf.place(x=0,y=100)
presstostop = Label(tk, text="f5 to stop",font="13")
presstostop.place(x=0,y=125)
bindkeys = BooleanVar()
bindkeys.set(0)
b2 = Radiobutton(tk, text="2",variable=bindkeys,value=0)
b2.place(x=100,y=125)
f5 = Radiobutton(tk, text="f5", value=1,variable=bindkeys)
f5.place(x=140,y=125)
changeb = Button(tk, text="rebind", command=rebind)
changeb.place(x=190,y=125)

# @
tk.mainloop()