from msilib.schema import File
import pytesseract
from tkinter import *
from PIL import Image
from tkinter import filedialog
import pyperclip
import webbrowser
from tkinter import messagebox
import os
tk = Tk()
tk.title('recoder')
tk.geometry('600x350')
def copy():
    pyperclip.copy(lbl["text"])
def importer():
    global btn, lbl
    def importfile():
        global file,recod
        file = filedialog.askopenfilename()
        s = file.split('/')
        s = s[-1]
        btn.configure(text=s)
        recod = Button(tk, text='start',bg="green", command=recoder)
        recod.place(x=525, y=0)


    def recoder():
        global copyb,clearb,textafterbase,searchb
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        txt = Image.open(file)
        textafterbase = pytesseract.image_to_string(txt, lang='rus+eng')
        lbl.configure(text=textafterbase)
        clearb = Button(tk, text="clear",bg="red", command=clear)
        clearb.place(x=560,y=0)
        copyb = Button(tk, text='copy', command=copy)
        copyb.place(x=487,y=25)
        searchb = Button(tk,text="web search", command=search)
        searchb.place(x=525,y=25)
        print(len(textafterbase))
    
    def search():
        webbrowser.open_new(f"https://www.google.com/search?q={textafterbase}")
    def clear():
        lbl.configure(text="text here")
        btn.configure(text="import image")
        clearb.place_forget()
        copyb.place_forget()
        recod.place_forget()
        searchb.place_forget()
    
    btn = Button(tk, text='import image', command=importfile)
    btn.place(x=0, y=0)
    lbl = Label(tk, text='text here')
    lbl.place(x=0, y=50)

def check():
    def install():
            global count
            count = 0
            instly.place_forget()
            def sh():
                global url    
                messagebox.showinfo("installing requiments"," install to C:\Program Files") 
                url = "https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.2.0.20220712.exe"
                oipenin()
            def td():
                global url    
                messagebox.showinfo("installing requiments"," install to C:\Program Files") 
                url = "https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w32-setup-v5.2.0.20220712.exe"
                oipenin()
            def option():
                global count
                count += 1
                os.system("start https://imgur.com/a/LEZlk6h")
            x64 = Button(tk, text="install x64",font="header 20",command=sh)
            x64.place(x=0,y=60)
            x32 = Button(tk, text="install x32",font="header 20", command=td)
            x32.place(x=280,y=60)
            opt = Button(tk, text="instruction to install russian language ",font="header 20",command=option)
            opt.place(x=50,y=150)
            def oipenin():
                for i in range(1):
                    webbrowser.open_new(url)
                    x64.place_forget()
                    x32.place_forget()
                    inst.place_forget()
                    instly.place_forget()
                    opt.place_forget()
                    install()
            

    bz = os.path.exists(r'C:\Program Files\Tesseract-OCR\tesseract.exe')
    if bz == False:
        inst = Label(tk, text="tesseract ocr(software) required for application to work is not installed",font="header 10")
        inst.place(x=0,y=0)
        instly = Button(tk, text="install",command=install)
        instly.place(x=0,y=30)
    else: importer()
        
check()





tk.mainloop()