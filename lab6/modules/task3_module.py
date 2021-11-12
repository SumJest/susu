import os


def input_exist() -> bool:
    for file in os.listdir(os.getcwd() + "\\lab6"):
        if file.endswith(".txt"):
            if file == "input.txt":
                return True
    return False


def read_n() -> int:
    f = open("lab6/input.txt", 'r')
    n = int(f.readline().split(' ')[0])
    f.close()
    return n


def prime_filter(list_of_integer: list) -> list:
    """
    Реализация алгоритма Решето Эратосфена
    :param list_of_integer: List of integer numbers
    :return: List of prime numbers
    """
    count = len(list_of_integer)
    list_of_integer = list(range(2, count + 1))  # список целых чисел до count
    i_num = 0  # Индекс текущего числа, кратные которому будут исключатся из массива
    while list_of_integer[i_num] ** 2 <= count:
        for i in range(list_of_integer[i_num] ** 2, count + 1,
                       list_of_integer[i_num]):  # Пробегаемся по всем числам, кратным выбранному
            if i in list_of_integer:
                list_of_integer.remove(i)
        i_num += 1  # берем следующее не исключенное число
    return list_of_integer


def write_line(line: str):
    f = open("lab6/output.txt", 'w')
    f.write(line)
    f.close()
