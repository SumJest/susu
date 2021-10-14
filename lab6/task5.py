import numpy as np
import random as rand


def np_to_table(A):
    a = len(A)
    b = len(A[0])
    output = ""
    for i in range(a):
        output += ("{:<2} " * b).format(*A[i]) + "\n"
    return output.rstrip()


f = open("lab6/input.txt", 'r')
N, M = map(int, f.readline().split(" "))
f.close()

A = np.random.randint(0, 20, (N, M))

for i in range(N):
    maxn = max(A[i])
    for j in range(M):
        A[i][j] //= maxn
output = ""

output += "Матрица A:\n"
output += np_to_table(A) + "\n"

K = rand.randint(5, 15)
B = np.random.randint(0, 20, (M, K))

output += "Матрица B:\n" + np_to_table(B) + "\n"

output += "Матрица A*B:\n" + np_to_table(np.dot(A, B)) + "\n"

f = open("lab6/output.txt", 'w')
f.write(output)
f.close()
