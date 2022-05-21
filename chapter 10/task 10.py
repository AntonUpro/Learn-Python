# Напишите программу, в которой создается три дочерних потока. В первом потоке вычисляется факториал числа (произведение натуральных чисел). 
# Во втором потоке вычисляется двойной факториал числа (произведение чисел через одно). В третьем потоке вычисляется число из последовательности Фибоначчи 
# (первые два числа равны единице, а каждое следующее равно сумме двух предыдущих).
from threading import *
from time import sleep
from random import randint

class myThread(Thread):
    def __init__(self,a,b):
        super().__init__()
        mylock.acquire()
        self.num=a
        self.name=b
        mylock.release()
    def run(self):
        mylock.acquire()
        print(self.name)
        sleep(1)
        print(self.num)
        sleep(1)
        mylock.release()

def fib(n1):
    """Последовательность чисел фибоначи"""
    a=1
    b=1
    for i in range(n1-2):
        a,b=b,a+b
    return b

def fact1(n1):
    """Факториал числа"""
    if n1==1:
        return 1
    else:
        return n1*fact1(n1-1)
    
def fact2(n1):
    """Двойной факториал числа"""
    if n1<=2:
        return n1
    else:
        return n1*fact2(n1-2)

mylock=Lock()
x=int(input("Введите целое число: "))
A1=myThread(fib(x),fib.__doc__)
B1=myThread(fact1(x),fact1.__doc__)
C1=myThread(fact2(x),fact2.__doc__)
A1.start()
B1.start()
C1.start()
A1.join()
B1.join()
C1.join()
