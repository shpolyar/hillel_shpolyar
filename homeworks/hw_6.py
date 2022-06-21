n = int(input('Введите число: '))
if n != 0:
    total = 0
    quantity = 0
    number_of_even = 0
    number_of_odd = 0
    max_num = 0
    min_num = n
    while n != 0:
        total += n
        quantity += 1
        if n % 2:
            number_of_odd += 1
        else:
            number_of_even += 1
        if n > max_num:
            max_num = n
        elif n < min_num:
            min_num = n
        n = int(input('Введите число: '))
    average = total / quantity
    print("Количество введеных чисел: ", quantity)
    print("Сума введеных чисел: ", total)
    print("Среднее арефметическое введеных чисел: ", average)
    print("Максимальное значение: ", max_num)
    print("Минимальное значение: ", min_num)
    print("Количество парных чисел: ", number_of_even)
    print("Количесво непарных чисел: ", number_of_odd)
else:
    print('0 был введен сразу\nДля вычислений нужны натуральные числа')

