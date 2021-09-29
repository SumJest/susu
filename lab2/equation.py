import math

number = int(input("Введите номер функции(1-4): "))
x = float(input("Введите значение x: "))

try:
    if number == 1:
        print("y = " + str(1 / (math.sqrt(1 - x ** 4 - x ** 2))))
    elif number == 2:
        print("y = " + str(math.pow(math.e, math.sqrt(x + math.sqrt(x)))))
    elif number == 3:
        print("y = " + str((x ** 2 + 1) / (3 * (x ** 2 - 1)) + (x ** 2 - 1) * (1 - x)))
    elif number == 4:
        print("y = " + str(math.sqrt(x + math.sqrt(x + math.sqrt(x)))))
    else:
        print("Номер неверный ;-(")
except (ZeroDivisionError, ValueError):
    print("x не входит в область допустимых значений")
