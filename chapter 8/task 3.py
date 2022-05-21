from fractions import Fraction

class myclass:
    
    def __init__(self,L1):
        self.list1=[]
        for i in L1:
            if type(i)==int or type(i)==float or type(i)==Fraction:
                self.list1.append(i)

    def show(self):
        for k in self.list1:
            print(k, end=" ")
        print()
        
    def mean(self):
        print("Среднее значение элементов поля списка равно: ",sum(self.list1)/len(self.list1))
     
list2=[12,2.3,"руль",7/8,"флыв",64]   
obj1=myclass(list2)
obj1.show()
obj1.mean()

obj2=myclass([120,23,19,56,68])
obj2.show()
obj2.mean()
