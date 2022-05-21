
# Online Python - IDE, Editor, Compiler, Interpreter

from random import randint
a=int(input("Введите количество элементов списка: "))
list1=[randint(0,100) for i in range(a)]
print(list1)
n=1
for i in range(len(list1)-1):
    list1.insert(n,list1[n-1]+list1[n])
    n+=2
print(list1)
    






  


