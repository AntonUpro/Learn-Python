
# Online Python - IDE, Editor, Compiler, Interpreter
# вариант 1

c=input("Введите текст: ")

d=list(c)
a={}
for i in set(c):
    b=""
    k=0
    for j in list(c):
        if i!=j or k>0:
            b=b+d[d.index(j)]
        else:
            k=k+1
            continue 
    a[i]=b
print(a)




  


