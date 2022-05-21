class myclass2:
    num=0
    def __init__(self):
        myclass2.num+=1
        self.num=myclass2.num
        print("Создается классa myclass2. Общее количество созданий объектов этого класса",myclass2.num)
    def __del__(self):
        print("Удален объект", self.num)

def myf(n):
    """Из предыдущего задания"""
    global myclass2
    a=myclass2()
    b=a
    for i in range(n-1):
        a.next=myclass2()
        a=a.next
    return b

A=myf(5)
print(A.__class__)
print(A.next.__dict__)
print(A.next.next.next.__class__)

class myclass1:
    pass

def del_obj(num:"Номер удаляемого объекта",obj:"Объект из которого производиться удаление",vaule:"Имя переменной"):
    """Напишите программу, в которой создается цепочка объектов. Предложите метод или функцию, которые позволяют вставить новый объект
    в уже существующую цепочку, а также метод или функцию, которые позволяют удалить объект из цепочки (так, чтобы оставшиеся объекты образовали цепочку)"""
    if num!=2:
        for i in obj.__dict__:
            if i==vaule:
                del_obj(num-1,obj.__dict__[i],vaule)
    else:
        for i in obj.__dict__:
            if i==vaule:
                c=obj.__dict__[i]
                obj.__dict__[i]=c.__dict__[i]
    return obj

B=del_obj(3,A,"next")
print(B.num)
print(B.next.num)
print(B.next.next.num)
print(B.next.next.next.num)
# Не успел понять почему по окончанию все объекты удаляются