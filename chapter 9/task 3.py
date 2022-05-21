import copy as co
from random import randint, seed
class myclass1:
    """Напишите программу, в которой для объектов класса определена операция сложения. У каждого объекта есть поле-список, и при сложении
объектов получается новый объект того же класса. Его поле-список получается объединением полей-списков исходных объектов."""
    def __init__(self,a):
        self.L1=a
    def __radd__(self,d):
        L3=co.copy(self.L1)
        return L3
    def __add__(self,val):
        if type(val)==list:
            L2=co.copy(val)
        for i in self.L1:
            L2.append(i)
        print("Проверка",L2)
        return myclass1(L2)
seed(12)
obj1=myclass1([randint(0,50) for i in range(6)])
obj2=myclass1([randint(0,50) for i in range(6)])
print(obj1.L1)
print(obj2.L1)
obj3=obj2+(1+obj1) #Пришлось выполнить ненужную операцию 1+obj1, что бы вернуть результатом операции список
print("Объект 3", obj3.L1)
print(obj3.__dict__)