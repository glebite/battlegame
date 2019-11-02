"""
test_cell.py

All tests will be in @pytest markup format.

"""
import pytest
import sys
sys.path.append('../src')
from cell import *

@pytest.mark.test_id(1)
def test_cell_creation():
    x_obj = Cell()
    assert x_obj is not None

@pytest.mark.test_id(2)
def test_cell_creation_value():
    x_obj = Cell()
    assert x_obj.state == 0 and x_obj.contains_piece_of_ship == None

@pytest.mark.test_id(3)
def test_state_output_empty():
    x_obj = Cell()
    x_obj.state = EMPTY
    assert x_obj.__str__() == ' '

@pytest.mark.test_id(4)
def test_state_output_hit():
    x_obj = Cell()
    x_obj.state = HIT
    assert x_obj.__str__() == 'H'

@pytest.mark.test_id(5)
def test_state_output_ship():
    x_obj = Cell()
    x_obj.state = SHIP
    assert x_obj.__str__() == 'S'

@pytest.mark.test_id(6)
def test_state_output_sunk():
    x_obj = Cell()
    x_obj.state = SUNK
    assert x_obj.__str__() == '*'

@pytest.mark.test_id(7)
def test_state_output_miss():
    x_obj = Cell()
    x_obj.state = MISS
    assert x_obj.__str__() == 'M'
