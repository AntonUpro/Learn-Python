# Напишите программу, в которой создается объект с двумя списками. Списки заполняются значениями с помощью двух дочерних потоков:
# один список заполняется символами, а второй список заполняется числами.
from threading import *
from time import sleep
from random import randint
class myclass:
    pass
def symbol():
    global A
    index=0
    while index<len(A.L1):
        A.L2[index]=(chr(ord("А")+index))
        index+=1
def number():
    global A
    index=0
    while index<len(A.L1):
        A.L1[index]=index+1
        index+=1
A=myclass()
A.L1=[randint(1,50) for i in range(8)]
A.L2=[chr(randint(ord("А"),ord("Я"))) for i in range(8)]
print("Начальные списки с рандомными значениями")
print(A.L1)
print(A.L2)
A.L1.sort()  #Вспоминал сортировку элементов списка
A.L2.sort()
print(A.L1)
print(A.L2)
myevent=Event()
P1=Thread(target=symbol)
P2=Thread(target=number)
P1.start()
P2.start()
P1.join()
P2.join()
print("Полученные списки")
print(A.L1)
print(A.L2)