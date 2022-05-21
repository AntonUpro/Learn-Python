

a=int(input("Введите ваше число: "))
b=int(input("Введите номер бита для отображения: "))
n=bin(a)
x=a.bit_length()
print(n)
print(x)
if a>=0:
    print(n[len(str(n))-b])
else:
    print(n[len(str(n))-b])

