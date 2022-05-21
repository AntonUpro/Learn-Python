import copy as co
from random import randint, seed
class myclass1:
    """Напишите программу, в которой для объектов предусмотрены операции сложения с числом, вычитания числа и вычитания из числа, а также умножения 
на число и деления на число. У объекта должно быть поле с числовым значением, и при выполнении указанных операций они должны выполняться с полем объекта."""
    def __init__(self,a):
        self.L1=a
    def __add__(self,val):
        if type(val)==int:
            self.L1+=val
    def __sub__(self,val):
        if type(val)==int:
            self.L1-=val    
    def __mul__(self,val):
        if type(val)==int:
            self.L1*=val 
    def __truediv__(self,val):
        if type(val)==int:
            self.L1/=val 
    def show(self):
        print("Значение L1=",self.L1, sep="")
seed(12)
obj1=myclass1(25)
obj1.show()
print("Умножаем на 5")
obj1+5
obj1.show()
print("Вычитаем 12")
obj1-12
obj1.show()
print("Умножаем на 6")
obj1*6
obj1.show()
obj1/2
obj1.show()


