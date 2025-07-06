'''Задача 1:
Есть словарь с товарами и их ценами, нужно найти товар с максимальной ценой.
Пример:
python
КопироватьРедактировать
products = {'laptop': 2000, 'mouse': 25, 'keyboard': 100}
# ожидаемый вывод: 'laptop'
'''

products = {'laptop': 2000, 'mouse': 25, 'keyboard': 100}

expensive_price = {'price': 0}

for item, price in products.items():
    if price > expensive_price['price']:
        expensive_price['price'] = price
        item_name = item
        item_price = price

print(f'\nThe most expensive item is {item_name}\nAnd it price is {item_price}')


'''products = {'laptop': 2000, 'mouse': 25, 'keyboard': 100}

max_price = 0
item_name = ''

for item, price in products.items():
    if price > max_price:
        max_price = price
        item_name = item

print(f'\nThe most expensive item is {item_name}\nAnd its price is {max_price}')'''