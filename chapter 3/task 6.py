
# Online Python - IDE, Editor, Compiler, Interpreter

a=[85,64,1,5,6,7,9,436,485,65,3,545,64,45]
print (a)
for k in range(len(a)):
    for i in range(len(a)-1):
        if a[i]>a[i+1]:
           a[i],a[i+1]=a[i+1],a[i]
        else:
            continue
    print (a)


print (a)


  


