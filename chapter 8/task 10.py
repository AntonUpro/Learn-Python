
class myclass2:
    num=0
    def __init__(self):
        if myclass2.num<100:
            myclass2.num+=1
            self.num=myclass2.num
            print("Создается объект номер",self.num,". Общее количество созданий объектов этого класса",myclass2.num)
            self.wood1=myclass2()
            self.wood2=myclass2()
        else:
            myclass2.num+=1
            self.num=myclass2.num
            print("Создается объект номер",self.num)
    def __del__(self):
        print("Удален объект", self.num)
        
wood3=myclass2()
