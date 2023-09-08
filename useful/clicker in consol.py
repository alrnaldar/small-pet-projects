import pyautogui as pad
import sys
import keyboard
key = keyboard
yslovie = True
bttn = input("какая кнопка мыши right or left: ")
if bttn == "right":
    bttn2 = "right"
else:
    bttn2 = "left"
spd = int(input("введите скорость: "))
print("нажмите 8, чтобы начать ")
print("нажмите 9, чтобы завершить")



while True:  
    key.wait("8")
    
    while yslovie:
        if key.is_pressed("9"):
            break
        pad.click(button=bttn2, interval=spd)
        
