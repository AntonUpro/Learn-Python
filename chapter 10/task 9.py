# Напишите программу, в которой создается и построчно заполняется двумерный список (список, элементами которого являются списки).
# Для заполнения каждой строки (каждого внутреннего списка) используется отдельный дочерний поток.
from threading import *
from time import sleep
from random import randint


def myf1(n1,n2):
    global L1, num
    mylock.acquire()
    t=current_thread()
    print(t.name)
    for i in range(n2):
        L1[n1][i]=num
        num+=1
        t=current_thread()
        print("Выполняется", t.name)
        print(L1[n1][i])
        sleep(0.5)
    print(L1[n1])
    mylock.release()
x=8
num=1
L1=[[randint(1,50) for j in range(x)] for i in range(x)]
print(L1)
T=[Thread(target=myf1, args=[k,x], name="Поток "+str(k+1)) for k in range(x)]
mylock=Lock()
for t in T:
    t.start()
for t in T:
    t.join()
print("Создание матрицы списков")
for i in L1:
    print(i)
    
