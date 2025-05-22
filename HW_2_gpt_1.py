'''Задача 1: Сумма всех чисел в списке
Пользователь вводит числа через input() и добавляет их в список. После завершения ввода — программа должна вывести сумму всех чисел.

📌 Дополнительно: проверить, что пользователь вводит только числа.'''

print("\nProgram started \n")

user_list = list()

while True:
    try:
        user_numb = int(input("Please enter only positive\ninteger number: "))
        if user_numb <= 0:
            print("You are entered negative number or zero, please enter only positive integer digit!")
            continue

    except ValueError:
        print("You are entered wrong value, please try again.")
        continue

    user_list.append(user_numb)

    yes_no_qest = input('Do you want enter more number to the List? Y or N: ')
    if yes_no_qest.lower() != 'n':
        continue
    else:
        print(f'\nYour List is: {user_list}\n')
        break

num_sum = 0

for i in user_list:
    num_sum = i + num_sum

print(f'Sum of numbers in your list is {num_sum}')

print(f'\nProgram finished!')
