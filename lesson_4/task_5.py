from functools import reduce

some_list = [i for i in range(100, 1001) if i % 2 == 0]
print(some_list)

def my_f(num1, num2):
    return num1 * num2


print(reduce(my_f, some_list))
