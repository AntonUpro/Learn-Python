# import random as r

#   """Напишите программу, в которой пользователю предлагается ввести два целочисленных значения. Эти значения определяют границы диапазона, 
x1=0
x2=0
def f1():
    global x1
    try:
        x3=int(input("Введите первое целое число:"))
    except ValueError:
        print("Не верный тип данных, повторите попытку.")
        f1()
    else:
        x1=x3

def f2():
    global x2
    try:
        x4=int(input("Введите второе целое число:"))
    
    except ValueError:
        print("Не верный тип данных, повторите попытку.")
        f2()
    else:
        x2=x4

f1()
f2()

if x1<=x2:
    try:
        n=x1
        while True:
            if n<=x2:
                print(n, end=" ")
                n+=1
            else:
                raise StopIteration
    except StopIteration:
        print("\nСписок закончен")
else:
    try:
        n=x1
        while True:
            if n>=x2:
                print(n, end=" ")
                n-=1
            else:
                raise StopIteration
    except StopIteration:
        print("\nСписок закончен")
        
        


