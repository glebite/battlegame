"""
player.py
"""
import os
import logging
from grid import Grid

FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
logging.basicConfig(format=FORMAT, level=os.environ.get("LOGLEVEL", "DEBUG"))
LOG = logging.getLogger(__name__)


class Player:
    """ class Player """
    my_hits = 0
    my_misses = 0
    enemy_sunk = 0
    mine_sunk = 0

    def __init__(self, name=None):
        """
        __init__ - all of the init goodness
        """
        LOG.debug("Init %s with player_name = %s", self.__class__, name)
        self.player_name = name
        self.game_grid = Grid()

    def reset_stats(self):
        """
        reset_stats - used to reset the user for another game
        """
        LOG.debug("player_name = %s", self.player_name)

        self.my_hits = 0
        self.my_misses = 0
        self.enemy_sunk = 0
        self.mine_sunk = 0

    def hits(self):
        """
        player_hits - a method to record a hit
        """
        self.my_hits += 1
        LOG.debug("player_hits = %s", self.my_hits)

    def misses(self):
        """
        player_misses - a method to record a miss
        """
        self.my_misses += 1
        LOG.debug("player_misses = %s", self.my_misses)

    def sinks_enemy(self):
        """
        player - just in case we sink an enemy
        """
        self.enemy_sunk += 1
        LOG.debug("player_sinks_enemy = %s", self.enemy_sunk)

    def place_ship(self, ship_piece):
        """
        place_ship - places a ship piece in the grid
        TODO: fill in the blanks - define ship_piece object
        """
        pass

    def __rpr__(self):
        """
        __rpr__ internal state dump
        """
        return "%s(%r)" % (self.__class__, self.__dict__)

    def __str__(self):
        """
        __str__ representation of the player
        """
        return('Player: {}\n\tHits: {}\n\tMisses: {}\n\t'
               'Enemy Sunk: {}\n\tMine Sunk: {}\n'.
               format(self.player_name, self.my_hits, self.my_misses,
                      self.enemy_sunk, self.mine_sunk))

def main():
    """ main """
    return

if __name__ == "__main__":
    main()
