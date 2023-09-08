from tkinter import *
import time, random, sys
coord = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10, 11, -11, 12, -12, 13, -13, 14, -14, 15, -15, 16, -16, 17, -17, 18, -18, 19, -19, 20, -20, 21, -21, 22, -22, 23, -23, 24, -24, 25, -25, 26, -26, 27, -27, 28, -28, 29, -29, 30, -30, 31, -31, 32, -32, 33, -33, 34, -34, 35, -35, 36, -36, 37, -37, 38, -38, 39, -39, 40, -40, 41, -41, 42, 
-42, 43, -43, 44, -44, 45, -45, 46, -46, 47, -47, 48, -48, 49, -49, 50, -50, 51, -51, 52, -52, 53, -53, 54, -54, 55, -55, 56, -56, 57, -57, 58, -58, 59, -59, 60, -60, 61, -61, 62, -62, 63, -63, 64, -64, 65, -65, 66, -66]
def start():
    while True:
        ball1.igra()
        ball2.igra()
        ball3.igra()
        ball4.igra()
        ball5.igra()
        ball6.igra()
        ball7.igra()
        ball8.igra()
        ball9.igra()
        ball10.igra()
        ball11.igra()
        ball12.igra()
        ball13.igra()
        ball14.igra()
        ball15.igra()
        ball16.igra()
        ball17.igra()
        ball18.igra()
        ball19.igra()
        ball20.igra()
        ball21.igra()
        ball22.igra()
        ball23.igra()
        ball24.igra()
        ball25.igra()
        ball26.igra()
        ball27.igra()
        ball28.igra()
        ball29.igra()
        ball30.igra()
        ball31.igra()
        ball32.igra()
        ball33.igra()
        ball34.igra()
        ball35.igra()
        ball36.igra()
        ball37.igra()
        ball38.igra()
        ball39.igra()
        ball40.igra()
        ball41.igra()
        ball42.igra()
        ball43.igra()
        ball44.igra()
        ball45.igra()
        ball46.igra()
        ball47.igra()
        ball48.igra()
        ball49.igra()
        ball50.igra()
        tk.update_idletasks()
        tk.update()
        time.sleep(0.0001)
def stop():
    sys.exit()

class Ball:
    # for i in range(5):
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        # coord = [-3, -2, -1, 1, 2, 3]

        random.shuffle(coord)
        self.y = coord[1]
        self.x = -3
    def igra(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = random.randint(1,10)
        if pos[3] >= 500:
            self.y = 0 - random.randint(1, 10)
        if pos[0] <= 0:
            self.x = random.randint(1,10)
        if pos[2] >= 500:
            self.x = 0 - random.randint(1, 10)
 


tk = Tk()
tk.title('Игра')
tk.geometry('500x500')
tk.resizable(height = False, width = False)        
canvas = Canvas(tk, width = 500, height = 500, bd=0, highlightthickness=0)
canvas.pack()

btn = Button(tk, text='Start', padx=20, pady=5, command=start)
btn.place(x=0, y=450)


btn2 = Button(canvas, text='Stop', padx=20, pady=5, command=stop)
btn2.place(x=100, y=450)

# for i in range(1):
#     # nm = 1
#     # num = str(nm)
#     # numb = int(num)
#     # res = numb+i
#     # # ball = f'ball{res}.igra()'
#     # ball = f'Ball{res}= (canvas, "red")'
#     ball1= Ball(canvas, "red")
    
    


 
ball1= Ball(canvas, "black")
ball2= Ball(canvas, "white")
ball3= Ball(canvas, "blue")
ball4= Ball(canvas, "white")
ball5= Ball(canvas, "yellow")
ball6= Ball(canvas, "yellow")
ball7= Ball(canvas, "yellow")
ball8= Ball(canvas, "yellow")
ball9= Ball(canvas, "black")
ball10= Ball(canvas, "blue")
ball11= Ball(canvas, "black")
ball12= Ball(canvas, "white")
ball13= Ball(canvas, "red")
ball14= Ball(canvas, "black")
ball15= Ball(canvas, "black")
ball16= Ball(canvas, "blue")
ball17= Ball(canvas, "black")
ball18= Ball(canvas, "yellow")
ball19= Ball(canvas, "black")
ball20= Ball(canvas, "black")
ball21= Ball(canvas, "white")
ball22= Ball(canvas, "red")
ball23= Ball(canvas, "blue")
ball24= Ball(canvas, "yellow")
ball25= Ball(canvas, "yellow")
ball26= Ball(canvas, "yellow")
ball27= Ball(canvas, "blue")
ball28= Ball(canvas, "blue")
ball29= Ball(canvas, "black")
ball30= Ball(canvas, "yellow")
ball31= Ball(canvas, "yellow")
ball32= Ball(canvas, "red")
ball33= Ball(canvas, "black")
ball34= Ball(canvas, "yellow")
ball35= Ball(canvas, "white")
ball36= Ball(canvas, "yellow")
ball37= Ball(canvas, "white")
ball38= Ball(canvas, "white")
ball39= Ball(canvas, "white")
ball40= Ball(canvas, "white")
ball41= Ball(canvas, "blue")
ball42= Ball(canvas, "yellow")
ball43= Ball(canvas, "red")
ball44= Ball(canvas, "blue")
ball45= Ball(canvas, "black")
ball46= Ball(canvas, "white")
ball47= Ball(canvas, "blue")
ball48= Ball(canvas, "blue")
ball49= Ball(canvas, "red")
ball50= Ball(canvas, "white")



tk.mainloop()