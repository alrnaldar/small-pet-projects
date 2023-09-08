from msilib.schema import File
import pytesseract
from tkinter import *
from PIL import Image
from tkinter import filedialog
import pyperclip
import webbrowser
from tkinter import messagebox
import os
import pyautogui
import time
cou = 0
s = []

tk = Tk()


tk.title('recoder')
tk.geometry('600x350')
def copy():
    pyperclip.copy(lbl["text"])
def reloadpage():
        choicelabel.place_forget()
        choice.place_forget()
        choice2.place_forget()
def importer():
    global back, cou, btn, lbl
    cou+=1
    reloadpage()
    back = Button(tk, text="назад", command=ch)
    back.place(x=0,y=320)
    def importfile():
        global file,recod
        file = filedialog.askopenfilename()
        s = file.split('/')
        s = s[-1]
        btn.configure(text=s)
        recod = Button(tk, text='Рекодировать', command=recoder)
        recod.place(x=130, y=0)


    def recoder():
        global copyb,clearb
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        txt = Image.open(file)
        textafterbase = pytesseract.image_to_string(txt, lang='rus+eng')
        lbl.configure(text=textafterbase)
        clearb = Button(tk, text="очистить", command=clear)
        clearb.place(x=300,y=0)
        copyb = Button(tk, text='скопировать', command=copy)
        copyb.place(x=217,y=0)
        




    def clear():
        lbl.configure(text="текст здесь")
        btn.configure(text="выбрать файл")
        clearb.place_forget()
        copyb.place_forget()
        recod.place_forget()
    
    btn = Button(tk, text='выбрать файл', command=importfile)
    btn.place(x=0, y=0)
    lbl = Label(tk, text='текст здесь')
    lbl.place(x=0, y=30)
def cutter():
    reloadpage()
    def img():
        pass
    def recoderforcut():
        global copyb,clearb
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        txt = Image.open(file)
        textafterbase = pytesseract.image_to_string(txt, lang='rus+eng')
        lblforcut.configure(text=textafterbase)
        # clearb = Button(tk, text="очистить", command=clear)
        # clearb.place(x=300,y=0)
        copyb = Button(tk, text='скопировать', command=copy)
        copyb.place(x=217,y=0)
    def opnapp():
        os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\Snipping Tool.lnk")
        btnimprt = Button(tk, text="выбрать файл",command=recoderforcut)
        btnimprt.place(x=100,y=0)
        orka = Label(tk, text="или")
        orka.place(x=200,y=0)
        btnauto = Button(tk, text="автовыбор файла")
        btnauto.place(x=220,y=0)
        ymol = Label(tk, text="по умолчанию")
    startcut = Button(tk, text="начать вырезку", command=opnapp)
    startcut.place(x=0,y=0)
    lblforcut = Label(tk, text="текст здесь")
    lblforcut.place(x=0,y=30)
    instforcut = Button(tk, text="ИНСТРУКЦИЯ",font="header 30",command=img)
    instforcut.place(x=140,y=270)
def ch():
    global choicelabel, choice, choice2
    choicelabel = Label(tk, text="режим:", font="header 19")
    choicelabel.place(x=250,y=40)
    choice = Button(tk, text="импортировать файл", font="header 25", command=importer)
    choice.place(x=120,y=80)
    choice2 = Button(tk, text="вырезать файл(ножницы)", font="header 25", command=cutter)
    choice2.place(x=90,y=160)
    if cou >= 1:
        back.place_forget()
        btn.place_forget()
        lbl.place_forget()
def check():
    def install():
            global count
            count = 0
            instly.place_forget()
            def sh():
                global url

                if count < 1:
                    messagebox.showinfo("погодь","сначала смотри инструкцию, потом нажми еще раз")
                else:
                    url = "https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.2.0.20220712.exe"
                    oipenin()
            def td():
                global url
                
                if count < 1:
                    messagebox.showinfo("погодь","смотри инструкцию, потом нажми еще раз")
                else:
                    url = "https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w32-setup-v5.2.0.20220712.exe"
                    oipenin()
            def option():
                global count
                # url = "https://oir.mobi/uploads/posts/2021-03/thumbs/1616374854_25-p-anime-art-devushka-na-avu-32.jpg"

                # resp = requests.get(url, timeout=10)
                # img = Image.open(BytesIO(resp.content))
                # image = ImageTk.PhotoImage(img)
                # lbl = Label(tk, image=image)
                # lbl.place(x=0,y=0)
                count += 1
                os.system("start https://imgur.com/a/LEZlk6h")
            x64 = Button(tk, text="скачать x64(бита)",font="header 20",command=sh)
            x64.place(x=0,y=60)
            x32 = Button(tk, text="скачать x32(бита)",font="header 20", command=td)
            x32.place(x=280,y=60)
            opt = Button(tk, text="ИНСТРУКЦИЯ",font="header 30",command=option)
            opt.place(x=100,y=150)
            def oipenin():
                for i in range(1):
                    webbrowser.open_new(url)
                    x64.place_forget()
                    x32.place_forget()
                    inst.place_forget()
                    instly.place_forget()
                    opt.place_forget()
                    ch()
            

    bz = os.path.exists(r'C:\Program Files\Tesseract-OCR\tesseract.exe')
    if bz == False:
        inst = Label(tk, text="tesseract ocr(software) required for application to work is not installed",font="header 10")
        inst.place(x=0,y=0)
        instly = Button(tk, text="install",command=install)
        instly.place(x=0,y=30)
    else: ch()
        
check()





tk.mainloop()