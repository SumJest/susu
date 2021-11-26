"""
Задача №113662. Форум. Вывести путь
"""
from lab7.modules import forum

my_forum = forum.from_console()  # Получаем объект Forum, используя данные в консоли

k = int(input())  # Получаем номер сообщения, до которого нужно получить путь

print(my_forum.path(k))
