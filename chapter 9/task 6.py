
class myclass:
    """Напишите программу, в которой для объектов класса предусмотрен специальный режим доступа к полям. В частности, у объекта должно
быть поле-список, значением которому можно присваивать только список. Из присваиваемого списка в поле-список копируются только текстовые значения. 
При считывании значения этого поля возвращается текстовая строка, содержащая только начальные буквы текстовых значений, которые входят в список."""

    def __setattr__(self,name,val):
        if type(val)==list:
            self.__dict__[name]=[]
            for i in val:
                if type(i)==str:
                    self.__dict__[name].append(i)
        else:
            print("Приваиваемое поле не список!")
    def __getattribute__(self,name):
        if type(object.__getattribute__(self,name))==list:
            print("Запрашивается поле",name)
            res=""
            for i in object.__getattribute__(self,name):
                res+=i[0]
            return res
        else:
            return object.__getattribute__(self,name)

A=myclass()
A.list1=["Я",65,2,"буду",78,"программистом"]
print("Словарь для проверки:",A.__dict__)
print("Результат:",A.list1)

