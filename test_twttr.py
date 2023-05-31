#Unit tests for twttr.py

from twttr import shorten

def test_shorten():
    assert shorten("Hello") == "Hll"
    assert shorten("Good morning") == "Gd mrnng"
    assert shorten("My name is Megan") == "My nm s Mgn"
    assert shorten("Open house") == "pn hs"
    assert shorten("Hello 50") == "Hll 50"
    assert shorten("cs50.com") == "cs50.cm"