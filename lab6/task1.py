from lab6 import draw_module

sides = input().split(" ")
file = input()
file = file.strip("\"\'")  # Удалаем ковычки

if len(sides) == 1:
    draw_module.PrintSquare(int(sides[0]), file)
elif len(sides) == 2:
    draw_module.PrintRectangle(int(sides[0]), int(sides[1]), file)
