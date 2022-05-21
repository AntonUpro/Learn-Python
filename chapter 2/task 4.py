
# Online Python - IDE, Editor, Compiler, Interpreter
a=[1,51,654,68,22,46,3]
b=[1,51,654,68,22,46,3]
n=0
if len(a)==len(b):
    for k in range(len(a)):
        if a[k-1]==b[k-1]:
            continue
        else:
            print("Списки не равны")
            break
    else:    
        print("Списки равны")
else:
    print("Списки не равны")


