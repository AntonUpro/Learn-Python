def pop(a):
    n=0
    sum=0
    otr=1
    while n!=a:
        sum = sum + otr
        otr=otr+2
        n+=1
    return print(sum)



x=int(input("Число"))
pop(x)