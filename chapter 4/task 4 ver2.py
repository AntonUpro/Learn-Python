
# Online Python - IDE, Editor, Compiler, Interpreter

a=set(k for k in range(1,51) if k%3==0)
b=set(k for k in range(1,51) if k%4==0)
print(a)
print(b)
print(a^b)
print(a|b)

c=set()
for i in range(1,51):
    if (i%3==0 or i%4==0) and not (i%3==0 and i%4==0):
        c.add(i)

print(c)

    




  


