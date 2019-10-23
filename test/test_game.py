"""
test_game.py

All tests will be in @pytest markup format.

"""
import sys
import pytest
sys.path.append('../src')
from game import *

@pytest.mark.test_id(1)
def test_game_creation():
    game_obj1 = Game(name="Bob")
    assert game_obj1.game_name == "Bob"

@pytest.mark.test_id(2)
def test_player_creation():
    game_obj2 = Game(name="Bob2")
    game_obj2.add_player("A")
    assert len(game_obj2.return_players()) == 1
    
@pytest.mark.test_id(3)
def test_two_player_creation():
    game_obj3 = Game(name="Bob3")
    game_obj3.add_player("C")
    game_obj3.add_player("D")
    assert len(game_obj3.return_players()) == MAX_PLAYERS
    
@pytest.mark.test_id(4)
def test_three_player_creation():
    game_obj4 = Game(name="Bob4")
    game_obj4.add_player("E")
    game_obj4.add_player("F")
    try:
        game_obj4.add_player("G")
        assert False
    except GameMaxPlayersExceeded as raised_exception:
        print("Hey - hit exception...")
        assert True    

@pytest.mark.test_id(5)
def test_three_player_creation_count_check():
    game_obj = Game(name="Bob")
    game_obj.add_player("A")
    game_obj.add_player("B")
    try:
        game_obj.add_player("C")
    except GameMaxPlayersExceeded as raised_exception:
        assert len(game_obj.return_players()) == MAX_PLAYERS
        
@pytest.mark.test_id(6)
def test_player_name():
    game_obj = Game(name="Bob")
    game_obj.add_player("A")
    assert game_obj.players[0].player_name == "A"

@pytest.mark.test_id(7)
def test_game_creation_status():
    game_obj = Game(name="Bob")
    assert game_obj.game_status == GAME_INITIATION

@pytest.mark.test_id(8)
def test_player_stats():
    game_obj = Game(name="Bob")
    game_obj.add_player("A")
    assert game_obj.return_player_info("A")['name'] == "A"
    
