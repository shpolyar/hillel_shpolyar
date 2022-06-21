set_2 = {i for i in range(5)}
set_1 = {i for i in range(10)}
print('set_1 ', set_1)
print('set_2 ', set_2)

if len(set_1.intersection(set_2)) == len(set_2):
    print('set_1 является суперсетом для set_2')
else:
    print('set_1 не является суперсетом для set_2')

