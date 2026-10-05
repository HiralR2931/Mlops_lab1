import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.calculator import add, subtract, multiply, power, modulo, compound_operation


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(2.5, 0.5) == 3.0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 4) == -4


def test_multiply():
    assert multiply(4, 3) == 12
    assert multiply(-2, 3) == -6
    assert multiply(7, 0) == 0


def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(4, 0.5) == 2.0


def test_modulo():
    assert modulo(10, 3) == 1
    assert modulo(9, 3) == 0


def test_modulo_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        modulo(5, 0)


def test_compound_operation():
    assert compound_operation(2, 3, 4) == 20   # (2 + 3) * 4
    assert compound_operation(-1, 1, 10) == 0


@pytest.mark.parametrize("func", [add, subtract, multiply, power, modulo])
def test_invalid_inputs(func):
    with pytest.raises(ValueError, match="Both inputs must be numbers."):
        func("a", 2)


def test_compound_invalid_input():
    with pytest.raises(ValueError):
        compound_operation("a", 2, 3)
