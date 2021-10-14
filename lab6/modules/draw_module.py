def PrintRectangle(a, b, file):
    f = open("lab6/" + file, "w")
    rectangle = ""
    for i in range(b):
        for j in range(a):
            if i == 0 or i == b - 1:
                rectangle += "* "
            else:
                if j == 0 or j == a - 1:
                    rectangle += "* "
                else:
                    rectangle += "  "
        rectangle += "\n"
    f.write(rectangle)
    f.close()


def PrintSquare(a, file):
    PrintRectangle(a, a, file)
