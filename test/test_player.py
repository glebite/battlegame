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
    assert player_obj.my_hits == 0 and player_obj.my_misses == 0 and player_obj.enemy_sunk == 0 and player_obj.mine_sunk == 0

@pytest.mark.test_id(5)
def test_player_hits():
    player_obj = Player()
    player_obj.hits()
    assert player_obj.my_hits == 1 and player_obj.my_misses == 0 and player_obj.enemy_sunk == 0 and player_obj.mine_sunk == 0

@pytest.mark.test_id(6)
def test_player_reset():
    player_obj = Player()
    player_obj.hits()
    player_obj.reset_stats()
    assert player_obj.my_hits == 0 and player_obj.my_misses == 0 and player_obj.enemy_sunk == 0 and player_obj.mine_sunk == 0    

@pytest.mark.test_id(7)
def test_player_misses():
    player_obj = Player()
    player_obj.misses()
    assert player_obj.my_hits == 0 and player_obj.my_misses == 1 and player_obj.enemy_sunk == 0 and player_obj.mine_sunk == 0

@pytest.mark.test_id(7)
def test_player_sinks_enemy():
    player_obj = Player()
    player_obj.sinks_enemy()
    assert player_obj.my_hits == 0 and player_obj.my_misses == 0 and player_obj.enemy_sunk == 1 and player_obj.mine_sunk == 0

@pytest.mark.test_id(8)
def test_player_grid_default():
    player_obj = Player()
    assert player_obj.view_grid.rows == 10 and player_obj.view_grid.cols == 10

@pytest.mark.test_id(9)
def test_player_place_ship():
    player_obj = Player()
    assert player_obj.place_ship("hornblower") == "hornblower"

@pytest.mark.test_id(10)
def test_player_string_test():
    player_obj = Player()
    assert str(player_obj) == "Player: None\n\tHits: 0\n\tMisses: 0\n\tEnemy Sunk: 0\n\tMine Sunk: 0\n"

@pytest.mark.test_id(11)
def test_player_string_test_name():
    player_obj = Player("binkie")
    assert str(player_obj) == "Player: binkie\n\tHits: 0\n\tMisses: 0\n\tEnemy Sunk: 0\n\tMine Sunk: 0\n"

@pytest.mark.test_id(12)
def test_player_string_test_hit():
    player_obj = Player("binkie")
    player_obj.hits()
    assert str(player_obj) == "Player: binkie\n\tHits: 1\n\tMisses: 0\n\tEnemy Sunk: 0\n\tMine Sunk: 0\n"
