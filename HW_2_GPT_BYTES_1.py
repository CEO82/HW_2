'''Задача 1:
Создать bytes из строки и вывести каждый байт как число.
Пример:
python
КопироватьРедактировать
s = "Hi"
# ожидаемый вывод: 72 105
'''

s = "Hi"

s_in_bytes = bytes(s, 'utf-8')

print(s_in_bytes)
print(f'\nThe string \n{s} \nin digital code wil be \n{list(s_in_bytes)}')