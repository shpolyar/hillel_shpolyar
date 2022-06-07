def checkio(a):
    res = 1
    for i in a:
        i = int(i)
        if i != 0:
            res *= i
    return res


number = input('Введите число: ')
print(checkio(number))
