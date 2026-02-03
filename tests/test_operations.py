import pytest
from app.operations import addition, division, multiplication, subtraction

def test_addition():
    assert addition(1, 1) == 2

def test_subtraction():
    assert subtraction(1, 1) == 0

def test_multiiplication():
    assert multiplication(1, 1) == 1

def test_division_positive():
    assert division(1, 1) == 1

def test_division_negative():
    """Test division by zero."""
    with pytest.raises(ValueError, match="Division by zero is not allowed."):
        division(1, 0)