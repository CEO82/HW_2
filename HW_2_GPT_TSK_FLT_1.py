'''Задача 1:
Есть список чисел с плавающей запятой, нужно вывести их округленные значения до 2 знаков.
Пример:
python
КопироватьРедактировать
nums = [1.123, 3.1415, 2.718]
# ожидаемый вывод: [1.12, 3.14, 2.72]
'''

nums = [1.123, 3.1415, 2.718]
rounded_numbers = []

for n in nums:
    rounded_numbers.append(round(n, 2))

print(f'\nBasic list of numbers was {nums} \nand new list of rounded numbers is {rounded_numbers}')