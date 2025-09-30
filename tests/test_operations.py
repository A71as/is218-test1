""" this is a doc string """

import pytest

from src.operations import add, divide, multiply, subtract


def test_add():
    """
    - Basic positive numbers
    - Adding opposites should yield zero
    - Identity element for addition
    """
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtract():
    """
    - Subtract smaller from larger
    - Subtracting zero changes nothing
    - Subtracting equal negatives yields zero
    """
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0
    assert subtract(-1, -1) == 0


def test_multiply():
    """
    - Basic multiplication
    - Sign rules for multiplication
    - Zero property of multiplication
    """
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(0, 100) == 0


def test_divide():
    """
    - Basic division
    - Sign rules for division
    - Division by zero should raise ZeroDivisionError
    """
    assert divide(6, 3) == 2
    assert divide(-6, 2) == -3
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
