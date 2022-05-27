n = int(input('Введите число: '))
a = 1
print(n, end='\t\t')
while a ** 2 < n:
    print(a ** 2, end=' ')
    a += 1