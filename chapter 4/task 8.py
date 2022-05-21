
# Online Python - IDE, Editor, Compiler, Interpreter
# вариант 1

c={"булгаков":"Мастер и Маргарита","пушкин":"Евгений онегин","достоевский":"преступление и наказание","тютчев":"Муму"}
n=0
for i in c.values():
    a=input("Введи автора произведения "+i)
    if c.get((a.lower()),"не верно")==i:
        n+=1
    else:
        continue

print(n)



  


