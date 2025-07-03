'''Задача 2:
Проверить, является ли число палиндромом (читается одинаково слева направо и справа налево).
Пример:
python
КопироватьРедактировать
n = 121
# ожидаемый вывод: True
'''


while True:
    try:
        user_number = int(input('Please enter a positive integer number: '))
        if user_number < 0:
            print('You are entered negative number')
            continue
        break
    except ValueError:
        print("You are entered wrong value, please try again.")


user_number_reversed = int(str(user_number)[::-1])

if user_number == user_number_reversed:
    print(f'\nTrue')
else:
    print('\nFalse')

print(f'\nEntered number is {user_number}\nand\nthe reversed number is {user_number_reversed}')