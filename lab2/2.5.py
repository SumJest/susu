# Переменные булева типа могут принимать только два значения.
# С помощью оператора сравнения == выведите два возможных значения переменной is_equal.
# Обратите внимание на результат применения функции int() к булевому значению.


two = 2

three = 3

#

print(int(two==three))

#

print(str(two==three))

"""
В языке Python поддерживается множество операций сравнения( ==, >=, < и т.д.).
Все подобные операции имеют одинаковый приоритет. Результат сравнения - булева переменная.
Сравнения могут осуществляться в любом порядке.
"""


one = 1

two = 2

three = 3

print(one < two < three)  # Сравнения (one < two) и (two < three) происходят в одно и то же время.

# Создайте несколько переменных и осуществите различные сравнения между ними, выведите результаты в консоль.

four = 4

four_too = 4

five = 5

six = 6

print(four>four_too, four>=four_too, six<five, six>=five)