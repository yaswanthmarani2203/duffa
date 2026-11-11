"""Unit tests for the Calculator class."""

import pytest

from calculator import Calculator


@pytest.fixture
def calculator():
    """Return a Calculator instance for tests."""
    return Calculator()


def test_add(calculator):
    """Check addition."""
    assert calculator.add(10, 5) == 15


def test_subtract(calculator):
    """Check subtraction."""
    assert calculator.subtract(10, 5) == 5


def test_multiply(calculator):
    """Check multiplication."""
    assert calculator.multiply(10, 5) == 50


def test_divide(calculator):
    """Check division."""
    assert calculator.divide(10, 5) == 2


def test_divide_by_zero(calculator):
    """Check division by zero raises ValueError."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator.divide(10, 0)


def test_is_even():
    """Check even and odd values."""
    assert Calculator.is_even(4) is True
    assert Calculator.is_even(5) is False


def test_factorial():
    """Check factorial for zero and a positive integer."""
    assert Calculator.factorial(0) == 1
    assert Calculator.factorial(5) == 120


def test_factorial_negative():
    """Check negative factorial raises ValueError."""
    with pytest.raises(ValueError, match="Negative numbers not allowed"):
        Calculator.factorial(-1)