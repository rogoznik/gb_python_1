my_sum = 0

isExit = False

print('Q/q - exit')
while not isExit:
    request = input('Введите числа: ')
    listRequest = request.split()
    for elem in listRequest:
        if elem.upper() == 'Q':
            isExit = True
            break

        my_sum += int(elem)

    print(f'Сумма: {my_sum}')