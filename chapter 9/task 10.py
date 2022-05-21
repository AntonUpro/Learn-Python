# import random as r
class myclass1:
    """Напишите программу, в которой создается итератор, генерирующий числа Фибоначчи (первые два числа равны единице, а каждое следующее есть сумма двух предыдущих).
    Количество генерируемых чисел передается в качестве аргумента конструктору при создании итератора."""
    def __init__(self,x):
        self.x=x
        self.a=1
        self.b=1
        self.position=1
    def __iter__(self):
        print(self.a,self.b,end=" ")
        return self
    def __next__(self):
        self.position+=1
        if self.position>=self.x:
            raise StopIteration
        else:
            self.a,self.b=self.b,self.a+self.b
            return self.b


x=int(input("Введите количество чисел фибоначи в последовательности:"))   
A=myclass1(x)
B=iter(A)
try:
    while True:
        print(next(B), end=" ")
except StopIteration:
    print("\nКонец итерирования")
