from typing import List


def np_to_table(matrix: List[List[int]]) -> str:
    a = len(matrix)
    b = len(matrix[0])
    output = ""
    for i in range(a):
        output += ("{:<2} " * b).format(*matrix[i]) + "\n"
    return output.rstrip()


M, N = map(int, input().split())
X, Y = map(int, input().split())

board = [[0 for j in range(N)] for i in range(M)]

moves = [
    [1, 2],
    [2, 1],
    [2, -1],
    [1, -2],
    [-1, -2],
    [-2, -1],
    [-2, 1],
    [-1, 2]

]


# ------

def allowed_moves(x: int, y: int) -> List[List[int]]:
    possible = []
    for move in moves:
        if 0 <= x + move[0] < N and 0 <= y + move[1] < M and board[y + move[1]][x + move[0]] == 0:
            possible.append(move)
    return possible


def fill_board():
    x, y = X - 1, Y - 1
    for i in range(1, M * N + 1):
        board[y][x] = i
        # print(np_to_table(board))
        next_move: List[int] = []
        minimal = 8
        for move in allowed_moves(x, y):
            count = len(allowed_moves(x + move[0], y + move[1]))
            if count < minimal:
                minimal = count
                next_move = move
        if len(next_move) == 0:
            break
        x, y = x + next_move[0], y + next_move[1]


fill_board()
print(np_to_table(board))
