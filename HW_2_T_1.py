"""1. Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию
type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
а указать явно, в программе.
"""

'''
Data for using in task
thing_1 = 34
thing_2 = 23.5
thing_3 = "Hello"
thing_4 = (5+6J)
thing_5 = ['a', 'e', 45, (5, 5), -45]
thing_6 = (2, 4, 7)
thing_7 = {2, 7, 1, 9, 6}
thing_8 = {'k_1': 222, 'k_2': 333, 'k_3': 444}
thing_9 = False
thing_10 = True
thing_11 = None'''

data_type_list = [34, 23.5, "Hello", (5+6J), ['a', 'e', 45, (5, 5), -45], (2, 4, 7), {2, 7, 1, 9, 6}, {'k_1': 222, 'k_2': 333, 'k_3': 444}, False, True, None]

print(f'Program started! \n')

for data in data_type_list:
    print(f'{data} is {type(data)} type')

print(f'\nProgram finished!')