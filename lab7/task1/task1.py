"""
Задача №113659. Форум. Удаление ветви
"""
from lab7.modules import forum


my_forum = forum.from_console()

k = int(input())

print(my_forum.del_message(k))
