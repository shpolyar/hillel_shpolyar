def arithmetic(num_1, num_2, operator):
    res = 0
    if operator == '+':
        res = num_1 + num_2
    elif operator == '-':
        res = num_1 - num_2
    elif operator == '*':
        res = num_1 * num_2
    elif operator == '/':
        res = num_1 / num_2
    else:
        print("Неизвестная операция")
    return res


num_1 = int(input('Первое число: '))
num_2 = int(input('Второе число: '))
operator = input('Операция: ')
print(arithmetic(num_1, num_2, operator))

