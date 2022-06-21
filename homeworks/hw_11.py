import string
import random

dict_1 = {}
dict_2 = {}

for _ in range(10):
    dict_1[random.choice(string.ascii_lowercase)] = random.randint(0, 10)
    dict_2[random.choice(string.ascii_lowercase)] = random.randint(0, 10)

print(f'Cловарь 1:\n{dict_1}')
print(f'Cловарь 2:\n{dict_2}')

for k, v in dict_2.items():
    if k in dict_1.keys():
        if v > dict_1[k]:
            dict_1[k] = v
    else:
        dict_1[k] = v

print(f'Новый словарь:\n{dict_1}')
