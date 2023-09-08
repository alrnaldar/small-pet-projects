from msilib.schema import File
import pytesseract
from tkinter import *
from PIL import Image,ImageTk
from tkinter import filedialog
import pyperclip
import webbrowser


from tkinter import messagebox

import os
from keyboard import add_hotkey
s = []
tk = Tk()
tk.title('recoder')
tk.geometry('400x200')

def main():
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
        


    def copy():
        # print(lbl["text"])
        # tk.clipboard_append(lbl['text'])
        pyperclip.copy(lbl["text"])

    def clear():
        lbl.configure(text="текст здесь")
        btn.configure(text="выбрать файл")
        clearb.place_forget()
        copyb.place_forget()
        recod.place_forget()
    def instol():
        inkey = adminstall.get()
        if inkey.encode("utf-16") == b'\xff\xfet\x00h\x00i\x00s\x00i\x00s\x00s\x00p\x00a\x00r\x00t\x00a\x00':
            p = r"(C:\for recoder)"
            os.mkdir(r"C:\for recoder")
            messagebox.showinfo("инфо","вип получен папка "+p+" создана,требуется перезагрузка приложения")
            tk.destroy()
        else:
            messagebox.showwarning("неправильно","неправильный пароль")

    btn = Button(tk, text='выбрать файл', command=importfile)
    btn.place(x=0, y=0)
    lbl = Label(tk, text='текст здесь')
    lbl.place(x=0, y=30)
    adminstall = Entry(tk,font="header 20", width="24")
    adminstall.place(x=100,y=300)
    adminstall.insert(0,"вип доступ, введите пароль")
    add_hotkey("enter", instol)
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
                    main()
            

    bz = os.path.exists(r'C:\Program Files\Tesseract-OCR\tesseract.exe')
    if bz == False:
        inst = Label(tk, text="не установлен tesseract ocr(программное обеспечение), необходимый для работы приложения",font="header 10")
        inst.place(x=0,y=0)
        tk.geometry("600x300")
        instly = Button(tk, text="скачать",command=install)
        instly.place(x=0,y=30)
    else:main()

def adminka():
    def opencutter():
        os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\Snipping Tool.lnk")
    def txti():
        global txt
        txt = r"C:\for recoder\Снимок.JPG"
        recoderi()
    def txtimpi():
        global file
        file = filedialog.askopenfilename()
        txt = Image.open(file)
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        textafterbase = pytesseract.image_to_string(txt, lang='rus+eng')
        lbli.configure(text=textafterbase)
        copyb = Button(tk, text="скопировать", command=copy)
        copyb.place(x=250,y=0)
    def recoderi():
        global textafterbase
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        textafterbase = pytesseract.image_to_string(txt, lang='rus+eng')
        lbli.configure(text=textafterbase)
        copyb = Button(tk, text="скопировать", command=copy)
        copyb.place(x=250,y=0)
        googleing = Button(tk, text="гуглить",command=google)
        googleing.place(x=340,y=0)
    def copy():
        pyperclip.copy(lbli["text"])
    btni = Button(tk, text="открыть ножницы", command=opencutter)
    btni.place(x=0,y=0)
    iforme = Button(tk, text="для меня", command=txti)
    iforme.place(x=120,y=0)
    lbli = Label(tk, text="текст")
    lbli.place(x=0,y=30)
    importfiler = Button(tk, text="импорт", command=txtimpi)
    importfiler.place(x=190,y=0)
    def google():
        webbrowser.open_new(f"https://www.google.com/search?q={textafterbase}")

checksnipper = os.path.exists(r"C:\for recoder")
if checksnipper == True:
    adminka()
else: check()



tk.mainloop()