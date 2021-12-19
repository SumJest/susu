from typing import TextIO, List


class Tape:
    """
    Объект псевдоленты
    """
    file: TextIO
    path: str
    current: str
    mode: str

    def __init__(self, file: str, mode: str):
        self.file = open(file, mode)
        self.path = file
        self.mode = mode

    def reopen(self, mode: str = "") -> None:
        """
        "Отматывает" в начало ленту и задает режим работы с ней (чтение/запись)
        :param mode:
        :return:
        """
        if mode:
            self.mode = mode
        self.file.close()
        self.file = open(self.path, self.mode)

    def read(self) -> str:
        """
        Читает символ/число из файла
        :return: "\n" - конец блока, "" - конец ленты, число
        """
        n = ""
        ch = self.file.read(1)

        # Если конец блока или ленты
        if ch == "" or ch == "\n":
            self.current = ch
            return ch

        while ch != " " and ch != "\n":
            n += ch
            ch = self.file.read(1)
        self.current = n
        return n

    def write(self, char: str) -> None:
        """
        Записывает в файл символы
        :param char: символ(ы)
        :return:
        """
        self.file.write(char)
        self.current = char

    def close(self) -> None:
        """
        Прекращает работу с лентой
        :return:
        """
        self.file.close()


def reopen(tapes: List[Tape], mode) -> None:
    """
    Отматывает все ленты в tapes в начало с режимом работы,
    если передан mode=0, то ленты 0,1 - в режиме чтения; 2,3 - в режиме записи
    если передан mode=1, то ленты 0,1 - в режиме записи; 2,3 - в режиме чтения
    :param tapes: Ленты
    :param mode: режим работы
    :return:
    """
    for i in range(mode * 2, mode * 2 + 2):
        tapes[i].reopen('r')
    for i in range(((mode + 1) % 2) * 2, ((mode + 1) % 2) * 2 + 2):
        tapes[i].reopen('w')
