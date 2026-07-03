# PyTest Example

from calculator import *


def test_add():
    assert add(12, 8) == 20


def test_subtract():
    assert subtract(15, 5) == 10


def test_multiply():
    assert multiply(6, 7) == 42


def test_divide():
    assert divide(20, 4) == 5