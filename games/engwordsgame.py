from tkinter import *
import random
from translate import Translator

tk = Tk()
tk.title("funny game")
tk.geometry("500x500")


with open('wordlist.10000.txt', 'r') as file:
    words = file.readlines()
    words = [s.strip("\n") for s in words]
    
    def random_word():
        global word
        word = random.choice(words)
        
        lbl2.place_forget()
        
        
        lbl.configure(text=word)
        
        
    def show():
        
        lbl2.place(x=100,y=0)
        translation_process = Translator(to_lang="rus")
        translated = translation_process.translate(word)
        
        
        
        lbl2.configure(text=translated)
        
        

lbl = Label(tk, text="здесь слово")
lbl.place(x=0,y=0)
lbl2 = Label(tk, text="перевод")
lbl2.place(x=100,y=0)

btn = Button(tk, text="клацк",command=random_word)
btn.place(x=0,y=20)
btn2 = Button(tk, text="клуцк", command=show)
btn2.place(x=70,y=20)


tk.mainloop()