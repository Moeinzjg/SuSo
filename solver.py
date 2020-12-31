'''
Aims at solving any given sudoku puzzel with 3x3 boxes.
'''
import numpy as np


PUZZLE = np.array([[5, 3, 0, 0, 7, 0, 0, 0, 0],
                   [6, 0, 0, 1, 9, 5, 0, 0, 0],
                   [0, 9, 8, 0, 0, 0, 0, 6, 0],
                   [8, 0, 0, 0, 6, 0, 0, 0, 3],
                   [4, 0, 0, 8, 0, 3, 0, 0, 1],
                   [7, 0, 0, 0, 2, 0, 0, 0, 6],
                   [0, 6, 0, 0, 0, 0, 2, 8, 0],
                   [0, 0, 0, 4, 1, 9, 0, 0, 5],
                   [0, 0, 0, 0, 8, 0, 0, 7, 9]], dtype=np.int16) 
                   

class SudokuSolver:
    '''a class to solve and draw a given 9x9 sudoku'''
    def __init__(self, puzzle: np.array) -> None:
        self.puzzle = puzzle
        self.value_cell = 0

    def draw(self) -> None:
        print(self.puzzle)

    def check_row(self, row: int, val: int) -> bool:
        if val in self.puzzle[row,:]:
            return False
        else:
            return True

    def check_col(self, col: int, val: int) -> bool:
        if val in self.puzzle[:,col]:
            return False
        else:
            return True
    
    def check_box(self, row: int, col: int, val: int) -> bool:
        row_box = row // 3 * 3     # first row of the box
        col_box = col // 3 * 3     # first column of the box
        if val in self.puzzle[row_box : row_box+3,col_box : col_box+3]:
            return False
        else:
            return True 
    
    def is_valid(self, row: int, col: int) -> bool:
        cond1 = self.check_row(row, self.value_cell)
        cond2 = self.check_col(col, self.value_cell)
        cond3 = self.check_box(row, col, self.value_cell)
        answer = cond1 and cond2 and cond3
        return answer  

    def solve(self) -> bool:
        '''
        Solves a given sudoku where empty squares are filled with 0s
        '''
        if not 0 in self.puzzle:
            return True
        else:
            empty_rows , empty_cols = np.where(self.puzzle == 0)
            row_cell, col_cell = empty_rows[0], empty_cols[0]
            for self.value_cell in range(1, 10):
                if self.is_valid(row_cell, col_cell):
                    self.puzzle[row_cell, col_cell] = self.value_cell

                    if self.solve():
                        return True

                    self.puzzle[row_cell, col_cell] = 0
        return False


solver = SudokuSolver(PUZZLE)
solver.solve()
solver.draw()