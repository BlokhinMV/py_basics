class Cell:
    def __init__(self, nucleus):
        self.nucleus = int(nucleus)

    def __str__(self):
        return f'Полученная клетка: ({self.nucleus * "*"})'
    def __add__(self, other):
        return Cell(self.nucleus + other.nucleus)
    def __sub__(self, other):
        return Cell(self.nucleus - other.nucleus) if (self.nucleus > other.nucleus) else print ('Невозможно выполнить вычитание')
    def __mul__(self, other):
        return Cell(self.nucleus * other.nucleus)
    def __truediv__(self, other):
        return Cell(round(self.nucleus // other.nucleus))
    def make_order(self, nucl_in_row):
        string = 'Упорядоченная клетка:\n('
        for i in range(self.nucleus // nucl_in_row):
            string += f'{nucl_in_row * "*"}\n'
        string += f'{(self.nucleus % nucl_in_row) * "*"})'
        return string

cell1 = Cell(48)
cell2 = Cell(9)
print(cell1)
print(cell1 + cell2)
print(cell1 - cell2)
cell3 = cell1 * cell2
print(cell3)
print(cell1 / cell2)
print(cell3.make_order(100))