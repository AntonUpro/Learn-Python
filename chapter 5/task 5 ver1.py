txt1=input("Введите первый текст: ")
txt2=input("Введите второй текст: ")
txt3=""
if len(txt1)<len(txt2):
    txt1,txt2=txt2,txt1
for i in range(len(txt1)):
    if i<len(txt2):
        txt3+=(txt1[i]+txt2[i])
    else:
        txt3+=txt1[i]+"*"


print(txt3)

