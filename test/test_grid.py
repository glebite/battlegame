"""
test_grid.py

All tests will be in @pytest markup format.

"""
import pytest
import sys
sys.path.append('../src')
from grid import Grid

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
    assert x_obj.set_grid_position(5, 5, 1) is True

@pytest.mark.test_id(6)
def test_grid_position_values():
    x_obj = Grid()
    x_obj.create_own_grid()
    x_obj.set_grid_position(5, 5, 1)
    assert x_obj.get_grid_position(5, 5) == 1 and x_obj.get_grid_position(5, 4) == 0
    
    
