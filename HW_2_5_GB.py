'''5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который
не возрастает. У пользователя нужно запрашивать новый элемент рейтинга. Если в рейтинге
существуют элементы с одинаковыми значениями, то новый элемент с тем же значением
должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
'''

basic_list = [7, 5, 3, 3, 2]
print(f'Basic list is - {basic_list}\n')

while True:
    try:
        user_n = int(input("Please enter positive number: "))
        if user_n < 0:
            print("You are entered negative number, please enter positive")
            continue
        break
    except ValueError:
        print("You are entered wrong value, please try again.")

mx_lst = max(basic_list)
mn_lst = min(basic_list)

if basic_list.count(user_n) > 0:
    if user_n > mx_lst:
        basic_list.insert(0, user_n)
    elif user_n < mn_lst:
        basic_list.append(user_n)
    else:
        basic_list.insert(basic_list.index(user_n), user_n)
else:
    count = 0
    srh_h = user_n
    srh_l = user_n

    while True:
        srh_h += 1
        srh_l -= 1
        if basic_list.count(srh_h) > 0:
            basic_list.insert(basic_list.index(srh_h) + 1, user_n)
            break
        elif basic_list.count(srh_l) > 0:
            basic_list.insert(basic_list.index(srh_l) - 1, user_n)
            break

print(f'\nNew list is: {basic_list}')
