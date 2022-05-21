
# Online Python - IDE, Editor, Compiler, Interpreter
# вариант 1

a={12:"Мастер и Маргарита",13:"Евгений онегин",14:"преступление и наказание",15:"Муму"}
b={8:"Мастер и Маргарита",12:"трабле",14:"чече говыаьы",15:"Муму"}
c={}
for i,j in b.items():
    if i in a.keys():
        c[i]=set(a[i]).union(b[i])
    else:
        c[i]=set(j)
print(c)




  


