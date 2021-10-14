import math


def vradius(x, y, x1, y1):
    return ((x - x1) ** 2 + (y - y1) ** 2) ** 0.5


def getSquareCoord(x, y, r):
    return math.floor(x - r), math.floor(y - r), math.ceil(x + r), math.ceil(y + r)
