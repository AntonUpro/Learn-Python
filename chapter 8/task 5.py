# Напишите программу, в которой описывается функция, предназначенная для создания объекта. Объект создается на основе уже существующего объекта, который передается
# функции в качестве аргумента. В создаваемый объект добавляются только те неслужебные поля из исходного объекта, которые имеют целочисленное значение.
# Создание первого класса
class myclass1:
    def __init__(self):
        self.num1=8
        self.num2=2.5
        self.num3=563
        self.num4=16/4
        self.num5=-56
        self.num6=0
        self.num7="проверка текста"
    def show(self):
        print("Текст для проверки метода")
obj1=myclass1()
print(obj1.__dict__)
# Создание функции
def do_obj(obj):
    list1=[]
    for i in obj.__dict__:
        if type(obj.__dict__[i])!=int:
            list1.append(i)
    for i in list1:
        print("Удаляется поле со значением:",obj.__dict__[i])
        del obj.__dict__[i]
    return obj

obj2=do_obj(obj1)
print(obj2.__dict__)
print("Проверка метода show в полученном классе")
obj2.show()
