import pytest

from AAA_Homework4_Python_morseCode import decode


@pytest.mark.parametrize("test_input,expected", [('... --- ...', 'SOS'), ('- .. .-. . -..', 'TIRED'), ('--..', 'Z')])
def test_decode(test_input, expected):
    assert decode(test_input) == expected


