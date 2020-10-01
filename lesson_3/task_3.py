def my_func(a, b, c):
    if a <= b <= c or a <= c <= b:
        return b + c
    elif c <= b <= a or c <= a <= b:
        return b + a
    else:
        return a + c


num1 = int(input('a = '))
num2 = int(input('b = '))
num3 = int(input('c = '))

print(my_func(num1, num2, num3))
