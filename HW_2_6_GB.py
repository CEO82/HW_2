'''6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два
элемента — номер товара и словарь с параметрами, то есть характеристиками товара:
название, цена, количество, единица измерения. Структуру нужно сформировать программно,
запросив все данные у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Нужно собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ —
характеристика товара, например, название. Тогда значение — список
значений-характеристик, например, список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
'''

# tuple_lst = [(1, {})] # В списке должны быть кортежи а в кортежах порядковый номер и словарь с характеристиками товаров.

tpl_cnt_nmb = 0  # Tuple counter
tpls_lst = []  # List of Tuples

while True:
    tpl_cnt_nmb += 1
    # it_name = {'Name' : input('Please enter item name: ')}
    dct_fr_tpl = {'Name': input('Please enter item name: ')}  # #Dictionary for Tuple

    while True:
        try:
            it_price = int(input("Please enter item price: "))
            if it_price < 0:
                print("You are entered negative price, please enter positive price: ")
                continue
            break
        except ValueError:
            print("You are entered wrong value, please try again.")
    it_price = {'Price': it_price}
    dct_fr_tpl.update(it_price)

    while True:
        try:
            it_quantity = int(input("Please enter item it_quantity: "))
            if it_quantity < 0:
                print("You are entered negative it_quantity, please enter positive it_quantity: ")
                continue
            break
        except ValueError:
            print("You are entered wrong value, please try again.")

    it_quantity = {'Quantity': it_quantity}
    dct_fr_tpl.update(it_quantity)
    it_units = {'Units': 'pcs'}
    dct_fr_tpl.update(it_units)
    basic_tuple = (tpl_cnt_nmb, dct_fr_tpl)

    y_n_check = str(input(
        'If you want to continue entering data please enter any value,\nif you want finish entering data please enter N or n : '))

    tpls_lst.append(basic_tuple)

    if y_n_check.lower() == 'n':
        break


analitic_dct = {}
name_lst = []
prc_lst = []
qnt_lst = []
unt_lst = []

for i in tpls_lst:

    i_dct = i[1]
    name_lst.append(i_dct.get('Name'))
    prc_lst.append(i_dct.get('Price'))
    qnt_lst.append(i_dct.get('Quantity'))
    unt_lst.append(i_dct.get('Units'))

analitic_dct['Name'] = name_lst
analitic_dct['Price'] = prc_lst
analitic_dct['Quantity'] = qnt_lst
analitic_dct['Units'] = unt_lst

print(f'\nThe Analitic dictionary wil be:\n{analitic_dct}')
