"""
grid.py

"""


class grid:
    def __init__(self, shape=None):
        """ shape is a tuple """
        self.grid = None
        if shape:
            self.rows = shape[0]
            self.cols = shape[1]
        else:
            self.rows = 10
            self.cols = 10

    def createGrid(self):
        if self.rows <= 0 or self.cols <= 0:
            raise ValueError("rows or cols cannot be <= 0")
        grid = [[0 for x in range(self.cols)] for y in range(self.rows)]
        return grid

    def createOwnGrid(self):
        self.grid = self.createGrid()
        return True

    def get_grid_position(self, row, col):
        return self.grid[row][col]

    def set_grid_position(self, row, col, value):
        self.grid[row][col] = value
        return True


if __name__ == "__main__":
    print("Executing tests...")
    x = grid()
    assert x.rows == 10, "rows should be 10"
    assert x.cols == 10, "cols should be 10"
    y = grid((5, 3))
    assert y.rows == 5
    assert y.cols == 3
    assert isinstance(y.createGrid(), list) is True
    z = grid((-1, 5))
    try:
        assert isinstance(z.createGrid(), list) is True
    except ValueError as e:
        print("Exception raised as expected: {}".format(e))

    assert isinstance(x.createGrid(), list) is True
    assert x.createOwnGrid() is True
    assert x.set_grid_position(5, 5, 1) is True
    assert x.get_grid_position(5, 5) == 1
    assert x.get_grid_position(5, 4) == 0
