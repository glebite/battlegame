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

@pytest.mark.test_id(2)
def test_player_creation():
    game_obj = Game(name="Bob")
    game_obj.add_player("A")
    assert len(game_obj.return_players()) == 1
    
@pytest.mark.test_id(3)
def test_two_player_creation():
    game_obj = Game(name="Bob")
    game_obj.add_player("A")
    game_obj.add_player("B")
    assert len(game_obj.return_players()) == 2

@pytest.mark.test_id(4)
def test_three_player_creation():
    game_obj = Game(name="Bob")
    game_obj.add_player("A")
    game_obj.add_player("B")
    assert game_obj.add_player("C") == False

@pytest.mark.test_id(5)
def test_three_player_creation_count_check():
    game_obj = Game(name="Bob")
    game_obj.add_player("A")
    game_obj.add_player("B")
    game_obj.add_player("C")
    assert len(game_obj.return_players()) == 2
