height = int(input('Введите висоту фигуры: '))
for i in range(height + 1):
    print('  ' * (height - i), end='')
    print('* ' * (i - 1), end='')
    print('* ' * i)





