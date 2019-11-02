"""
test_grid.py

All tests will be in @pytest markup format.

"""
import pytest
import sys
sys.path.append('../src')
from grid import *
from ship_piece import *
from cell import *

@pytest.mark.test_id(1)
def test_grid_creation():
    x_obj = Grid()
    assert x_obj.rows == 10 and x_obj.cols == 10

@pytest.mark.test_id(2)
def test_grid_creation_sizes():
    y_obj = Grid((5, 3))
    assert y_obj.rows == 5 and y_obj.cols == 3   

@pytest.mark.test_id(3)
def test_grid_creation_type():
    y_obj = Grid((5,3))
    assert isinstance(y_obj.create_grid(), list) is True
    
@pytest.mark.test_id(4)
def test_reinstantiation():
    z_obj = Grid((-1, 5))
    try:
        assert isinstance(z_obj.create_grid(), list) is True
    except ValueError as e_exception:
        print("Exception raised as expected: {}".format(e_exception))

@pytest.mark.test_id(5)
def test_grid_positions():
    x_obj = Grid()
    x_obj.create_own_grid()
    cell_obj = Cell()
    assert x_obj.set_grid_position(5, 5, cell_obj) is True

@pytest.mark.test_id(6)
def test_grid_position_values():
    x_obj = Grid()
    x_obj.create_own_grid()
    cell_obj = Cell()
    x_obj.set_grid_position(5, 5, cell_obj)
    assert type(x_obj.get_grid_position(5, 5)) is Cell
    
@pytest.mark.test_id(7)
def test_grid_place_ship_safe_vertical():
    x_obj = Grid()
    x_obj.create_own_grid()
    sp_obj = ShipPiece(2, "submarine")
    assert x_obj.test_place_ship(0, 0, sp_obj, 'vertical') == True
    
@pytest.mark.test_id(8)
def test_grid_place_ship_safe_horizontal():
    x_obj = Grid()
    x_obj.create_own_grid()
    sp_obj = ShipPiece(2, "submarine")
    assert x_obj.test_place_ship(0, 0, sp_obj, 'horizontal') == True

@pytest.mark.test_id(9)
def test_grid_place_ship_invalid_orientation():
    x_obj = Grid()
    x_obj.create_own_grid()
    sp_obj = ShipPiece(2, "submarine")
    try:
        x_obj.test_place_ship(0, 0, sp_obj, "diagonal")
        assert False
    except GridIncorrectOrientationException as orientation_exception:
        assert True

@pytest.mark.test_id(10)
def test_grid_place_ship_invalid_vertical_placement():
    x_obj = Grid()
    x_obj.create_own_grid()
    sp_obj = ShipPiece(12, "submarine")
    try:
        x_obj.test_place_ship(0, 0, sp_obj, "vertical")
        assert False
    except GridVerticalPlacementException as orientation_exception:
        assert True

@pytest.mark.test_id(11)
def test_grid_place_ship_invalid_horizontal_placement():
    x_obj = Grid()
    x_obj.create_own_grid()
    sp_obj = ShipPiece(12, "submarine")
    try:
        x_obj.test_place_ship(0, 0, sp_obj, "horizontal")
        assert False
    except GridHorizontalPlacementException as orientation_exception:
        assert True

@pytest.mark.test_id(12)
def test_grid_place_ship_invalid_seed_placement():
    x_obj = Grid()
    x_obj.create_own_grid()
    sp_obj = ShipPiece(4, "submarine")
    try:
        x_obj.test_place_ship(2, -1, sp_obj, "horizontal")
        assert False
    except GridBadSeedLocationException as orientation_exception:
        assert True
