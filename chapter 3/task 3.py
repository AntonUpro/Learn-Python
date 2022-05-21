
# Online Python - IDE, Editor, Compiler, Interpreter
from random import randint 
n=int(input("Веедите количество элементов основного списка: "))
m=int(input("Веедите количество элементов вложенных списков: "))
def tuple_character(n,m):
    val=str("А")
    tuple_character=[[chr(ord(val)+randint(0,30)) for i in range(m)] for j in range(n)]
    print(tuple_character)

tuple_character(n,m)



  


