def fact(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
        yield res


for el in fact(4):
    print(el)
