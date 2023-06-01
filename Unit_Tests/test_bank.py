#Unit tests for bank.py

from bank import value

def test_good():
    assert value("Hello") == 0
    assert value("Hello there") == 0

def test_partial():
    assert value("Hi") == 20
    assert value("Hey") == 20

def test_bad():
    assert value("Welcome") == 100
    assert value("Greetings") == 100
