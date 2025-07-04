'''Задача 2:
Вычислить, сколько составляет 15% от числа и сколько останется после их вычитания.
Пример:
python
КопироватьРедактировать
num = 200
# ожидаемый вывод:
# 15% от числа: 30.0
# остаток: 170.0
'''


while True:
    try:
        customer_number = float(input(f'\nPlease enter any number: '))
        break
    except ValueError:
        print(f'\nYou are entered not number, please try again')

print(f'\nYour number was {customer_number: .2f}\n15% of your number is {customer_number * 0.15: .2f}\nRemaining of your number is {customer_number - customer_number * 0.15: .2f}')
