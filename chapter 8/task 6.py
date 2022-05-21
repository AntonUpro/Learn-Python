# Напишите программу, в которой описан класс и функция, предназначенная для создания списка из объектов. У объектов класса должно быть поле
# (предназначенное для записи целочисленных значений). При вызове функции аргументом ей передается целое число, определяющее количество объ-
# ектов в списке. Поля объектов заполняются целыми нечетными числами.
# Создание первого класса
import random 
class myclass1:
    classnum=0
    def __init__(self):
        self.num1=random.randint(0,10)*2+1
        self.__name__=chr(ord("A")+myclass1.classnum)
        print(f"Создан класс {self.__name__} с полем num1={self.num1}.")
        myclass1.classnum+=1
# Создание функции
def do_obj(n):
    global myclass1
    list1=[]
    for i in range(n):
        list1.append(myclass1())
    return list1

list2=do_obj(6)
print("Количество созданных объектов на основе класса \"myclass1\":",myclass1.classnum)