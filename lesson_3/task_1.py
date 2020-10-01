def div(dividend, divider):
    try:
        res = dividend / divider
        return res
    except ZeroDivisionError:
        return 'Ошибка: Деление на 0'


a = int(input('Введите a: '))
b = int(input('Введите b: '))

print(div(a, b))
