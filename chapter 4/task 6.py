
# Online Python - IDE, Editor, Compiler, Interpreter
# вариант 1
n=int(input("Введите целое число: "))
a=list(i for i in range(1,n+1))
b={a[i]:a[-i-1] for i in range(len(a))}
print(a)
print(b)




  


