'''Задача 5: Переворот списка
Пользователь вводит значения в список. Затем выведи этот список в обратном порядке (не используя .reverse() или [::-1]).'''

my_list = [1, 2, 3, 4, 5, 6, 'r', -7.6]
lst_lnh = len(my_list) #list length
new_lst = []

for v in my_list:
    new_lst.append(my_list[lst_lnh - 1])
    lst_lnh -= 1

print(f'New list is: {new_lst}')
