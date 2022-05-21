txt=input("Введите предложение: ")
list1=txt.split()
list2=[]
for i in list1:
    list2.append(len(i))
print(list1)
print(list2)
nmax=list2.index(max(list2))
nmin=list2.index(min(list2))
if nmax>nmin:
    list1.remove(list1[nmax])
    list1.remove(list1[nmin])
else:
    list1.remove(list1[nmin])
    list1.remove(list1[nmax])
print(list1)
txt2=" ".join(list1)
print(txt2)



