import operator

my_dict = {'+': operator.add,
           '-': operator.sub,
           '*': operator.mul,
           '/': operator.truediv
           }


def arithmetic(num_1, num_2, operation):
    return my_dict.get(operation, "Неизвестная операция")(num_1, num_2)


num_1 = int(input('Первое число: '))
num_2 = int(input('Второе число: '))
operation = input('Операция: ')
print(arithmetic(num_1, num_2, operation))
