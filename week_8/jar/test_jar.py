from jar import Jar
import pytest

def test_init():
    jarobj = Jar()


def test_str():
    jarobj = Jar()
    assert str(jarobj) == ""
    jarobj.deposit(1)
    assert str(jarobj) == "🍪"
    jarobj.deposit(11)
    assert str(jarobj) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jarobj = Jar()
    jarobj.deposit(1)
    assert jarobj.size == 1
    with pytest.raises(ValueError):
        jarobj.deposit(20)


def test_withdraw():
    jarobj = Jar()
    jarobj.deposit(4)
    jarobj.withdraw(1)
    assert jarobj.size == 3
    with pytest.raises(ValueError):
        jarobj.withdraw(100)
