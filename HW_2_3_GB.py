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

print(f'The number {month_n} month is - {month_lst[month_n - 1]}')

month_dict = {1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}

print(f'\nThe number {month_n} month is - {month_dict.get(month_n)}')