'''🔹 Задача 3: Удаление всех вхождений элемента
Пусть у тебя есть список:

python
Копировать
Редактировать
my_list = [1, 2, 3, 2, 4, 2, 5]
Удалить все элементы равные 2.'''

us_lst = [1, 3, 2, 5, 6, 7, 2, 9, 8]

el_to_del = 10
ind_cnt = 0
a = 0

if us_lst.count(el_to_del) < 1:
    a = 1

while us_lst.count(el_to_del) > 0:
    us_lst.pop(us_lst.index(el_to_del))


if a == 1:
    print(f'The element {el_to_del} is not in the list {us_lst}')
else:
    print(f'New list is: {us_lst}')

