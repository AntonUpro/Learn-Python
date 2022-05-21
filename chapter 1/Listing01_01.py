
def fac1(x):
    fac=1
    for k in range(1,x+1):
        fac=fac*k
    return print("Факториалом числа",x,"будет значение",fac)

n=int(input("Введите целое положительное число: "))

while n<1:
    n = int(input("Вы ввели отрицательное число, попробуйте еще раз: "))

else:
    fac1(n)




