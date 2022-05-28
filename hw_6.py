n = int(input('Введите число: '))
if n != 0:
    items = []
    while n != 0:
        items.append(n)
        n = int(input('Введите число: '))
    total = 0
    quantity = 0
    max_num = 0
    min_num = 0
    number_of_even = 0
    number_of_odd = 0
    for i in items:
        total += i
        quantity += 1
        if i % 2:
            number_of_odd += 1
        else:
            number_of_even += 1
    items.sort()
    min_num = items[0]
    max_num = items[quantity - 1]
    average = total / quantity
    print(f"Количество введеных чисел: {quantity}\n"
          f"Сума введеных чисел: {total}\n"
          f"Среднее арефметическое введеных чисел: {average}\n"
          f"Максимальное значение: {max_num}\n"
          f"Минимальное значение: {min_num}\n"
          f"Количество парных чисел: {number_of_even}\n"
          f"Количесво непарных чисел: {number_of_odd}")
else:
    print('0 был введен сразу\nДля вычислений нужны натуральные числа')

