'''Задача 2: Максимум и минимум
Создай список чисел (можно задать вручную), а затем:

Выведи на экран максимальное и минимальное значения.

Укажи позиции (индексы), где они находятся.'''

us_lst = [44, 11, 2, 4, 55, 49, 15, 88]

max_d = 0
min_d = 0

for i in range(len(us_lst) - 1):
    if us_lst[i] > us_lst[i +1] and us_lst[i] > max_d:
        max_d = us_lst[i]
    elif us_lst[i] < us_lst[i +1] and us_lst[i] < max_d:
        min_d = us_lst[i]

print(f'biggest number is {max_d} and smallest {min_d}')
