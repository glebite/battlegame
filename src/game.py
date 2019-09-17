"""
game.py - got game?
"""
import os
import logging
from player import Player

FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
logging.basicConfig(format=FORMAT, level=os.environ.get("LOGLEVEL", "DEBUG"))
LOG = logging.getLogger(__name__)


class Game:
    """ class Game """
    players = list()
    def __init__(self, name=None):
        """
        __init__ - all of the init goodness
        """
        LOG.debug("Init %s with game_name = %s", self.__class__, name)
        self.game_name = name

    def add_player(self, player_name):
        """
        add_player
        """
        if len(self.players) == 2:
            return False
        player_obj = Player(name=player_name)
        self.players.append(player_obj)
        return True

    def return_players(self):
        """
        return_players - will do more
        TODO: do more
        """
        return self.players

def main():
    """ main """
    return True

if __name__ == "__main__":
    main()
