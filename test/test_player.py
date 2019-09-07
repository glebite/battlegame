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

    
