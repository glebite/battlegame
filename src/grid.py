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

if __name__ == "__main__":
    print("Executing tests...")
    x = grid()
    assert x.rows == 10
    assert x.cols == 10
    y = grid((5,3))
    assert y.rows == 5
    assert y.cols == 3
    

            
