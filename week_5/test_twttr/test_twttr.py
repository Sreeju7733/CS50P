from twttr import shorten

def test_shorten_no_vowels():
    assert shorten("hello") == "hll"

def test_shorten_with_vowels():
    assert shorten("apple") == "ppl"

def test_shorten_empty_string():
    assert shorten("") == ""

def test_shorten_all_vowels():
    assert shorten("AEIOUaeiou") == ""

def test_shorten_mixed_case():
    assert shorten("HeLLo") == "HLL"

def test_shorten_with_numbers_and_symbols():
    assert shorten("hello123!") == "hll123!"

def test_shorten_with_spaces():
    assert shorten("hello world") == "hll wrld"

def test_names():
    assert shorten("Rakshaya") == "Rkshy"
    assert shorten("Sreeju") == "Srj"
