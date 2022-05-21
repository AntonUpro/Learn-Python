
# Online Python - IDE, Editor, Compiler, Interpreter
a=int(input("Введите первую сторону треугольника: "))
b=int(input("Введите вторую сторону треугольника: "))
c=int(input("Введите третью сторону треугольника: "))
if ((a+b>c) or (a+c>b) or (b+c>a)) and (max(a,b,c)<((a+b+c)-max(a,b,c))):
    print("Треугольник с такими сторонами существует")
else:
    print("Треугольника с такими сторонами не существует")

