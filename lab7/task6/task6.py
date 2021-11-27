"""
Задача №113663. Форум. Количество сообщений в самой длинной ветке
"""
from lab7.modules import forum

my_forum = forum.from_console()

print(my_forum.longer_branch())
