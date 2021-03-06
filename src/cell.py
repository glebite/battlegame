"""
Cell.py
"""
from enum import Enum

class States(Enum):
    EMPTY = 0
    HIT = 1
    SHIP = 2
    SUNK = 4
    MISS = 8

    
class Cell:
    """ Cell - one entry in the grid"""
    def __init__(self):
        self.__state = States.EMPTY
        self.__contains_piece_of_ship = None

    @property
    def state(self):
        """ state """
        return self.__state

    @property
    def contains_piece_of_ship(self):
        """ contains_piece_of_ship """
        return self.__contains_piece_of_ship

    @state.setter
    def state(self, value):
        self.__state = value

    @contains_piece_of_ship.setter
    def contains_piece_of_ship(self, value):
        self.__contains_piece_of_ship = value

    def __str__(self):
        state_dict = {States.EMPTY: '.',
                      States.HIT: 'H',
                      States.SHIP: 'S',
                      States.SUNK: '*',
                      States.MISS: 'M'}
        return state_dict[self.state]


def main():
    """ nonce function - does nothing for now... """


if __name__ == "__main__":
    main()
