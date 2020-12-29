import pytest

from src.fibonacci.fib2 import fib2


def test_fib2_recursion():
    assert fib2(5) == 5
    assert fib2(10) == 55

