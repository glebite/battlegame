"""
grid.py

used to define the grid for the playing field
"""
import os
import logging
import cell

FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
logging.basicConfig(format=FORMAT, level=os.environ.get("LOGLEVEL", "DEBUG"))
LOG = logging.getLogger(__name__)
EMPTY = 0
HIT_SHIP = 1
MISS_SHIP = 2


class GridIncorrectOrientationException(Exception):
    """ if orientation is not proper """

class GridVerticalPlacementException(Exception):
    """ if vertical placement is wrong"""

class GridHorizontalPlacementException(Exception):
    """ if horizontal placement is wrong """

class GridBadSeedLocationException(Exception):
    """ if row/col position are out of bounds of the grid """


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
        LOG.debug("Creating grid and allocating space...")
        if self.rows <= 0 or self.cols <= 0:
            raise ValueError("rows or cols cannot be <= 0")
        grid = [[cell.Cell() for x in range(self.cols)] for y in range(self.rows)]
        return grid

    def create_own_grid(self):
        """ create_own_grid """
        LOG.debug("Creating own grid")
        self.grid = self.create_grid()
        return True

    def get_grid_position(self, row, col):
        """ get_grid_position """
        LOG.debug("Getting grid position row {} col {}", row, col)
        return self.grid[row][col]

    def set_grid_position(self, row, col, value):
        """ set_grid_position """
        LOG.debug("Setting grid position row {} col {} value {}", row, col, value)
        self.grid[row][col] = value
        return True

    def test_place_ship(self, r_pos, c_pos, ship_piece, orientation):
        """
        place_ship

        placement is based on r_pos, c_pos, size of ship_piece, and orientation
                  based on that from that seed point
        """
        LOG.debug("Placing ship: r_pos {}, c_pos {}, ship_piece {}, orientation {}", r_pos, c_pos, ship_piece, orientation)
        allowed_orientations = ['horizontal', 'vertical']
        if orientation in allowed_orientations:
            pass
        else:
            raise GridIncorrectOrientationException()
        if r_pos < 0 or r_pos > self.rows:
            raise GridBadSeedLocationException()
        if c_pos < 0 or c_pos > self.rows:
            raise GridBadSeedLocationException()
        if orientation == "horizontal":
            if c_pos + ship_piece.size > self.cols:
                raise GridHorizontalPlacementException()
        if orientation == "vertical":
            if r_pos + ship_piece.size > self.rows:
                raise GridVerticalPlacementException()
        return True

    def __str__(self):
        """
        __str__ - return a string representation of the grid
        """
        out_string = ""
        for row in range(self.rows):
            for col in range(self.cols):
                out_string += str(self.grid[row][col]) + " "
            out_string += "\n"
        return out_string


def main():
    """ main """

if __name__ == "__main__":
    main()
