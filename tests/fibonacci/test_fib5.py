import pytest

from src.fibonacci.fib5 import fib5


def test_fib5_iterative():
    assert fib5(5) == 5
    assert fib5(50) == 12586269025
