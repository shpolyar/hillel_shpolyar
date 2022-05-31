import random
my_list = [random.randint(0, 100) for _ in range(20)]
print(my_list)
count = 0
for i in my_list[1:19]:
    index = my_list.index(i)
    if i > my_list[index - 1] and i > my_list[index + 1]:
        count += 1
else:
    print(f'Количество элементов, которые больше двух своих соседей: {count}')


