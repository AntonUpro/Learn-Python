
# Online Python - IDE, Editor, Compiler, Interpreter

try:
    a=int(input("Введите первое целое число: "))
    b=int(input("Введите второе целое число: "))
    print("первое число больше" if a>b else "второе число больше")
except TypeError:
    print("TypeError введено не верное значение")
except ValueError:
    print("ValueError введено не верное значение")


