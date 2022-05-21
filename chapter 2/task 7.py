
# Online Python - IDE, Editor, Compiler, Interpreter
a=int(input("Введите первое число: "))
b=int(input("Введите второе число: "))
c=int(input("Введите третье число: "))

a,b,c=min(a,b,c),(a+b+c-min(a,b,c)-max(a,b,c)),max(a,b,c)
if b-a==c-b:
    print("Арифметическая последовательность")
else:
    print("Нет арифметической послеовательности")

