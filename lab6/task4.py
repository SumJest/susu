from lab6 import task4_module
from datetime import datetime

output = ""
start = datetime.now()
output += datetime.strftime(start,
                            "%d.%m.%Y %H:%M") + "\n"

f = open("lab6/input.txt", 'r')

r = int(f.readline())
x, y = map(int, f.readline().split(' '))

f.close()

x1, y1, x2, y2 = task4_module.getSquareCoord(x, y, r)

count = 0

for i in range(x1, x2 + 1):
    for j in range(y1, y2 + 1):
        if task4_module.vradius(x, y, i, j) <= r:
            count += 1

output += str(count) + "\n"

output += str(round(datetime.timestamp(datetime.now()) - datetime.timestamp(start), 2))

f = open("lab6/output.txt", 'w')
f.write(output)
f.close()
