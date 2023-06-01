#Unit tests for seasons.py

from seasons import convert

def test_convert():
    assert convert("2022-01-04") == "Five hundred twenty-five thousand, six hundred minutes"
