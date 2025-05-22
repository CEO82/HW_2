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

user_list = [11, 22, 33, 44]

limit = len(user_list) - 1 if len(user_list) % 2 != 0 else len(user_list)

# Меняем местами элементы парами: 0-1, 2-3, и т.д.
for i in range(0, limit, 2):
    user_list[i], user_list[i + 1] = user_list[i + 1], user_list[i]

print(f'List after change: {user_list}')