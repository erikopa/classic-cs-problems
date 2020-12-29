import pytest

from src.fibonacci.fib3 import fib3


def test_fib3_recursion():
    assert fib3(5) == 5
    assert fib3(50) == 12586269025

