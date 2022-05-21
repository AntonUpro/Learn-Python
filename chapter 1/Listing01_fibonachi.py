n=int(input("Введите количество значений: "))

f1=1
f2=1
print(f1,f2, end=" ")
sam=f1+f2
for k in range(2,n):
    f1,f2=f2,f1+f2
    sam=sam+f2
    print(f2, end=" ")

print("/n", sam)







