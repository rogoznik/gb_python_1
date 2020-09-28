count_goods = int(input('ВВедите кол-во товаров: '))

list_goods = []
analytics = {
    'название': [],
    'цена': [],
    'количество': [],
    'ед': []
}

i = 1
while i <= count_goods:
    name_good = input('Введите название товара: ')
    price_good = float(input('Введите цену товара: '))
    count_good = int(input('Введите кол-во товара: '))
    units_good = input('Введите ед. изм. товара: ')

    good = (i, {
        'название': name_good,
        'цена': price_good,
        'количество': count_good,
        'ед': units_good
    })

    list_goods.append(good)

    i += 1

for elem in list_goods:
    for key in analytics:
        analytics[key].append(elem[1][key])

print(analytics)
