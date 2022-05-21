
# Напишите программу, в которой с использованием потоков, вычисляется сумма квадратов натуральных чисел. 
# Сумма вычисляется определенное время, по аналогии с примером из листинга 10.15.

from threading import *

from time import sleep

def mysum():
    global num 
    k=1
    txt=str(num)
    while myevent.is_set():
        num+=k**2
        txt+=" + "+str(k**2)
        print("[",k**2,"]",txt,"=",num,sep="")
        k+=1
        sleep(0.3)

t=Thread(target=mysum)
num=0
myevent=Event()
myevent.set()
t.start()
sleep(2)
myevent.clear()
if t.is_alive():
    t.join()
print(num)

    