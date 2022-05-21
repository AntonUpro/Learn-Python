
# Online Python - IDE, Editor, Compiler, Interpreter
n=int(input("Введите целое число: "))
a=tuple(str(n))
a=tuple(int(i) for i in a)
b=tuple(int(k) for k in reversed(tuple(str(n))))
print(a)
print(b)



  


