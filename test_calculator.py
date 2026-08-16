from calculator import add
from calculator import subtract
from calculator import multiply


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply_positive_numbers():
    assert multiply(3, 4) == 12


def test_multiply_by_zero():
    assert multiply(10, 0) == 0


def test_multiply_negative_number():
    assert multiply(-3, 4) == -12


def test_multiply_two_negative_numbers():
    assert multiply(-3, -4) == 12