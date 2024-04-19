import pytest
from um import count


def test():
    assert count("Um, thanks for the album.") == 1
    assert count("Um um um um") == 4
    assert count("um") == 1
    assert count("Um um um") == 3
    assert count("Um, thanks, um...") == 2
    assert count("Um?") == 1
    assert count("Um um um um um") == 5
