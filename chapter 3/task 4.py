
# Online Python - IDE, Editor, Compiler, Interpreter
a=int(input("Введите А"))
b=int(input("Введите B"))
def list_snake(n,m):
    val=1
    tuple_character=[[i+1 for i in range(m)] for j in range(n)]
    print(tuple_character)
    for k in tuple_character:
        for l in k:
            print(l, end=" ")
        print()
    return tuple_character
list_snake(a,b)

def completion(x):
    n=0
    for q in range(len(x)):
        for w in range(len(x[q])):
            n+=1
            
                
    print(x)        
completion(list_snake(a,b))


  


