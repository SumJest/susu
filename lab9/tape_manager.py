from typing import TextIO, List


class Tape(object):
    file: TextIO
    path: str
    current: str
    mode: str

    def __init__(self, file: str, mode: str):
        self.file = open(file, mode)
        self.path = file
        self.mode = mode

    def reopen(self, mode: str = ""):
        if mode:
            self.mode = mode
        self.file.close()
        self.file = open(self.path, self.mode)

    def read(self) -> str:
        n = ""
        ch = self.file.read(1)
        if ch == "" or ch == "\n":
            self.current = ch
            return ch
        while ch != " " and ch != "\n":
            n += ch
            ch = self.file.read(1)
        self.current = n
        return n

    def write(self, char: str):
        self.file.write(char)
        self.current = char

    def close(self):
        self.file.close()


def reopen(tapes: List[Tape], mode):
    for i in range(mode * 2, mode * 2 + 2):
        tapes[i].reopen('r')
    for i in range(((mode + 1) % 2) * 2, ((mode + 1) % 2) * 2 + 2):
        tapes[i].reopen('w')
