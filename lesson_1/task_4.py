num = input('Введите целое положительное число: ')
count = len(num) - 1
digit = 0
idx = 0

while idx <= count:
    tmp_digit = int(num[idx])
    if tmp_digit > digit:
        digit = tmp_digit

    idx += 1

print(f'Самая большая цифра в веденнов числе: {digit}')
