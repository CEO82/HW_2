'''3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года
относится месяц (зима, весна, лето, осень). Напишите решения через list и dict.
'''

while True:
    try:
        month_n = int(input("Please month number from 1 to 12: "))
        if month_n < 1 or month_n > 12:
            print("You are entered wrong month number")
            continue
        break
    except ValueError:
        print("You are entered wrong value, please try again.")

month_lst = ['Jan', 'Feb', 'Mar', 'Apr', 'May', "Jun", 'Jul', "Aug", 'Sep', 'Oct', 'Nov', 'Dec']

if 1 <= month_n <= 2 or month_n == 12:
    year_time = 1
elif 3 <= month_n <= 5:
    year_time = 2
elif 6 <= month_n <= 8:
    year_time = 3
elif 9 <= month_n <= 11:
    year_time = 4

year_time_lst = ('Winter', 'Spring', 'Summer', 'Autumn')

print(f'The number {month_n} month is - {month_lst[month_n - 1]}\nAnd year time is - {year_time_lst[year_time - 1]}')

month_dict = {1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}
year_time_dct = {1:'Winter', 2:'Spring', 3:'Summer', 4:'Autumn'}

print(f'\nThe number {month_n} month is - {month_dict.get(month_n)}\nAnd year time is - {year_time_dct.get(year_time)}')