'''4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое
слово с новой строки. Строки нужно пронумеровать. Если слово длинное, выводить только
первые 10 букв в слове.
'''

user_str = 'Mother washed window in abrecadabreplus that is all'
us_lst = user_str.split()

for i in us_lst:
    print(f'{i.title():.10}')