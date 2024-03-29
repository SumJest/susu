A, B, C = map(float, input().split(' '))

print("Уравнение")
# Используем команду .format() для того, чтобы подставить значения в формулу
# :.5f означает, что мы хотим вывести переданные значения как числа с плавающей точкой
# с 5 знаками после '.'
print("({:.5f})*X^2+({:.5f})*X+({:.5f})=0".format(A, B, C))
D = B ** 2 - 4 * A * C
if D > 0:
    print("Количество корней: 2")
    print("{:.5f}".format((-B - D ** 0.5) / (2 * A)))
    print("{:.5f}".format((-B + D ** 0.5) / (2 * A)))
elif D == 0:
    print("Количество корней: 1")
    print("{:.5f}".format((-B) / (2 * A)))
    print("{:.5f}".format((-B) / (2 * A)))
else:
    print("Количество корней: 0")
