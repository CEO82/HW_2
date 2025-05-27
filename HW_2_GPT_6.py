'''Задача 6: Подсчёт положительных, отрицательных и нулей
Список из чисел. Нужно посчитать и вывести:

Кол-во положительных чисел

Кол-во отрицательных

Кол-во нулей'''

lst_f_chk = [1, -2, 0, 5, -3, 0, 5, -9, 0, 34]

pos_cnt = 0
neg_cnt = 0
zero_cnt = 0

for i in lst_f_chk:
    if i > 0:
        pos_cnt += 1
    elif i < 0:
        neg_cnt += 1
    else:
        zero_cnt += 1

print(f'In the list {lst_f_chk}\n{pos_cnt} - positive numbers\n{neg_cnt} - negative numbers\n{zero_cnt} - zero numbers')