'''Задача 1:
Найти пересечение двух списков через множество.
Пример:
python
КопироватьРедактировать
a = [1, 2, 3]
b = [2, 3, 4]
# ожидаемый вывод: {2, 3}
'''

a = [1, 4, 6, 7, 2]
b = [2, 5, 8, 9, 10, 4]

set_a = set(a)
set_b = set(b)

crossing = set_a & set_b

print(f'\nThe crossing numbers in lists:\n{a}\nand\n{b}\nis\n{crossing}')