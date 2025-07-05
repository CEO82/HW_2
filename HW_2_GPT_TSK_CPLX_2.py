'''Задача 2:
Вывести модуль комплексного числа с помощью abs().
Пример:
python
КопироватьРедактировать
z = complex(3, 4)
# ожидаемый вывод: 5.0
'''

import math

while True:
    try:
        real_number_1 = float(input(f'\nPlease enter real number for complex number: '))
        break
    except ValueError:
        print(f'\nYou are entered not number, please try again')

while True:
    try:
        imaginary_number_1 = float(input(f'\nPlease enter imaginary number for complex number: '))
        break
    except ValueError:
        print(f'\nYou are entered not number, please try again')

user_complex_number = complex(real_number_1, imaginary_number_1)

print(f'\nYour complex number is {user_complex_number}\nModulus of your complex number is {abs(user_complex_number): .2f}')