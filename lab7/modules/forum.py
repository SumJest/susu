from typing import List


class Message:
    m_id: int
    parent: int

    def __init__(self, m_id: int, parent: int):
        self.m_id = m_id
        self.parent = parent


class Forum:
    messages: List[Message]

    def __init__(self, messages_list: List[Message]):
        self.messages = messages_list

    def get_message(self, m_id: int) -> Message:
        """
        Function returns message by id
        :param m_id: id of message
        :return: Message object
        """

        for m in self.messages:
            if m.m_id == m_id:
                return m

    def has_child(self, m_id: int) -> bool:
        """
        Function checks for child messages
        :param m_id:
        :return: True - if there are message, False - if no
        """

        for m in self.messages:
            if m.parent == m_id:
                return True
        return False

    def del_message(self, m_id: int) -> int:
        """
        The function recursively deletes message n and its child messages. Pass 0 if you want to delete all messages\n
        :param m_id: id of message
        :return: count of deleted messages
        """

        count = 1

        if m_id == 0:  # Если нужно удалить все сообщения
            count = 0  # Приравниваем к нулю, так как нет сообщения под номером 0

        for m in self.messages:
            if m.parent == m_id:
                count += self.del_message(m.m_id)

        return count

    def path(self, m_id: int) -> str:
        """
        The function return full path to message n\n
        :param m_id: id of message
        :return: path
        """

        if m_id == 0:  # Если это корневое сообщение
            return f"0"
        parent = self.get_message(m_id).parent  # Получаем id родительского сообщения
        return self.path(parent) + f"#{m_id}"

    def tree(self, m_id: int = 0, level: int = 0):
        """
        The function prints struct of forum. \n
        :param m_id: number of message
        :param level: current level
        """

        for m in self.messages:
            if m.parent == m_id:
                print("**" * level + str(m.m_id))
                self.tree(m.m_id, level + 1)

    def root(self, m_id: int):
        message = self.get_message(m_id)
        if message.parent == 0:
            return m_id
        return self.root(message.parent)


def from_console() -> Forum:
    """
    Function read messages from console and return Forum object
    :return: Forum object
    """
    N = int(input())

    messages: List[Message] = []

    for i in range(N):
        line = input().split()
        m_id = int(line[0])
        parent = int(line[1])
        messages.append(Message(m_id, parent))

    return Forum(messages)
