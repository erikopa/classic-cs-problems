import pytest

from src.fibonacci.fib1 import fib1


def test_fib1_recursion_depth():
    with pytest.raises(RecursionError):
        fib1(5)
