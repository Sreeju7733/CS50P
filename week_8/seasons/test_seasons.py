from seasons import convert

def test_convert_large_number():
    assert convert(10477) == "Fifteen million, eighty-six thousand, eight hundred eighty minutes"

def test_convert_minutes_to_hours():
    assert convert(120) == "Two hours"

def test_convert_minutes_to_days():
    assert convert(2880) == "Two days and forty-eight minutes"

def test_convert_minutes_to_years():
    assert convert(1051200) == "Two years"

def test_convert_zero_minutes():
    assert convert(0) == "Zero minutes"

def test_convert_negative_minutes():
    assert convert(-100) == "Negative one hundred minutes"

def test_convert_large_negative_minutes():
    assert convert(-1000000) == "Negative one million minutes"

def test_convert_invalid_input_none():
    with pytest.raises(TypeError):
        convert(None)

def test_convert_invalid_input_float():
    with pytest.raises(TypeError):
        convert(123.45)

def test_convert_invalid_input_string():
    with pytest.raises(TypeError):
        convert("123")

def test_convert_invalid_input_list():
    with pytest.raises(TypeError):
        convert([100])

def test_main_exits_with_success(capsys):
    input_values = ['2007-01-26\n', '2007-03-07\n']
    sys.stdin = StringIO(''.join(input_values))

    with pytest.raises(SystemExit) as ex:
        from season import main
        main()

    assert ex.value.code == 0
