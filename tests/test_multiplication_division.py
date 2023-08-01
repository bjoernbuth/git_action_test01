import pytest
from your_python_script import multiply, divide


def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(0, 0) == 0
    assert multiply(-2, 2) == -4


def test_divide():
    assert divide(6, 3) == 2
    assert divide(0, 1) == 0
    with pytest.raises(ValueError):
        divide(1, 0)
