
# Online Python - IDE, Editor, Compiler, Interpreter

from random import randint
a=int(input("Введите количество элементов списка: "))
list1=[randint(0,30) for i in range(a)]
print(list1)
list2=[]
list3=[]
n=0
for i in list1:
    if n%2==0:
        list2.insert(0,i)
        n+=1
    else:
        list3.insert(0,i)
        n+=1
print(list2)
print(list3)
list2.sort()
list3.sort(reverse=True)
print(list2)
print(list3)






  


