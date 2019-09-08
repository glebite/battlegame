"""
test_player.py

All tests will be in @pytest markup format.

"""
import pytest
import sys
sys.path.append('../src')
from player import Player

@pytest.mark.test_id(1)
def test_player_creation():
    player_obj = Player(name="Bob")
    assert player_obj.player_name is "Bob"

@pytest.mark.test_id(2)
def test_player_creation_default():
    player_obj = Player()
    assert player_obj.player_name is None

@pytest.mark.test_id(3)
def test_player_grid_default():
    player_obj = Player()
    assert player_obj.game_grid.rows == 10 and player_obj.game_grid.cols == 10








