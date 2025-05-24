'''Задача 2: Максимум и минимум
Создай список чисел (можно задать вручную), а затем:

Выведи на экран максимальное и минимальное значения.

Укажи позиции (индексы), где они находятся.'''

us_lst = [-6, 44, 11, 2, 4, 55, -1, 49, 500, 15, 100, 88, -5, 200, 700]

max_d = us_lst[0]
min_d = us_lst[0]
max_ind = 0
min_ind = 0

for i in range(len(us_lst)):
    if us_lst[i] > max_d:
        max_d = us_lst[i]
        max_ind = i
    if us_lst[i] < min_d:
        min_d = us_lst[i]
        min_ind = i

print(f'biggest number is: {max_d} with index: {max_ind}\nand smallest is: {min_d} with index: {min_ind}')
