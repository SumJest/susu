from typing import List

board: List[List[int]]

# Пути передвижения шахматного коня
moves = [
    [2, 1],
    [2, -1],
    [1, 2],
    [1, -2],
    [-1, 2],
    [-1, -2],
    [-2, 1],
    [-2, -1],
]


# ------

def np_to_table(matrix: List[List[int]]) -> str:
    """
    Форматирует двумерный список в таблицу
    :param matrix: двумерный список из int
    :return: Строка - таблица
    """
    a = len(matrix)
    b = len(matrix[0])
    output = ""
    for i in range(a):
        output += ("{:<3} " * b).format(*matrix[i]) + "\n"
    return output.rstrip()


def allowed_moves(x: int, y: int) -> List[List[int]]:
    """
    Доступные пути из точки x, y
    :param x: Координата по x
    :param y: Координата y
    :return: Список из доступных путей
    """
    possible = []
    for move in moves:
        if 0 <= x + move[0] < N and 0 <= y + move[1] < M and board[y + move[1]][x + move[0]] == 0:
            possible.append(move)
    return possible


def fill_board():
    """
    Реализация правила Варнсдорфа
    :return:
    """
    x, y = X - 1, Y - 1
    for i in range(1, M * N + 1):
        board[y][x] = i
        # print(np_to_table(board))
        next_move: List[int] = []
        minimal = 9
        for move in allowed_moves(x, y):
            count = len(allowed_moves(x + move[0], y + move[1]))
            if count < minimal and (count != 0 or i == N * M - 1):
                minimal = count
                next_move = move
        if len(next_move) == 0:
            break
        x, y = x + next_move[0], y + next_move[1]
    if i != M * N:
        print(f"Маршрут не построен. Остановлен на x: {x}, y: {y}. i = {i}")


M, N = map(int, input().split())  # Чтение размера доски
X, Y = map(int, input().split())  # Чтение начальной позиции

board = [[0 for j in range(N)] for i in range(M)]

fill_board()

print(np_to_table(board))
