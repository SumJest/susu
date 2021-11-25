"""
Задача №113659. Форум. Удаление ветви
"""
from typing import List


class Forum:
    messages: List[int]

    def __init__(self, messages_list: List[int]):
        self.messages = messages_list

    def del_message(self, n: int) -> int:
        """
        The function recursively deletes message n and its child messages
        :param n: number of message
        :return: count of deleted messages
        """
        if n not in messages:
            return 1
        count = 1
        for i, m in enumerate(messages):
            if m == n:
                count += self.del_message(i)
        return count


N = int(input())

messages = [-1 for i in range(N + 1)]

for i in range(N):
    line = input().split()
    parent = int(line[0])
    child = int(line[1])
    messages[parent] = child

k = int(input())
forum = Forum(messages)

print(forum.del_message(k))
