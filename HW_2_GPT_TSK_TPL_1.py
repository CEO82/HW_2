'''Задача 1:
Дан список чисел, вывести кортеж (минимум, максимум, сумма).
Пример:
python
КопироватьРедактировать
lst = [1, 2, 3, 4]
# ожидаемый вывод: (1, 4, 10)
'''

lst = [1, 2, 3, 4]

new_tpl = tuple([min(lst), max(lst), sum(lst)])

print(f'\nThe basic list was {lst}\nAnd new list with smallest, biggest and sum is {new_tpl}')
