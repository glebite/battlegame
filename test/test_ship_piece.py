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

@pytest.mark.test_id(4)
def test_ship_piece_creation_name_exception_zero():
    try:
        sp_obj = ShipPiece(ship_size=2, ship_name="")
        assert False
    except ShipPieceNameException as raised_exception:
        assert True

@pytest.mark.test_id(5)
def test_ship_piece_creation_name_exception_none():
    try:
        sp_obj = ShipPiece(ship_size=2)
        assert False
    except ShipPieceNameException as raised_exception:
        assert True        

@pytest.mark.test_id(6)
def test_ship_piece_creation_hole_size():
    sp_obj = ShipPiece(ship_size=2, ship_name="destroyer")
    assert len(sp_obj.holes) == 2

@pytest.mark.test_id(7)
def test_ship_still_floating_default():
    sp_obj = ShipPiece(ship_size=2, ship_name="minnow")
    assert sp_obj.still_floating() == True

@pytest.mark.test_id(8)
def test_ship_still_floating_filled():
    sp_obj = ShipPiece(ship_size=1,ship_name="tug")
    sp_obj.holes[0] = 1
    assert sp_obj.still_floating() == False

@pytest.mark.test_id(9)
def test_ship_floating_percent_default():
    sp_obj = ShipPiece(ship_size=4,ship_name="submarine")
    assert sp_obj.percentage_floating() == 0.0

@pytest.mark.test_id(10)
def test_ship_floating_percent_fifty():
    sp_obj = ShipPiece(ship_size=4,ship_name="submarine")
    sp_obj.holes[1] = 1
    sp_obj.holes[2] = 1
    assert sp_obj.percentage_floating() == 0.5
