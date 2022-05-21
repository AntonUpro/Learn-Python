txt=input("Введите текст для шифрования: ")
txt2=""
txt3=""
for i in txt:
    if i=="а" or i=="А":
        txt2+=chr(ord(i)+(ord("я")-ord("а")-1))
    elif i=="б" or i=="Б":
        txt2 += chr(ord(i) + (ord("я")-ord("а")-1))
    elif (ord("а")>ord(i) or ord(i)>ord("я")) and (ord("А")>ord(i) or ord(i)>ord("Я")):
        txt2 += i
    else:
        txt2+=chr(ord(i)-2)
print("Зашифрованный текст:",txt2)

n=ord("Ю")-ord("А")

for i in txt2:
    if (ord("а")>ord(i) or ord(i)>ord("я")) and (ord("А")>ord(i) or ord(i)>ord("Я")):
        txt3+=i
    elif (i=="Ю" or i=="ю") or (i=="Я" or i=="я"):
        txt3+=chr(ord(i)-n)
    else:
        txt3+=chr(ord(i)+2)
print(txt3)

