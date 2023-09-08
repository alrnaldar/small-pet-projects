# import keyboard
# import time
# import sys

# while True:
#     key = keyboard
#     key.wait('space')
    
#     while True:
#         if key.is_pressed("2"):
#             sys.exit()
#         key.write('куу')
#         key.press("enter")
#         key.release("enter")
#         time.sleep(0.3)
        
import keyboard
import time
import sys

while True:
    key = keyboard
    key.wait('space')
    
    for i in range(999):
        if key.is_pressed("2"):
            sys.exit()
        key.write('#FREEPLOHOYPAREN')
        key.press("enter")
        key.release("enter")
        time.sleep(0.3)
    



