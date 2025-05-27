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

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8, 8]
prefinal_lst = []
final_lst = []

if len(list1) > len(list2):
    main_lst = list2
    second_lst = list1
else:
    main_lst = list1
    second_lst = list2

for i in main_lst:
    if i in second_lst:
        continue
    else:
        prefinal_lst.append(i)

for i in second_lst:
    if i in main_lst:
        continue
    else:
        prefinal_lst.append(i)

for i in prefinal_lst:
    if prefinal_lst.count(i) > 1:
        continue
    else:
        final_lst.append(i)

print(f'List with unique numbers is - {final_lst}')




