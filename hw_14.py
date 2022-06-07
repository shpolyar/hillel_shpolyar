import math


def square(side):
    p = side * 4
    s = side ** 2
    d = side * math.sqrt(2)
    return p, s, d


side = int(input('Сторона квадрата: '))
res = square(side)
print(res)
