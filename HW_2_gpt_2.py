'''Задача 2: Максимум и минимум
Создай список чисел (можно задать вручную), а затем:

Выведи на экран максимальное и минимальное значения.

Укажи позиции (индексы), где они находятся.'''

us_lst = [300, -6, 44, 11, 2, 4, 55, -1, 49, 15, 100, 88, -5, 200]

if us_lst[0] > us_lst[1]:
    max_d = us_lst[0]
    min_d = us_lst[1]
    max_ind = 0
    min_ind = 1
else:
    max_d = us_lst[1]
    min_d = us_lst[0]
    max_ind = 1
    min_ind = 0

for i in range(len(us_lst) - 1):
    value_i = us_lst[i]
    value_i_plus = us_lst[i + 1]
    if us_lst[i] > us_lst[i + 1] and us_lst[i] > max_d:
        max_d = us_lst[i]
        max_ind = i
    elif us_lst[i] < us_lst[i + 1] and us_lst[i + 1] > max_d:
        max_d = us_lst[i + 1]
        max_ind = i + 1

    if us_lst[i] < us_lst[i + 1] and us_lst[i] < min_d:
        min_d = us_lst[i + 1]
        min_ind = i
    elif us_lst[i] > us_lst[i + 1] and us_lst[i + 1] < min_d:
        min_d = us_lst[i + 1]
        min_ind = i + 1


print(f'biggest number is: {max_d} with index: {max_ind}\nand smallest is: {min_d} with index: {min_ind}')
