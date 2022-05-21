
class myclass:
    """Напишите программу, в которой для объектов класса предусмотрены операции сравнения. У каждого объекта есть поле-список с числовыми
значениями. Операции сравнения выполняются так: объекты на предмет равенства проверяются по первому элементу в списках, на предмет
«не равно» — по второму элементу в списках, «меньше» — по третьему элементу в списках, и так далее. Если соответствующего элемента
в списке нет, используется нулевое значение."""
    def __init__(self,L1):
        self.list1=L1
        self.n1=-1
    def __eq__(self, val):
        self.n1+=1
        if len(self.list1)<self.n1+1:
            return 0==val
        else:
            return self.list1[self.n1]==val   
    def __ne__(self, val):
        self.n1+=1
        if len(self.list1)<self.n1+1:
            return 0!=val
        else:
            return self.list1[self.n1]!=val   
    def __lt__(self, val):
        self.n1+=1
        if len(self.list1)<self.n1+1:
            return 0<val
        else:
            return self.list1[self.n1]<val   
    def __gt__(self, val):
        self.n1+=1
        if len(self.list1)<self.n1+1:
            return 0>val
        else:
            return self.list1[self.n1]>val    
    def __le__(self, val):
        self.n1+=1
        if len(self.list1)<self.n1+1:
            return 0<=val
        else:
            return self.list1[self.n1]<=val    
    def __ge__(self, val):
        self.n1+=1
        if len(self.list1)<self.n1+1:
            return 0>=val
        else:
            return self.list1[self.n1]>=val    

A=myclass([3,65,2,3,78,9,4])
B=myclass([3,6,2,-5,34,5,9,1])
print("Выполняется операция сравнения",A==B)
print("Выполняется операция \"не равно\"",A!=B)
print("Выполняется операция \"меньше <\"",A<B)
print("Выполняется операция \"больше >\"",A>B)
print("Выполняется операция \"меньше, либо равно <=\"",A<=B)
print("Выполняется операция \"больше, либо равно >=\"",A>=B)
