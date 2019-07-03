"""
grid.py

"""
import pytest
import logging

class grid:
    def __init__(self, shape=None):
        """ shape is a tuple """
        if shape:
            self.rows = shape[0]
            self.cols = shape[1]
        else:
            self.rows = 10
            self.cols = 10

    def createGrid(self):
        if self.rows <= 0 or self.cols <= 0:
            raise ValueError("rows or cols cannot be <= 0")
        grid = [[0 for x in range(self.cols)]
                      for y in range(self.rows)]
        return grid

    def createBoard(self):
        self.board = self.createGrid()
        return True

    def get_board(self, row, col):
        return self.board[row][col]
    
    def set_board(self, row, col, value):
        self.board[row][col] = value
        return True

            
if __name__ == "__main__":
    print("Executing tests...")
    x = grid()
    assert x.rows == 10
    assert x.cols == 10
    y = grid((5,3))
    assert y.rows == 5
    assert y.cols == 3
    assert isinstance(y.createGrid(), list) == True
    z = grid((-1,5))
    try:
        assert isinstance(z.createGrid(), list) == True
    except ValueError as e:
        print("Exception raised as expected: {}".format(e))

    assert isinstance(x.createGrid(), list) == True
    assert x.createBoard() == True
    assert x.set_board(5,5,1) == True
    assert x.get_board(5,5) == 1
    assert x.get_board(5,4) == 0

