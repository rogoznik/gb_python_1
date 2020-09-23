proceeds = float(input('Введите выручку: '))
costs = float(input('Введите издержки: '))

profitability = 0
diff = proceeds - costs

if diff > 0:
    print('Фирма работает в прибыль!')

    profitability = diff / proceeds
    print(f'Рентабельность: {profitability}')
    num_employees = int(input('Введите кол-во сотрудков: '))
    print(f'Прибыль фирмы на одного сотрудника: {diff / num_employees}')
else:
    print('Фирма работает в убыток!')


