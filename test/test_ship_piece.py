"""
test_ship_piece.py

All tests will be in @pytest markup format.

"""
import sys
import pytest
sys.path.append('../src')
from ship_piece import ShipPiece

@pytest.mark.test_id(1)
def test_ship_piece_creation():
    sp_obj = ShipPiece(size=5, name="Bob")
    assert sp_obj.name == "Bob" and sp_obj.size == 5
