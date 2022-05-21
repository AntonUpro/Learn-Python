txt=input("Введите предложение: ")
list1=txt.split()
list2=list(reversed(list1))
print(list1)
txt2=" ".join(list2)
print(txt2)

# Второй вариант в одну строку
print(" ".join(list(reversed(txt.split()))))





