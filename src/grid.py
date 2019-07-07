"""
grid.py

"""


class Grid:
    """ class Grid """
    def __init__(self, shape=None):
        """ shape is a tuple """
        self.grid = None
        if shape:
            self.rows = shape[0]
            self.cols = shape[1]
        else:
            self.rows = 10
            self.cols = 10

    def create_grid(self):
        """ create_grid """
        if self.rows <= 0 or self.cols <= 0:
            raise ValueError("rows or cols cannot be <= 0")
        grid = [[0 for x in range(self.cols)] for y in range(self.rows)]
        return grid

    def create_own_grid(self):
        """ create_own_grid """
        self.grid = self.create_grid()
        return True

    def get_grid_position(self, row, col):
        """ get_grid_position """
        return self.grid[row][col]

    def set_grid_position(self, row, col, value):
        """ set_grid_position """
        self.grid[row][col] = value
        return True

def main():
    """ main """
    print("Executing tests...")
    x_obj = Grid()
    assert x_obj.rows == 10, "rows should be 10"
    assert x_obj.cols == 10, "cols should be 10"
    y_obj = Grid((5, 3))
    assert y_obj.rows == 5
    assert y_obj.cols == 3
    assert isinstance(y_obj.create_grid(), list) is True
    z_obj = Grid((-1, 5))
    try:
        assert isinstance(z_obj.create_grid(), list) is True
    except ValueError as e_exception:
        print("Exception raised as expected: {}".format(e_exception))

    assert isinstance(x_obj.create_grid(), list) is True
    assert x_obj.create_own_grid() is True
    assert x_obj.set_grid_position(5, 5, 1) is True
    assert x_obj.get_grid_position(5, 5) == 1
    assert x_obj.get_grid_position(5, 4) == 0

if __name__ == "__main__":
    main()
