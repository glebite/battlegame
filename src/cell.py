"""
Cell.py
"""

EMPTY = 0
HIT = 1
SHIP = 2
SUNK = 4
MISS = 8


class Cell:
    def __init__(self):
        self.__state = EMPTY
        self.__contains_piece_of_ship = None

    @property
    def state(self):
        """ """
        return self.__state

    @property
    def contains_piece_of_ship(self):
        """ """
        return self.__contains_piece_of_ship

    @state.setter
    def state(self, value):
        self.__state = value

    @contains_piece_of_ship.setter
    def contains_piece_of_ship(self, value):
        self.__contains_piece_of_ship = value
        
    def __str__(self):
        state_dict = {EMPTY: ' ',
                      HIT: 'H',
                      SHIP: 'S',
                      SUNK: '*',
                      MISS: 'M'}
        return state_dict[self.state]

    
def main():
    pass

if __name__ == "__main__":
    main()
