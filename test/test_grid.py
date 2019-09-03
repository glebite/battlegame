"""
test_server.py

All tests will be in @pytest markup format.

test_status
...
test_last
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
    
