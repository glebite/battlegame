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
    pass

if __name__ == "__main__":
    main()
