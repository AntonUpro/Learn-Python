
from datetime import datetime, time
print("Введите время в формате \"2020-09-22 13:30:55\" год-месяц-число часы:минуты:секунды:")
a=input("Введите дату и время: ")
a=datetime.fromisoformat(a)
b=datetime.now()
s=a-b
print("Разница между текущим временеем и введеным составляет:",s)
print(s.total_seconds())