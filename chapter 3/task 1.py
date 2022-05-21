
# Online Python - IDE, Editor, Compiler, Interpreter
a=input("Введите текст: ")
n=int(input("Введите интервал выборки: "))
a=tuple(a)
b=tuple(a[n*k] for k in range((len(a)+n-1)//n))
print(a)
print(b)


  


