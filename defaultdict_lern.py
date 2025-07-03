
from collections import defaultdict


goods = [
    (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'ед': 'шт.'}),
    (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'ед': 'шт.'}),
    (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'ед': 'шт.'})
]

analitics = defaultdict(list)

for _, products in goods:
    for key, value in products.items():
        analitics[key].append(value)
        print(f'{key}  {value}')


print(analitics)

analitics = dict(analitics)

print(analitics)