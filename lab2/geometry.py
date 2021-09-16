from math import sqrt
from math import sin

number = int(input("Введите номер задачи(1-4): "))
a = float(input("Введите значение a: "))

try:
    if number == 1:
        print("Радиус сферы равен: " + str(a*sqrt(3)/2))
    elif number == 2:
        print("Радиус сферы равен: " + str((a/(4*sqrt(3)))*(3+sqrt(5))))
    elif number == 3:
        print("Радиус сферы равен: " + str((a/4)*sqrt(2*(5+sqrt(5)))))
    elif number == 4:
        r = float(input("Введите радиус вписанной окружности: "))
        print("Площадь равнобедренной трапеции равна: " + str(4*(r**2)/sin(a)))
    else:
        print("Номер неверный ;-(")
except (ZeroDivisionError, ValueError):
    print("Введенные значения не входят в область допустимых значений")
