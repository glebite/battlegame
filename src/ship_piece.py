"""
ship_piece.py
"""
import os
import logging

FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
logging.basicConfig(format=FORMAT, level=os.environ.get("LOGLEVEL", "DEBUG"))
LOG = logging.getLogger(__name__)


class ShipPiece:
    """ class ShipPiece """
    def __init__(self, size, name):
        """
        __init__ - all of the init goodness that there is to have
        """
        self.__size = size
        self.__name = name
        LOG.debug("Init %s with size: %s name: %s", self.__class__, size, name)

    @property
    def size(self):
        """ size retrieval """
        return self.__size

    @property
    def name(self):
        """ name retrieval """
        return self.__name


def main():
    """
    main function - for use as a standalone tool
    """
    return True

if __name__ == "__main__":
    main()
