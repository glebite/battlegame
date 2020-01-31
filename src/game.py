"""
game.py - got game?
"""
import os
import logging
from player import Player
from enum import Enum

class GameStates(Enum):
    MAX_PLAYERS = 2
    GAME_INITIATION = 1

FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
logging.basicConfig(format=FORMAT, level=os.environ.get("LOGLEVEL", "DEBUG"))
LOG = logging.getLogger(__name__)

class GameMaxPlayersExceeded(Exception):
    """
    MaxPlayersExceeded - exception
    """


class Game:
    """ class Game """

    def __init__(self, name=None):
        """
        __init__ - all of the init goodness
        """
        self.players = list()
        self.game_status = GameStates.GAME_INITIATION
        LOG.debug("Init %s with game_name = %s", self.__class__, name)
        self.game_name = name

    def add_player(self, player_name):
        """
        add_player
        """
        LOG.debug("Adding player %s", player_name)
        if len(self.players) == GameStates.MAX_PLAYERS:
            raise GameMaxPlayersExceeded()
        player_obj = Player(name=player_name)
        self.players.append(player_obj)
        return True

    def return_players(self):
        """
        return_players - will do more
        TODO: do more
        """
        LOG.debug("Returning players...")
        return self.players

    def return_player_info(self, name):
        """
        """
        LOG.debug("Returning a specific player")
        for player_obj in self.players:
            if player_obj.player_name == name:
                return player_obj.get_stats()


def main():
    """ main """
    return True

if __name__ == "__main__":
    main()
