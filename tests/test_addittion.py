import pytest
from your_python_script import add


def test_add():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-2, 2) == 0
