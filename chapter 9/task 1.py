
class myclass1:
    num1=325
    def init(self,n1):
        "Не конструктор"
        self.num1=n1
    def show(self):
        print("Это из класса 1")
class myclass2(myclass1):
    num2=28
    def init(self,n1):
        self.num2=n1
    def show(self):
        print("Это из класса 2")
class myclass3(myclass2):
    num3=0
    def init(self,n1):
        self.num3=n1
    def show(self):
        print("Это из класса 3")

obj=myclass3()
print(obj.num1)
print(obj.num2)
print(obj.num3)
obj.init(34)
print(obj.num3)
obj.show()
obj2=myclass2()
obj2.init(15)
obj2.show()
print(obj.num2)
print(obj2.num2)