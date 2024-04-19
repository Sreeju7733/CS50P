from bank import value


def test_starts_with_hello():
    assert value("hello, world") == 0
    assert value("Hello, everyone") == 0
    assert value("HELLO") == 0

def test_starts_with_h():
    assert value("hi there") == 20
    assert value("Hooray!") == 20
    assert value("hmm...") == 20

def test_starts_neither_hello_nor_h():
    assert value("Good morning") == 100
    assert value("123") == 100

def test_case_insensitivity():
    assert value("HeLlO") == 0
    assert value("hElLo, World!") == 0
    assert value("Hi") == 20
    assert value("HELLO, everyone") == 0
    assert value("gOOd MoRniNg") == 100

def test_input_hello():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("Hello") == 0

def test_input_containing_hello():
    assert value("say hello!") == 100
