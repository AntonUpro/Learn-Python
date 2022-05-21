
# Online Python - IDE, Editor, Compiler, Interpreter
a=int(input("Введите целое число"))
b=""
for k in range(len(str(a))):
    c=9-a%10
    a=a//10
    b=b+str(c)
print(b[::-1])

    