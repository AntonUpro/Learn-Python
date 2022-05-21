

a=int(input("Введите ваше число: "))
n=bin(a)
x=a.bit_length()
print(n)
print(x)
s=0
if a>=0:
    b=str(n)[2:]
    for i in b:
        s+=int(i)
    print("Сумма битов равна:",s)
else:
    b=str(n)[3:]
    for i in b:
        s+=int(i)
    print("Сумма битов равна:",s)
    

