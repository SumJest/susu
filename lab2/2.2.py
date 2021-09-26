# Целые числа и числа с плавающей точкой являются одними из самых распространенных в языке Python

number = 9

print(type(number))  # Вывод типа переменной number

float_number = 9.0

# Создайте ещё несколько переменных разных типов и осуществите вывод их типов

integer_number = 3

string_number = "4.123"

print(str(float_number) + " (" + str(type(float_number)) + ")\n" + str(integer_number) + " (" + str(
    type(integer_number)) + ")\n" + string_number + " (" + str(type(string_number)) + ")\n")

# Существует множество функций, позволяющих изменять тип переменных.
# Изучите такие функции как int(), float(), str() и последовательно примените их к переменным, созданным ранее.
string_number = float(string_number)
print(string_number)
string_number = int(string_number)
print(string_number)
string_number = str(string_number)
print(string_number)
