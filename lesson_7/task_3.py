class Cell:
    def __init__(self, num_of_cells):
        self.num_of_cells = num_of_cells

    def __add__(self, other):
        res = self.num_of_cells + other.num_of_cells

        return Cell(res)

    def __sub__(self, other):
        res = self.num_of_cells - other.num_of_cells

        if res > 0:
            return Cell(res)
        else:
            return 'Ошибка: не возможно выполнить операцию'

    def __mul__(self, other):
        res = self.num_of_cells * other.num_of_cells

        return Cell(res)

    def __truediv__(self, other):
        res = round(self.num_of_cells / other.num_of_cells)

        return Cell(res)

    def make_order(self, cell, num_of_cells_in_row):
        res = ''
        for i in range(cell.num_of_cells // num_of_cells_in_row):
            res += '*' * num_of_cells_in_row + '\n'

        res += '*' * (cell.num_of_cells % num_of_cells_in_row)

        return res.strip()


cell1 = Cell(12)
print(cell1.make_order(cell1, 5))

cell2 = Cell(2)
cell3 = Cell(2)
print((cell2 + cell3).num_of_cells)
res = cell2 - cell3
print(res.num_of_cells if isinstance(res, Cell) else res)
print((cell2 * cell3).num_of_cells)
print((cell2 / cell3).num_of_cells)
