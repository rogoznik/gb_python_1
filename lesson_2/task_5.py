my_list = [8, 6, 4, 4, 3]

num = int(input('Введите число: '))
is_paste = False

if num <= my_list[-1]:
    my_list.append(num)
    is_paste = True

if not is_paste:
    for i in range(-2, len(my_list)):
        if num <= my_list[i]:
            my_list.insert(i + 1, num)
            is_paste = True
            break

if not is_paste:
    if num > my_list[0]:
        my_list.insert(0, num)

print(my_list)
