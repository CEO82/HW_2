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


user_list = [22, 33, 44, 55, 66, 77] # delet after tests
print(user_list) # delet after tests

list_lenth = len(user_list)

if list_lenth % 2 != 0:
    even_chk = 'non_even'
else:
    even_chk = 'even'

if even_chk == 'non_even':
    counter = list_lenth - 1
else:
    counter = list_lenth

ind_2 = 1
ind_1 = 0
counter -= 1

while counter > 0:
    user_list.insert(ind_1, user_list[ind_2])
    print(f'list after swap {user_list}')  # delet after tests

    user_list.pop(ind_2 + 1)

    ind_2, ind_1 = ind_2 + 2, ind_1 + 2
    counter -= 1