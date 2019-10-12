"""
ship_piece.py
"""
import os
import logging


FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
logging.basicConfig(format=FORMAT, level=os.environ.get("LOGLEVEL", "DEBUG"))
LOG = logging.getLogger(__name__)

class ShipPieceSizeException(Exception):
    """
    ShipPieceSizeException - raised if the size is bad
    """

class ShipPieceNameException(Exception):
    """
    ShipPieceSizeException - raised if the name was empty
    """


class ShipPiece:
    """ class ShipPiece """
    def __init__(self, ship_size=None, ship_name=None):
        """
        __init__ - all of the init goodness that there is to have
        """
        if ship_size <= 0:
            raise ShipPieceSizeException()
        if ship_name is None or len(ship_name) == 0:
            raise ShipPieceNameException()
        self.__size = ship_size
        self.holes = [0 for i in range(0,self.__size)]
        self.__name = ship_name
        LOG.debug("Init %s with size: %s name: %s", self.__class__, ship_size, ship_name)

    @property
    def size(self):
        """ size retrieval """
        return self.__size

    @property
    def name(self):
        """ name retrieval """
        return self.__name

    def still_floating(self):
        """ still_floating """
        if self.holes.count(1) == len(self.holes):
            return False
        else:
            return True

    def percentage_floating(self):
        """ percentage_floating """
        return self.holes.count(1) / float(len(self.holes))


def main():
    """
    main function - for use as a standalone tool
    """
    return True

if __name__ == "__main__":
    main()
