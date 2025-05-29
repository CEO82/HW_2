'''4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое
слово с новой строки. Строки нужно пронумеровать. Если слово длинное, выводить только
первые 10 букв в слове.
'''

user_str = 'Mother washed window in abrecadabreplus that is all'
us_lst = user_str.split()

print(f'\n{'*' * 25}\n{'№':<3}{'Word':<10}\n{'*' * 25}')

for index, word in enumerate(us_lst, start=1):
    print(f'{index} - {word.title():<10}')

print(f'{'*' * 25}')
