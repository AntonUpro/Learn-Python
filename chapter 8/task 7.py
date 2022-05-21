import random as r
class myclass1:
    pass

A=myclass1()
B=myclass1()
A.list1=[r.randint(0,50) for i in range(15)]
B.list2=[r.randint(0,50) for i in range(10)]
print(A.list1)
print(B.list2)

def myf(a,b):
    """Напишите программу, в которой описана функция. В качестве аргументов функции передаются два объекта одного и того же класса.
У каждого объекта есть поле, представляющее собой список из целых чисел. В результате функция возвращает объект того же класса. 
Поле-список этого объекта получается суммированием соответствующих элементов из полей-списков объектов, переданных аргументами функции.
Если в этих объектах списки разной длины, то недостающие элементы в списке заменяются нулями."""
    slist=[]
    for i in a.__dict__:
        if type(a.__dict__[i])==list:
            alist=a.__dict__[i]
    for i in b.__dict__:
        if type(b.__dict__[i])==list:
            blist=b.__dict__[i]
    if len(blist)>len(alist):
        alist,blist=blist,alist
    for k in range(len(alist)):
        if k>=len(blist):
            slist.append(alist[k])
        else:
            slist.append(alist[k]+blist[k])
    c=a.__class__()
    c.list3=slist
    return c
D=myf(A,B)
print(D.__class__.__name__)
print(D.__dict__)
