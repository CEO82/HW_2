'''2. Для списка реализовать обмен значений соседних элементов. Значениями обмениваются
элементы с индексами 0 и 1, 2 и 3 и т. д. При нечётном количестве элементов последний
сохранить на своём месте. Для заполнения списка элементов нужно использовать функцию
input().
'''

print(f'Program started \n')

print(
    f'You need to create the List of data, for add new data to the List press Y, to finish filling the List press N \n')

user_list = list()

while True:
    yes_no_qest = input('Do you want enter new data to the List? Y or N: ')
    if yes_no_qest.lower() != 'n':
        user_list.append(input('Please enter any value: '))
        print(user_list)
        continue
    else:
        print(f'\nYour List is: {user_list}\n')
        break

counter = ((len(user_list) - 1) / 2) if len(user_list) % 2 != 0 else len(user_list) / 2

ind_2 = 1
ind_1 = 0

while counter > 0:
    user_list.insert(ind_1, user_list[ind_2])

    user_list.pop(ind_2 + 1)

    ind_2, ind_1 = ind_2 + 2, ind_1 + 2
    counter -= 1

print(f'List after change {user_list}')
