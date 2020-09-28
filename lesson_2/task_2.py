count = int(input('Введите кол-во элементов списка: '))

my_list = []
for i in range(count):
    my_list.append(input(f'Введите {i} элемент списка: '))

print('Ваш список:', my_list)

k = 0
while k < (len(my_list) - 1):
    my_list[k], my_list[k + 1] = my_list[k + 1], my_list[k]
    k += 2

print('Список с переставленными элементами:', my_list)
