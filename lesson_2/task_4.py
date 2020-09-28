user_str = input('Введите слова разделяя их пробелом: ')
list_of_user_str = user_str.split()

for elem in list_of_user_str:
    if len(elem) <= 10:
        print(elem)
    else:
        print(elem[:10])
