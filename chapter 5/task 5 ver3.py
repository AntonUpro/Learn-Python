txt=input("Введите зашифрованный текст: ")
txt2=""
for i in txt:
    if i=="я" or i=="Я":
        txt2+=chr(ord(i)+(ord("а")-ord("я")))
    else:
        txt2+=chr(ord(i)+1)

print(txt2)

