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
        self.board = [[0 for x in range(self.cols)]
                      for y in range(self.rows)]
        return True
            
if __name__ == "__main__":
    print("Executing tests...")
    x = grid()
    assert x.rows == 10
    assert x.cols == 10
    y = grid((5,3))
    assert y.rows == 5
    assert y.cols == 3
    assert y.createGrid() == True
    z = grid((-1,5))
    try:
        assert z.createGrid() == True
    except ValueError as e:
        print("Exception raised as expected: {}".format(e))
    
    
    

            
