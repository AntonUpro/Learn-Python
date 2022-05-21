txt=input("Введите ваш текст: ")
num=0
txt2=""
for i in range(len(txt)//3):
    txt2+=(txt[num+2]+txt[num+1]+txt[num])
    if (i+1)==len(txt)//3:
        txt2+=(txt[(num+3):])
    else:
        num+=3
print(txt)
print(txt2)

