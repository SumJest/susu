"""
Задача №113660. Форум. Путь между сообщениями
"""
from lab7.modules import forum

my_forum = forum.from_console()

A, B = list(map(int, input().split()))


if str(A) in my_forum.path(B).split('#'):
    print("YES")
else:
    print("NO")
