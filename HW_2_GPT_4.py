'''Задача 4: Уникальные элементы
Пусть есть список с повторами. Создай новый список, в котором будут только уникальные элементы (без повторений), сохранив порядок появления.

python
Копировать
Редактировать
input_list = [4, 5, 4, 6, 5, 7]
# Ожидаемый результат: [4, 5, 6, 7]
'''

us_list = [1, 2, 3, 4, 3, 5, 6, 3, 7, 8, 9, 10, 7, 11]
num_list = []

unic_numb_list = list(set(us_list))

print(us_list)
print(f'{unic_numb_list} - The list made with set')

for n in us_list:
    if n in num_list:
        continue
    else:
        num_list.append(n)

print(f'{num_list} - The list made with cycle')