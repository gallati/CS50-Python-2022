from plates import is_valid

def test_all_letters():
    assert is_valid("AAAAAA") == False
    assert is_valid("aaaaaa") == False

def test_length():
    assert is_valid("AA77633") == False
    assert is_valid("AS") == False
    assert is_valid("CS500") == True