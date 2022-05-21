txt=input("Введите текст для шифрования: ")
gllow=["а","е","ё","и","о","у","ы","э","ю","я"]
glbig=["А","Е","Ё","И","О","У","Ы","Э","Ю","Я"]
sogllow=["б","в","г","д","ж","з","й","к","л","м","н","п","р","с","т","ф","х","ц","ч","ш","щ","ъ","ь"]
soglbig=["Б","В","Г","Д","Ж","З","Й","К","Л","М","Н","П","Р","С","Т","Ф","Х","Ц","Ч","Ш","Щ","Ъ","Ь"]
txt2=""
txt3=""
for i in txt:
    if (i in gllow) and (gllow.index(i)!=(len(gllow)-1)):
        txt2+=gllow[gllow.index(i)+1]
    elif (i in glbig) and (glbig.index(i)!=(len(glbig)-1)):
        txt2 += glbig[glbig.index(i) + 1]
    elif (i in sogllow) and (sogllow.index(i) != (len(sogllow) - 1)):
        txt2 += sogllow[sogllow.index(i) + 1]
    elif (i in soglbig) and (soglbig.index(i) != (len(soglbig) - 1)):
        txt2 += soglbig[soglbig.index(i) + 1]
    elif (i in gllow) and gllow.index(i)==(len(gllow)-1):
        txt2 += gllow[0]
    elif (i in glbig) and glbig.index(i)==len(glbig)-1:
        txt2 += glbig[0]
    elif (i in sogllow) and sogllow.index(i)==len(sogllow)-1:
        txt2 += sogllow[0]
    elif (i in soglbig) and soglbig.index(i)==len(soglbig)-1:
        txt2 += soglbig[0]
    else:
        txt2+=i
print("Зашифрованный текст:",txt2)
# Дешифрование текста
for i in txt2:
    if (i in gllow) and (gllow.index(i)!=0):
        txt3+=gllow[gllow.index(i)-1]
    elif (i in glbig) and (glbig.index(i)!=0):
        txt3 += glbig[glbig.index(i) - 1]
    elif (i in sogllow) and (sogllow.index(i) != 0):
        txt3 += sogllow[sogllow.index(i) - 1]
    elif (i in soglbig) and (soglbig.index(i) != 0):
        txt3 += soglbig[soglbig.index(i) - 1]
    elif (i in gllow) and gllow.index(i)==0:
        txt3 += gllow[len(gllow)-1]
    elif (i in glbig) and glbig.index(i)==0:
        txt3 += glbig[len(glbig)-1]
    elif (i in sogllow) and sogllow.index(i)==0:
        txt3 += sogllow[len(sogllow)-1]
    elif (i in soglbig) and soglbig.index(i)==0:
        txt3 += soglbig[len(soglbig)-1]
    else:
        txt3+=i
print("Расшифрованный текст:",txt3)



