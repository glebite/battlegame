"""
player.py
"""
from grid import Grid


class Player:
    """ class Player """
    hits = 0
    misses = 0
    enemy_sunk = 0
    mine_sunk = 0

    def __init__(self, name=None):
        """
        __init__ - all of the init goodness
        """
        self.player_name = name
        self.game_grid = Grid()

    def reset_stats(self):
        """
        reset_stats - used to reset the user for another game
        """
        self.hits = 0
        self.misses = 0
        self.enemy_sunk = 0
        self.mine_sunk = 0

    def player_hits(self):
        """
        player_hits - a method to record a hit
        """
        self.hits += 1

    def debug_status(self):
        """
        debug_status - simple logging output for debug usage
        """
        print('Player: {}\n\tHits: {}\n\tMisses: {}\n\t'
              'Enemy Sunk: {}\n\tMine Sunk: {}\n'.
              format(self.player_name, self.hits, self.misses,
                     self.enemy_sunk, self.mine_sunk))

def main():
    """ main """
    return

if __name__ == "__main__":
    main()
