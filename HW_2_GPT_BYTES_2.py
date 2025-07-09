'''Задача 2:
Создать bytearray из строки, изменить один байт, вывести обратно в строку.
Пример:
python
КопироватьРедактировать
s = "hello"
# изменить первый символ на 'H'
# ожидаемый вывод: "Hello"
'''

user_string = 'привет'

user_string_in_bytes = bytearray(user_string, 'utf-8')
print(f'\nThe code is: {user_string_in_bytes} \nmean: {user_string_in_bytes.decode('utf-8')}')
user_string_in_bytes[0:2] = 'П'.encode('utf-8')

print(f'\nThe code after changing \nis: {user_string_in_bytes}\nAnd it mean: {user_string_in_bytes.decode('utf-8')}')




