import pytest
from working import convert

def test_convert():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"
    assert convert("12:00 PM to 1:00 PM") == "12:00 to 13:00"
    assert convert("12:00 AM to 6:30 AM") == "00:00 to 06:30"


def test_errors():
    with pytest.raises(ValueError):
        convert("13:30 PM to 2:00 PM")
    with pytest.raises(ValueError):
        convert("11:30 XM to 2:45 PM")
    with pytest.raises(ValueError):
        convert("11:75 AM to 2:45 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM 2:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 to 2:00")
    with pytest.raises(ValueError):
        convert("10 PM to 13:00 AM")
