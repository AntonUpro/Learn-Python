# import random as r
class myclass1:
    """Напишите программу, в которой создается итератор, генерирующий нечетные натуральные числа. Количество генерируемых чисел определяется аргументом конструктора"""
    def __init__(self,x):
        self.x=x
        self.position=-1
    def __iter__(self):
        self.L1=[]
        for i in range(self.x):
            self.L1.append(2*i+1)
        return self
    def __next__(self):
        self.position+=1
        return self.L1[self.position]

# Второй вариант без создания списка 
class myclass2:
    """Напишите программу, в которой создается итератор, генерирующий нечетные натуральные числа. Количество генерируемых чисел определяется аргументом конструктора"""
    def __init__(self,x):
        self.x=x
        self.position=-1
    def __iter__(self):
        return self
    def __next__(self):
        if self.position==x-1:
            raise StopIteration
        else:
            self.position+=1
            return self.position*2+1

x=int(input("Введите количество генерируемых чисел: "))   
A=myclass1(x)
B=iter(A)
try:
    while True:
        print(next(B), end=" ")
except IndexError:
    print("Класс B закончил генерацию.")
# Второй вариант без создания списка 
C=myclass2(x)
D=iter(C)
try:
    while True:
        print(next(D), end=" ")
except StopIteration:
    print("Класс D закончил генерацию.")

