class_1 = int(input('Сколько учеников в классе №_1: '))
class_2 = int(input('Сколько учеников в классе №_2: '))
class_3 = int(input('Сколько учеников в классе №_3: '))
desks_1 = class_1 // 2 + class_1 % 2
desks_2 = class_2 // 2 + class_2 % 2
desks_3 = class_3 // 2 + class_3 % 2
print(f'Всего нужно будет закупить {desks_1 + desks_2 + desks_3} парт')

