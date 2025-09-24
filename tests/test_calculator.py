import pytest
from src.calculator import add

def test_add_integers():
    assert add(2, 3) == 5.0

def test_add_floats():
    assert add(2.5, 3.5) == 6.0

def test_add_mixed():
    assert add(2, 3.5) == 5.5
