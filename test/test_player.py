"""
test_player.py

All tests will be in @pytest markup format.

"""
import sys
import pytest
sys.path.append('../src')
from player import Player

@pytest.mark.test_id(1)
def test_player_creation():
    player_obj = Player(name="Bob")
    assert player_obj.player_name == "Bob"

@pytest.mark.test_id(2)
def test_player_creation_default():
    player_obj = Player()
    assert player_obj.player_name is None

@pytest.mark.test_id(3)
def test_player_grid_default():
    player_obj = Player()
    assert player_obj.game_grid.rows == 10 and player_obj.game_grid.cols == 10

@pytest.mark.test_id(4)
def test_player_initial_stats():
    player_obj = Player()
    assert player_obj.hits == 0 and player_obj.misses == 0 and player_obj.enemy_sunk == 0 and player_obj.mine_sunk == 0

@pytest.mark.test_id(5)
def test_player_hits():
    player_obj = Player()
    player_obj.player_hits()
    assert player_obj.hits == 1 and player_obj.misses == 0 and player_obj.enemy_sunk == 0 and player_obj.mine_sunk == 0

@pytest.mark.test_id(6)
def test_player_reset():
    player_obj = Player()
    player_obj.player_hits()
    player_obj.reset_stats()
    assert player_obj.hits == 0 and player_obj.misses == 0 and player_obj.enemy_sunk == 0 and player_obj.mine_sunk == 0    
