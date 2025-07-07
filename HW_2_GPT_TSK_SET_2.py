'''Задача 2:
Удалить из множества все элементы меньше 5.
Пример:
python
КопироватьРедактировать
s = {1, 3, 5, 7, 9}
# ожидаемый вывод: {5, 7, 9}
'''

s = {1, 3, 5, 7, 9}
print(f'\nThe basic set was {s}')

for v in s.copy():
    if v < 5:
        s.discard(v)

print(f'\nThe set where all numbers are greater than 5 is {s}')
