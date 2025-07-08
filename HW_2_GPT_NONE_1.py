'''Задача 1:
Если число отрицательное, вывести None, иначе вывести это число.
Пример:
python
КопироватьРедактировать
n = -5
# ожидаемый вывод: None
'''

n = -5

answer = None if n < 0 else n

print(f'\nThe number is {n} \nAnd result according to task is-> {answer}')