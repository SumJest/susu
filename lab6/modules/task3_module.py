import os


def input_exist():
    for file in os.listdir(os.getcwd() + "\\lab6"):
        if file.endswith(".txt"):
            if file == "input.txt":
                return True
    return False


def read_n():
    f = open("lab6/input.txt", 'r')
    n = int(f.readline().split(' ')[0])
    f.close()
    return n


def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def write_line(line):
    f = open("lab6/output.txt", 'w')
    f.write(line)
    f.close()
