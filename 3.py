class Cell:
    def __init__(self, piece):
        self.piece = piece

    def __str__(self):
        return f'{self.piece}'

    def __add__(self, other):
        return Cell(self.piece + other.piece)

    def __sub__(self, other):
       pos = self.piece - other.piece
       if pos > 0:
           return Cell(pos)
       else:
           print('Ошибка!')

    def __mul__(self, other):
        return Cell(self.piece * other.piece)

    def __truediv__(self, other):
        return Cell(self.piece // other.piece)

    def make_order(self, cells_in_row):
        row = ''
        for i in range(self.piece // cells_in_row):
            row += f'{"*" * cells_in_row} \n'
        row += f'{"*" * (self.piece % cells_in_row)}'
        return row


cells2 = Cell(33)
print(cells2.make_order(7))
cells1 = Cell(9)
print(cells1.make_order(3))
print(cells1 - cells2)
print(cells1 + cells2)
print(cells1 * cells2)
print(cells1 / cells2)