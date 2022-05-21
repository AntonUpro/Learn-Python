
# Online Python - IDE, Editor, Compiler, Interpreter

a=int(input("Введите первое число: "))
b=int(input("Введите второе число: "))
set1=set()
set2=set()
for i in range(len(str(a))):
    set1.add(a%10)
    a=a//10
print(set1)
for j in range(len(str(b))):
    set2.add(b%10)
    b=b//10
print(set2)

set3=set1|set2
print(set3)

    




  


