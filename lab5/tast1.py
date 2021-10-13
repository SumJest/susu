a, b, c = map(int, input().split(' '))

if max(a, b, c) >= (a + b + c - max(a, b, c)):
    print("Треугольник не существует")
elif a == b == c:
    print("Треугольник равносторонний")
elif a == b or a == c or b == c:
    print("Треугольник равнобедренный")
else:
    print("Треугольник общего вида")
