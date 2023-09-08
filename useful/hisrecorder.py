from tkinter import *
import pyscreenrec
import keyboard
import os
import sys
rec = pyscreenrec.ScreenRecorder()
tk = Tk()
tk.title('screenrecorder')
tk.geometry('400x250')


def startrec():
    filename = (name.get())
    label2.configure(text=filename)
    rec.start_recording(str(filename+".mp4"),6)


def stoprec():
    rec.stop_recording()


def pauserec():
    rec.pause_recording()


def resumerec():
    rec.resume_recording()


def filepathcheck():
    filename = (name.get())
    label2.configure(text=filename)
    crPath = os.path.abspath(os.path.dirname(filename))
    rootPath = os.path.split(os.getcwd())
    os.startfile(os.getcwd())
    print(rootPath)
    label3 = Label(tk, text=rootPath)
    label3.place(x=190, y=90)


label = Label(tk, text="file name ->", font='header')
label.place(x=15, y=40)
label2 = Label(tk, text="here is file name")
label2.place(x=15,y=20)

name = Entry(tk, width=25)
name.place(x=130, y=40)

startb = Button(tk, text='start', font='header 20', command=startrec)
startb.place(x=170, y=190)
stopb = Button(tk, text='stop', font='header 20', command=stoprec)
stopb.place(x=80, y=190)
resumeb = Button(tk, text='resume', font='header 20', command=resumerec)
resumeb.place(x=170, y=130)
pauseb = Button(tk, text='pause', font='header 20', command=pauserec)
pauseb.place(x=75, y=130)
fileb = Button(tk, text='filepath ->', command=filepathcheck)
fileb.place(x=100, y=90)




tk.mainloop()
