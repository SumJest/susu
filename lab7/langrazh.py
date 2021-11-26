
def rec_p(x, n):
    print(1)
    if n == 1:
        return x
    elif n == 0:
        return 1
    a = rec_p(x, n - 1) * x * (2 * n + 1) / (n + 1) - rec_p(x, n - 2) * n / (n + 1)
    return a


def it_p(x, n):
    p1 = 1
    p2 = x
    count = 2
    for i in range(2, n + 1):
        p1 = p2 * x * (2 * i + 1) / (i + 1) - p1 * i / (i + 1)
        b = p1
        p1 = p2
        p2 = b
        count += 4
    print(count)
    return p2


print(rec_p(5, 20))
print(it_p(5, 20))
