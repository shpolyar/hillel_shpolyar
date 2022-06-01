import random
petia = int(input('Рост Пети: '))
height = [random.randint(150, 200) for _ in range(15)] + [petia]
height.sort(reverse=True)
a = 0
for i in height:
    if i == petia:
        a += 1
print(height)
print(f'Петя должен встать {height.index(petia) + a} в строй')

