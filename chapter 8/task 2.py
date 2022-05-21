
class myclass:
    def __init__(self,a1,b1):
        if type(a1)==str:
            if type(b1)==str:
                self.str1=a1+b1
            elif type(b1)==int:
                self.str1=a1
                self.int1=b1
            else:
                self.str1=a1
        elif type(b1)==str:
            if type(a1)==str:
                self.str1=b1+a1
            elif type(a1)==int:
                self.str1=b1
                self.int1=a1
            else:
                self.str1=b1
        elif type(a1)==int:
            if type(b1)==int:
                self.int1=b1+a1
            elif type(b1)==str:
                self.str1=b1
                self.int1=a1
            else:
                self.int1=a1
        elif type(b1)==int:
            if type(a1)==int:
                self.int1=b1+a1
            elif type(a1)==str:
                self.str1=a1
                self.int1=b1
            else:
                self.int1=b1    
        else:
            pass
        
    def show(self):
        if hasattr(self,"str1")==True:
            print("Текстовое значение: ",self.str1)
        if hasattr(self,"int1")==True:
            print("Числовое значение: ",self.int1)
        
obj1=myclass("Я изучаю","программирование")
obj2=myclass(5,108)
obj3=myclass(45,"Python")
obj4=myclass("Я изучаю",56)
obj5=myclass(4.56,"Python")
obj6=myclass([1,"диск",5],"Python")
obj7=myclass([1,"диск",5],7/8)
obj1.show()
obj2.show()
obj3.show()
obj4.show()
obj5.show()
obj6.show()
obj7.show()