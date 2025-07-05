'''Задача 1:
Дана строка, нужно вывести количество уникальных символов.
Пример:
python
КопироватьРедактировать
s = "hello"
# ожидаемый вывод: 4
'''

user_str = input('Please enter any text or digits: ')
unique_symbols_count = 0

for s in user_str:
    if user_str.count(s) == 1:
        unique_symbols_count += 1

print(f'\nNumbers of unique symbols in string {user_str} is {unique_symbols_count}')