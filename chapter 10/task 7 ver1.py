# Напишите программу, в которой с использованием двух дочерних потоков заполняется список. Первый поток присваивает буквенные значения 
# элементам с четными индексами. Второй поток присваивает числовые значения элементам с нечетными индексами.
from threading import *
from time import sleep

def character():
    global size, item, L
    txt=ord("A")
    while item<size:
        myevent.wait()
        myevent.clear()
        sleep(0.1)
        L[item]=chr(txt)
        txt+=1
        item+=1
        myevent.set()
        sleep(0.1)
    
def number():
    global size, item, L
    num=1
    while item<size:
        myevent.wait()
        myevent.clear()
        sleep(0.1)
        L[item]=num
        num+=1
        item+=1
        myevent.set()
        sleep(0.1)

size=15
L=["*" for k in range(size)]
item=0
print(L)

A=Thread(target=character)
B=Thread(target=number)
myevent=Event()
myevent.set()

A.start()
B.start()
myevent.clear()
A.join()
B.join()
print(L)