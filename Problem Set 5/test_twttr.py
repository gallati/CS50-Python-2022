from twttr import shorten


def test_names():
    assert shorten("David") == "Dvd"
    assert shorten("Aaron") == "rn"
    assert shorten("Nuno Cerviño") == "Nn Crvñ"


def test_sentences():
    assert shorten("Hey, what's up?") == "Hy, wht's p?"
