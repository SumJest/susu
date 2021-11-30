from datetime import datetime
from typing import List, Union
import random
import sorts
import numpy as np

def write(text: str):
    """
    Function write text in output.txt file
    :param text: text str
    :return: None
    """
    with open("lab8/output.txt", "w") as f:
        f.write(text)
        f.close()

def np_to_table(matrix: List[List[Union[str, float, int]]]) -> str:
    """
    Форматирует двумерный список в таблицу
    :param matrix: двумерный список из int
    :return: Строка - таблица
    """
    a = len(matrix)
    b = len(matrix[0])
    output = ""
    for i in range(a):
        output += ("{:<21} " * b).format(*map(str, matrix[i])) + "\n"
    return output.rstrip()


def bench(array: List[int]) -> List[float]:
    """
    Function tests 4 type of sorting and returns result in seconds
    :param array: list for sort
    :return: list of seconds
    """
    start = datetime.now().timestamp()
    sorts.bubble_sort(array)
    bubble = datetime.now().timestamp() - start

    start = datetime.now().timestamp()
    sorts.merge_sort(array)
    merge = datetime.now().timestamp() - start

    qar = array.copy()
    start = datetime.now().timestamp()
    sorts.quick_sort(qar, 0, N - 1)
    quick = datetime.now().timestamp() - start

    pyar = array.copy()
    start = datetime.now().timestamp()
    pyar.sort()
    py = datetime.now().timestamp() - start

    return [round(bubble, 3), round(merge, 3), round(quick, 3), round(py, 3)]


N = int(input())

my_list: List[int] = []
for i in range(N):
    my_list.append(random.randint(-100, 100))

results = [["Метод", "Пузырьком", "Слиянием", "Быстрая", "Встроенная"], ]

results.append(["случайная, с", ] + bench(my_list))  # Случайно сгенерированная последовательность
my_list.sort()
results.append(["Отсортированная, с", ] + bench(my_list))  # Отсортированная последовательность
my_list.reverse()
results.append(["отсортированная в обратном порядке, с", ] + bench(my_list))  # Инвертированная

table = np_to_table(np.matrix(results).transpose().tolist())

write(f"{N}\n" + table)
