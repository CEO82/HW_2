'''Задача 2:
Вывести элементы кортежа в обратном порядке.
Пример:
python
КопироватьРедактировать
t = (1, 2, 3)
# ожидаемый вывод: (3, 2, 1)
'''

t = (1, 2, 3)
reverse = tuple(list(t)[::-1])

print(f'\nBasic tuple was {t}\nAnd reversed tuple is {reverse}')

