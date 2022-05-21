class myclass1:
    """Напишите программу, в которой есть класс с переопределенными методами для приведения к разным типам. В частности, у объекта должны
быть поля с целочисленным значением, текстом и действительным числовым значением. При приведении объекта к целочисленному, тексто-
вому или действительному числовому типу возвращается значение соответствующего поля."""
    def __init__(self,*a):
        self.L1=[]
        self.L2=[]
        self.L3=[]
        for i in a:
            if type(i)==int:
                self.L1.append(i)
            elif type(i)==str:
                self.L2.append(i)
            elif type(i)==float:
                self.L3.append(i)
            else:
                print(f"Обект {i} неизвестного типа")
    def __int__(self):
        self.s=sum(self.L1)
        return self.s
    def __str__(self):
        return " ".join(self.L2)    
    def __float__(self):
        self.s=sum(self.L3)
        return self.s/len(self.L3)   

obj=myclass1(12,6.9,"Я",4,5.2,"стану",9.9,"программистом",100,[1,5,9])
print(obj)
print("Сумма целочисленных зачений равна",int(obj))
print("Среднее значение не целых числе равно",float(obj))