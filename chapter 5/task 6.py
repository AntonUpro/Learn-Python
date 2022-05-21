txt=input("Введите зашифрованный текст: ")
txt2=""
for i in txt:
    if i=="я" or i=="Я":
        txt2+=chr(ord(i)+(ord("а")-ord("я")))
    elif (ord("а")>ord(i) or ord(i)>ord("я")) and (ord("А")>ord(i) or ord(i)>ord("Я")):
        txt2 += i

    else:
        txt2+=chr(ord(i)+1)

print(txt2)

