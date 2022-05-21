txt=input("Введите ваш текст:")
A=ord("А")
a=ord("а")
B=ord("Я")
b=ord("я")
n=a-A
#Можно не вводить столько переменных
for i in txt:
    if a<=ord(i)<=b:
        print(chr(ord(i)-n), end="")
    elif A<=ord(i)<=B:
        print(chr(ord(i) + n), end="")
    else:
        print(i, end="")


