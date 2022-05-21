# Напишите программу, в которой с использованием двух дочерних потоков заполняется список. Первый поток присваивает буквенные значения 
# элементам с четными индексами. Второй поток присваивает числовые значения элементам с нечетными индексами.
from threading import *
from time import sleep

def character():
    global size, L
    txt=ord("A")
    while len(L)<=size:
        myevent.wait()
        myevent.clear()
        sleep(0.1)
        L.append(chr(txt))
        txt+=1
        myevent.set()
        sleep(0.1)
    
def number():
    global size, L
    num=1
    while len(L)<=size:
        myevent.wait()
        myevent.clear()
        sleep(0.1)
        L.append(num)
        num+=1
        myevent.set()
        sleep(0.1)

size=15
L=[]
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