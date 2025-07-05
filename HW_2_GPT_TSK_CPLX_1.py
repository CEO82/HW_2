'''Задача 1:
Создай два комплексных числа и выведи их произведение и деление.
Пример:
python
КопироватьРедактировать
z1 = complex(2, 3)
z2 = complex(1, -1)
'''

while True:
    try:
        real_number_1 = int(input(f'\nPlease enter real number for first complex number: '))

    except ValueError:
        print(f'\nYou are entered not number, please try again')

    try:
        imaginary_number_1 = int(input(f'\nPlease enter imaginary number for first complex number: '))

    except ValueError:
        print(f'\nYou are entered not number, please try again')
    try:
        real_number_2 = int(input(f'\nPlease enter real number for second complex number: '))

    except ValueError:
        print(f'\nYou are entered not number, please try again')
    try:
        imaginary_number_2 = int(input(f'\nPlease enter imaginary number for second complex number: '))
        break
    except ValueError:
        print(f'\nYou are entered not number, please try again')

complex1 = complex(real_number_1, imaginary_number_1)
complex2 = complex(real_number_2, imaginary_number_2)

multiplication = complex1 * complex2
division = complex1 / complex2

print(
    f'\nFirst complex number is {complex1}\nSecond complex number is {complex2}\nMultiplication of two complex numbers is {multiplication}\nDivision of two complex numbers is {division}')
