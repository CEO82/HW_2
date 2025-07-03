'''У тебя есть список заказов в интернет-магазине в виде:

orders = [
    {'customer': 'Alice', 'item': 'Laptop', 'qty': 1},
    {'customer': 'Bob', 'item': 'Mouse', 'qty': 2},
    {'customer': 'Alice', 'item': 'Mouse', 'qty': 1},
    {'customer': 'Alice', 'item': 'Keyboard', 'qty': 1},
    {'customer': 'Bob', 'item': 'Laptop', 'qty': 1},
]

Требуется:

1️⃣ Построить словарь вида:

{
    'Alice': {'Laptop': 1, 'Mouse': 1, 'Keyboard': 1},
    'Bob': {'Mouse': 2, 'Laptop': 1}
}

То есть:

Ключи — имена покупателей.

Значения — словарь покупок (товар: общее количество этого товара у покупателя).

2️⃣ Использовать для решения defaultdict (и вложенный defaultdict для внутреннего словаря).

3️⃣ Вывести итоговую структуру аккуратно (print) для визуальной проверки.


'''

from collections import defaultdict

orders = [
    {'customer': 'Alice', 'item': 'Laptop', 'qty': 1},
    {'customer': 'Bob', 'item': 'Mouse', 'qty': 2},
    {'customer': 'Alice', 'item': 'Mouse', 'qty': 1},
    {'customer': 'Alice', 'item': 'Keyboard', 'qty': 1},
    {'customer': 'Bob', 'item': 'Laptop', 'qty': 1},
]


summary = defaultdict(lambda: defaultdict(int))

for order in orders:
    customer = order['customer']
    item = order['item']
    qty = order['qty']

    summary[customer][item] += qty

# summary = dict(summary)

print(f'\n{summary}\n')

# Для красивого вывода преобразуем во вложенные обычные словари
summary = {customer: dict(items) for customer, items in summary.items()}

print(summary)