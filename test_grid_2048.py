from grid_2048 import *
from pytest import *

def test_create_grid():
    assert create_grid() == [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
