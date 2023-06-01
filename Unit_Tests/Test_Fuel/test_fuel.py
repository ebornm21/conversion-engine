#Unit tests for fuel.py

from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    with pytest.raises(ValueError):
        convert("three/four")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_gauge():
    assert gauge(67) == "67%"
    assert gauge(75) == "75%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
