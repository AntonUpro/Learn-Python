
from datetime import date
print("Введите дату в формате \"2020-09-21\" год-месяц-день:")
a=(input("Введите первую дату: "))
b=(input("Введите вторую дату: "))
a=date.fromisoformat(a)
b=date.fromisoformat(b)
if a>b:
    s=a-b
else:
    s=b-a
print("Количество дней равно:",s.days)
