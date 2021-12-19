import random
from typing import List
from math import ceil
from lab9 import sorts, tape_manager as tm

N = 45000  # Количество чисел в массиве
M = 10  # Максимальное количество чисел, которые мы можем держать в памяти
P = 4  # Количество лент, которые мы будем использовать

# Заполняем список случайными числами
my_list: List[int] = []
for i in range(N):
    my_list.append(random.randint(-100, 100))

# Создаем и заполняем файл нашим списком по M чисел на строку
with open("lab9/array.txt", 'w') as f:
    for i in range(N // M):
        f.write(" ".join(map(str, my_list[i * M:i * M + M])) + "\n")
    f.close()

# Освобождаем память, занятую списком
del my_list

# ----------

tapes: List[tm.Tape] = [tm.Tape(f"lab9/arrays/{i}.txt", 'w') for i in range(4)]  # Список из лент

# Заполняем первые две ленты нашим списком
with open("lab9/array.txt", 'r') as f:
    for i in range(ceil(N / M)):
        array = list(map(int, f.readline().split()))
        sorts.selection_sort(array)  # Сортируем каждый набор из M чисел внутренней сортировкой
        tapes[i % 2].write(" ".join(map(str, array)) + " \n")
    f.close()

# Режим работы, отражает из какой двойки лент мы сейчас читаем числа
# 0 - из лент 0, 1;
# 1 - из лент 2, 3
mode = 0

tm.reopen(tapes, mode)  # Отматываем все ленты в начало

while True:  # Основной цикл, каждую итерацию этого цикла мы меняем режим работы (mode)

    cur1 = tapes[mode * 2].read()
    cur2 = tapes[mode * 2 + 1].read()

    if not cur1 or not cur2:  # Проверка, если какой из файлов пустой, значит массив отсортирован
        if cur1:
            print(f"Массив отсортирован и находится в {tapes[mode * 2].path}")
        else:
            print(f"Массив отсортирован и находится в {tapes[mode * 2 + 1].path}")
        break

    tape_n = ((mode + 1) % 2) * 2  # номер ленты, в которую мы записываем массив в данный момент

    while cur1 or cur2:  # Цикл, каждую итерацию которого мы перескакиваем на следующий блок ленты

        # Если какая либо из лент закончилась, то мы на ленту tape_n записываем всё оставшиеся числа
        if cur1 == '':
            while cur2:
                if cur2 == "\n":
                    cur2 = tapes[mode * 2 + 1].read()
                    continue
                tapes[tape_n].write(cur2 + ' ')
                cur2 = tapes[mode * 2 + 1].read()

            break

        elif cur2 == '':
            while cur1:

                if cur1 == "\n":
                    cur1 = tapes[mode * 2].read()
                    continue
                tapes[tape_n].write(cur1 + ' ')
                cur1 = tapes[mode * 2].read()

            break

        while cur1 != "\n" or cur2 != "\n":  # Цикл, внутри которого мы бежим по одному блоку ленты

            # Если какая либо из лент закончилась, мы выходим из цикла
            if not cur1 or not cur2:
                break

                # Если блок одной из лент закончился, мы заполняем ленту tape_n оставшимся блоком
            if cur1 == "\n":
                tapes[tape_n].write(cur2 + " ")
                cur2 = tapes[mode * 2 + 1].read()
                continue
            elif cur2 == "\n":
                tapes[tape_n].write(cur1 + " ")
                cur1 = tapes[mode * 2].read()
                continue

            # Основной процесс слияния
            if int(cur1) < int(cur2):
                tapes[tape_n].write(cur1 + " ")
                cur1 = tapes[mode * 2].read()
            else:
                tapes[tape_n].write(cur2 + " ")
                cur2 = tapes[mode * 2 + 1].read()

        # Если закончилась только одна из лент, то мы переходим на следующую итерацию, чтобы
        # заполнить ленту tape_n оставшейся лентой
        if bool(cur1) != bool(cur2):
            continue

        tapes[tape_n].write("\n")  # Обозначаем конец блока в ленте tape_n

        tape_n = ((mode + 1) % 2) * 2 + (tape_n + 1) % 2  # переключаемся на следующую ленту из пары

        cur1 = tapes[mode * 2].read()
        cur2 = tapes[mode * 2 + 1].read()

    mode = (mode + 1) % 2  # Переключаем режим
    tm.reopen(tapes, mode)  # Отматываем все ленты в начало
