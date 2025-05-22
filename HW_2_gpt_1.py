'''Задача 1: Сумма всех чисел в списке
Пользователь вводит числа через input() и добавляет их в список. После завершения ввода — программа должна вывести сумму всех чисел.

📌 Дополнительно: проверить, что пользователь вводит только числа.'''
from HW_2_T_2_gpt_variant import user_list

print("\nProgram started \n")

user_list = list()

while True:
    try:
        user_numb = int(input("Please enter only positive\ninteger number: "))
        if user_numb <= 0:
            print("You are entered negative number or zero, please enter only positive integer digit!")
            continue
        break
    except ValueError:
        print("You are entered wrong value, please try again.")
        continue

    user_list.append(user_numb)
    print(user_list)




    break