import pytest
from fuel import convert, gauge

def test_convert_valid_input():
    assert convert("5/10") == 50

def test_convert_invalid_input():
    with pytest.raises(ValueError):
        convert("5/a")

def test_convert_x_greater_than_y():
    with pytest.raises(ValueError):
        convert("10/5")

def test_convert_y_zero():
    with pytest.raises(ZeroDivisionError):
        convert("5/0")

def test_gauge_less_than_or_equal_to_1():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(0.5) == "E"

def test_gauge_greater_than_or_equal_to_99():
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(99.5) == "F"

def test_gauge_otherwise():
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"
