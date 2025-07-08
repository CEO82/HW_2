'''Задача 2:
Если строка не содержит цифр, вывести None, иначе вывести количество цифр в строке.
Пример:
python
КопироватьРедактировать
s = "abc123"
# ожидаемый вывод: 3
'''

user_string = 'abcd5efg1kl'

is_string_has_digit = any(s.isdigit() for s in user_string)
digits_count = 0 #this is for counting digits in user_string, if string does not have digits it will turns to None

if is_string_has_digit == True:
    for d in user_string:
        if d.isdigit():
            digits_count += 1
    print(f'\nTne string ->{user_string}<- has {digits_count} digits')
else:
    digits_count = None
    print(f'\nTne string ->{user_string}<- has {digits_count} digits')

