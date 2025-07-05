'''Задача 1:
Удалить дубликаты из списка, сохраняя порядок.
Пример:
python
КопироватьРедактировать
lst = [1, 2, 2, 3, 1]
# ожидаемый вывод: [1, 2, 3]
'''

lst = [5, 6, 2, 3, 1, 3, 5, 6, 5, 1, 1, 7]
new_lst = []

for s in lst:
    if s not in new_lst:
        new_lst.append(s)

print(f'\nThe list before changing was - {lst}\nThe list after changing is - {new_lst}')
