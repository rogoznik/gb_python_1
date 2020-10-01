def my_func1(x1, y1):
    return x1 ** y1


def my_func2(x2, y2):
    res = 1
    for i in range(1, abs(y2) + 1):
        res *= x2

    return 1 / res


x = int(input('x = '))
y = int(input('y = '))

print(my_func1(x, y))
print(my_func2(x, y))
