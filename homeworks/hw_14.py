import math


def square(side):
    return side * 4, side ** 2, side * math.sqrt(2)


side = int(input('Сторона квадрата: '))
res = square(side)
print(res)
