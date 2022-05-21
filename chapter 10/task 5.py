# import math as m
#   Напишите программу, в которой, по аналогии с примером из листинга 10.8, с использованием пользовательского класса исключения и рекурсивного вызова функции 
# создается объект исключения со списком, содержащим (в обратном порядке) буквы алфавита.
class myclass(Exception):
    def __init__(self):
        self.values=[]
    def __add__(self,val):
        self.values.append(val)
        return self

def getMyError(n):
    try:
        if n>=ord("Z"):
            raise myclass
        getMyError(n+1)
    except myclass as error:
        raise error+chr(n)
def getList(n):
    try:
        getMyError(n)
    except myclass as error:
        return error.values
A=getList(ord("A"))
print(A)
        