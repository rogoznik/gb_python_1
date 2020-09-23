a = float(input('Введите число a: '))
b = float(input('Введите число b: '))

num_days = 1
res = a

while res < b:
    print(f'{num_days}-й день: {res}')
    num_days += 1
    res += res * 0.1

print(f'{num_days}-й день: {res}')
print(f'На {num_days}-й день спортсмен достиг результата — не менее {b} км')
