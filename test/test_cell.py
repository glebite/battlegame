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
