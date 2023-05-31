#Unit tests for project.py.

from unittest import mock
from project import tempconvert
from project import lengthconvert
from project import massconvert
from project import distconvert


@mock.patch("project.input")
def test_tempconvert(mocked_input):
    mocked_input.side_effect = ["C", "0"]
    assert tempconvert() == "32.0 degrees Farenheit"
    mocked_input.side_effect = ["C", "100"]
    assert tempconvert() == "212.0 degrees Farenheit"
    mocked_input.side_effect = ["F", "32"]
    assert tempconvert() == "0.0 degrees Celsius"
    mocked_input.side_effect = ["F", "212"]
    assert tempconvert() == "100.0 degrees Celsius"

@mock.patch("project.input")
def test_lengthconvert(mocked_input):
    mocked_input.side_effect = ["in", "12"]
    assert lengthconvert() == "30.48 cm"
    mocked_input.side_effect = ["in", "1"]
    assert lengthconvert() == "2.54 cm"
    mocked_input.side_effect = ["cm", "10"]
    assert lengthconvert() == "3.937007874015748 inches"
    mocked_input.side_effect = ["cm", "2.54"]
    assert lengthconvert() == "1.0 inches"

@mock.patch("project.input")
def test_massconvert(mocked_input):
    mocked_input.side_effect = ["kg", "100"]
    assert massconvert() == "220.5 pounds"
    mocked_input.side_effect = ["kg", "50"]
    assert massconvert() == "110.25 pounds"
    mocked_input.side_effect = ["lb", "50"]
    assert massconvert() == "22.675736961451246 kilograms"
    mocked_input.side_effect = ["lb", "100"]
    assert massconvert() == "45.35147392290249 kilograms"

@mock.patch("project.input")
def test_distconvert(mocked_input):
    mocked_input.side_effect = ["km", "5"]
    assert distconvert() == "3.106855 miles"
    mocked_input.side_effect = ["km", "10"]
    assert distconvert() == "6.21371 miles"
    mocked_input.side_effect = ["mi", "5"]
    assert distconvert() == "8.046722489462816 kilometers"
    mocked_input.side_effect = ["mi", "10"]
    assert distconvert() == "16.093444978925632 kilometers"