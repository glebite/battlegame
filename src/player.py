"""
player.py
"""
import os
import logging
import json
from grid import Grid

FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
logging.basicConfig(format=FORMAT, level=os.environ.get("LOGLEVEL", "DEBUG"))
LOG = logging.getLogger(__name__)


class Player:
    """ 
    class Player

    Essentially there will be two players created - each with
    their own view of a grid - the game grid where their ships are 
    and recording hits.  As well, the view grid where the player can
    see where they scored a hit on the enemy or a miss to remove the
    position from selection in the future or an automated attack.
    """
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
        self.view_grid = Grid()

    def reset_stats(self):
        """
        reset_stats - used to reset the user for another game
        """
        LOG.debug("player_name = %s", self.player_name)

        self.my_hits = 0
        self.my_misses = 0
        self.enemy_sunk = 0
        self.mine_sunk = 0

    def get_stats(self):
        """
        get_stats - returns a json artifact with the stats
        """
        string_response= json.dumps({'name': self.player_name,
                                     'hits': self.my_hits,
                                     'misses': self.my_misses,
                                     'sunk': self.enemy_sunk,
                                     'my_sunk': self.mine_sunk})
        return json.loads(string_response)

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
        LOG.debug("Place ship %s", ship_piece)
        return ship_piece

    def out_view_grid(self):
        """
        out_view_grid - for now prints out the view_grid
        """
        LOG.debug("Output of grid: %s", self.view_grid)
        return self.view_grid

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
