'''Задача 6: Объединение списков с фильтрацией
У тебя есть два списка чисел:

python
Копировать
Редактировать
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
📌 Создай третий список, в котором будут только уникальные элементы из обоих списков
(то есть — никаких повторов, даже если они есть и в первом, и во втором списке).

Ожидаемый результат:

python
Копировать
Редактировать
[1, 2, 3, 6, 7, 8]
✅ Дополнительно:

Постарайся сделать решение сначала без использования set, чтобы закрепить навыки.

Потом сделай с использованием set и сравни — какой вариант проще/понятнее.'''
from enum import unique

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8, 8]
prefinal_lst = []
final_lst = []

unique = list((set(list1) ^ set(list2)))

print(unique)

unique_elements = []

for num in list1:
    if num not in list2 and num not in unique_elements:
        unique_elements.append(num)

for num in list2:
    if num not in list1 and num not in unique_elements:
        unique_elements.append(num)

print(f'List with unique elements: {unique_elements}')