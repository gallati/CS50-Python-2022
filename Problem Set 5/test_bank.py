from bank import value


def test_capital_letters():
    assert value("Hello") == 0
    assert value("Hi") == 20
    assert value ("Oh") == 100


def test_lowercase():
    assert value("hello") == 0
    assert value("hey") == 20
    assert value("sir") == 100


def test_sentences():
    assert value("Hello sir") == 0
    assert value("Hi, hello!") == 20
    assert value("Oh, hello sir!") == 100
