"""
test_ship_piece.py

All tests will be in @pytest markup format.

"""
import sys
import pytest
sys.path.append('../src')
from ship_piece import *

@pytest.mark.test_id(1)
def test_ship_piece_creation_name():
    sp_obj = ShipPiece(ship_size=5, ship_name="Bob")
    assert (sp_obj.name == "Bob")

@pytest.mark.test_id(2)
def test_ship_piece_creation_size():
    sp_obj = ShipPiece(ship_size=5, ship_name="Bob")
    assert (sp_obj.size == 5)

@pytest.mark.test_id(3)
def test_ship_piece_creation_size_exception():
    try:
        sp_obj = ShipPiece(ship_size=0, ship_name="Bob")
        assert False
    except ShipPieceSizeException as raised_exception:
        assert True
