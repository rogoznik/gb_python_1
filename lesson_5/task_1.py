with open('task1.txt', 'w') as f:
    while True:
        request = input('Введите что-нибудь: ')
        if not request:
            break

        print(request, file=f)
