'''Задача 1:
Дан список чисел. Вывести список их квадратов через list comprehension.
Пример:
python
КопироватьРедактировать
numbers = [1, 2, 3, 4]
# ожидаемый вывод: [1, 4, 9, 16]
'''

numbers = [1, 2, 3, 4, 5, 6, 7]

num_squers = [k ** 2 for k in numbers]

print(f'{num_squers}')