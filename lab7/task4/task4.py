"""
Задача №113661. Форум. Номер корня
"""
from lab7.modules import forum

my_forum = forum.from_console()

A = int(input())

print(my_forum.root(A))
