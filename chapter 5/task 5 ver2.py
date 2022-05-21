txt1=input("Введите первый текст: ")
txt2=input("Введите второй текст: ")
txt3=""
if len(txt1)>len(txt2):
    for i in range(len(txt1)):
        if i<len(txt2):
            txt3+=(txt1[i]+txt2[i])
        else:
            txt3+=txt1[i]+"*"
else:
    for i in range(len(txt2)):
        if i<len(txt1):
            txt3+=(txt1[i]+txt2[i])
        else:
            txt3+=txt2[i]+"*"

print(txt3)

