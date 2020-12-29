import pytest

from src.fibonacci.fib4 import fib4


def test_fib4_recursion():
    assert fib4(5) == 5
    assert fib4(50) == 12586269025
