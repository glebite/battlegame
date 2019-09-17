"""
test_game.py

All tests will be in @pytest markup format.

"""
import sys
import pytest
sys.path.append('../src')
from game import Game

@pytest.mark.test_id(1)
def test_game_creation():
    game_obj = Game(name="Bob")
    assert game_obj.game_name == "Bob"
