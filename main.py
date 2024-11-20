# ВАРИАНТ 4
from itertools import combinations


START_SP = 15
MAX_SIZE = 9
items = {
    'r': (3, 25), 'p': (2, 15), 'a': (2, 15), 'm': (2, 20), 'i': (1, 5),
    'k': (1, 15), 'x': (3, 20), 't': (1, 25), 'f': (1, 15), 'd': (1, 10),
    's': (2, 20), 'c': (2, 20)
}


def itog(itemss): # итоговые параметры для выбранных предметов
    itog_size = sum([items[item][0] for item in itemss])
    itog_sp = sum([items[item][1] for item in itemss]) \
               + START_SP - sum([items[item][1] for item in items if item not in itemss])
    return itog_size, itog_sp


max_sp = float('-inf')
best_combination = ()
for size in range(1, len(items) + 1):
    for combination in combinations(items.keys(), size):
        total_size, total_sp = itog(combination)
        if total_size <= MAX_SIZE and total_sp > max_sp:
            max_sp = total_sp
            best_combination = combination


inventory = [[" " for _ in range(3)] for _ in range(3)]
index = 0
for item in best_combination:
    for _ in range(items[item][0]):
        if index < MAX_SIZE:
            inventory[index // 3][index % 3] = f"[{item}]"
            index += 1


for row in inventory:
    print(",".join(row))
print("Итоговые очки выживания:", max_sp)