
# Online Python - IDE, Editor, Compiler, Interpreter
try:
    a,b=eval(input("Введите два числа: "))
    print ("Уравнение "+str(a)+"x="+str(b)+"-"+str(a)+"-1")
    if a!=0:
        print ("Решением уравнения x="+str((b-1)/a-1))
    elif b==1:
        print("Решением является любое число")
    else:
        print("Решений у уравнения нет")
except:
    print("Данные введены не корректно")



  


