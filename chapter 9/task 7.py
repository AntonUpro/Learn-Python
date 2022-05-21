import random as r
class myclass:
    """Напишите программу с классом, объекты которого можно индексировать. В частности, у объекта должно быть два поля-списка с числами.
При индексировании объекта возвращается сумма элементов из списков с соответствующим индексом. Если в каком-то списке нет такого элемента, 
он заменяется нулевым значением."""
    def __init__(self,l1,l2):
        self.list1=l1
        self.list2=l2
    
    def __getitem__(self,index):
        try:
            return self.list1[index]+self.list2[index]
        except IndexError:
            if len(self.list1)>len(self.list2):
                return self.list1[index]+0
            else:
                return self.list2[index]+0

A=myclass([r.randint(0,20) for i in range(4)],[r.randint(0,20) for i in range(6)])
print(A.list1)
print(A.list2)
print("Словарь для проверки:",A.__dict__)
for i in range(max(len(A.list1),len(A.list2))):
    print(A[i])

