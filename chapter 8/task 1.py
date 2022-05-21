
class myclass:
    def __init__(self,a1,b1):
        self.one=a1
        self.two=b1
    def show(self):
        print("Первая строчка: "+self.one)
        print("Вторая строчка: "+self.two)
        
obj1=myclass("Я изучаю","программирование")
obj2=myclass("Я изучаю","Python")

obj2.show()
obj1.show()
obj1.__init__("У меня","все получится!")
obj1.show()