from enum import Enum

class Cell(Enum):
    Empty = 1
    Wall = 2
    Start = 3
    End = 4

    def __str__(self):
        if self.value == 1:
            return "V"
        elif self.value == 2:
            return "M"
        elif self.value == 3:
            return "E"
        elif self.value == 4:
            return "S"
        
        

class Labyrinth:
    def __init__(self, n_rows, n_cols):
        self.cells = []
        self.n_rows = n_rows
        self.n_cols = n_cols

        for i in range(n_rows):
            row = []
            for i in range(n_cols):
                row.append(Cell.Empty)

            self.cells.append(row)

        self.cells[0][0] = Cell.Start
        self.cells[n_rows - 1][n_cols - 1] = Cell.End

    def show(self):
        for row in self.cells:
            for cell in row:
                print(cell, end=" | ")
            print()

lab = Labyrinth(4, 22)
print(lab.n_rows)
print(lab.n_cols)
lab.show()