class Matrix:
    def __init__(self, list_of_list):
        self.lst = list_of_list

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row)) for row in self.lst)

    def __add__(self, other):
        res = list()
        for i in range(len(self.lst)):
            res.append(list())
            for j in range(len(self.lst[i])):
                res[i].append(self.lst[i][j] + other.lst[i][j])

        return Matrix(res)


matrix1 = Matrix([[3, 3], [2, 2]])
print(matrix1)
print()
matrix2 = Matrix([[2, 2], [3, 3]])
print(matrix2)
print()
print(matrix1 + matrix2)
