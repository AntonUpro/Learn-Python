
# Online Python - IDE, Editor, Compiler, Interpreter
from random import *
a=int(input("Введите А"))
b=int(input("Введите B"))
matrix=[[randint(0,50) for i in range(a)] for j in range(b)]
print (matrix)
c=int(input("Введите какую строку нужно удалить: "))
matrix.pop(c-1)
print (matrix)
d=int(input("Введите номер столбца, который необходимо удалить: "))

for k in range(len(matrix)):
    matrix[k].pop(d-1)
print (matrix)


  


