from collections import defaultdict

# Пример списка кортежей товаров
goods = [
    (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'ед': 'шт.'}),
    (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'ед': 'шт.'}),
    (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'ед': 'шт.'})
]

# Используем defaultdict для удобства
analytics = defaultdict(list)

for _, product in goods:
    for key, value in product.items():
        analytics[key].append(value)

# Преобразуем обратно в обычный dict (для красоты вывода)
analytics = dict(analytics)

print(f'\nАналитика:\n{analytics}')