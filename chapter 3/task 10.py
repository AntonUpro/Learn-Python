
# Online Python - IDE, Editor, Compiler, Interpreter

from random import randint
a=int(input("Введите количество элементов списка: "))
list1=[randint(0,100) for i in range(a)]
print(list1)
list2=[randint(0,100) for i in range(a)]
print(list2)
list3=[]
for i in range(len(list1)):
    list3+=[list1[i]]
    list3+=[list2[i]]
print(list3)




  


