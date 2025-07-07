'''Задача 1:
Определить, есть ли в списке отрицательные элементы, и вывести True или False.
Пример:
python
КопироватьРедактировать
lst = [1, -2, 3]
# ожидаемый вывод: True
'''

lst = [1, -3, 4, 5]

check = any(n < 0 for n in lst)

print(f'\nLet check is in list {lst} negative number? \nAnd answer is {check}')