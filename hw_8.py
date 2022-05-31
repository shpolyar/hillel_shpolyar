# задача выполнена при условии, что дети построены по возрастанию
import random
petia = int(input('Рост Пети: '))
height = [random.randint(150, 200) for _ in range(15)] + [petia]
height.sort(reverse=True)
index = height.index(petia)
print(f'Петя должен встать {len(height) - index} в строй')

