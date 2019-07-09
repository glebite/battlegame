"""
Cells.py
"""
import enum


class Cells(enum.Enum):
    """ enumeration holder for Cell values """
    empty = 0
    miss = 1
    hit = 2
    carrier = 4
    battleship = 8
    cruiser = 16
    submarine = 32
    destroyer = 64

def main():
    pass

if __name__ == "__main__":
    main()
