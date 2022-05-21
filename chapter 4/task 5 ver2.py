
# Online Python - IDE, Editor, Compiler, Interpreter
# вариант 1
n=18
a=tuple(i*2+1 for i in range(n))
print(a)
b=set()
for i in range(n//2):
    b.add(a[i:i+2])
print(b)


# Вариант 2
c=set()  
for k in range(0,10):
    t=tuple(k*2+i for i in range(1,4) if i%2!=0)
    c.add(t)
    
print(c)



  


