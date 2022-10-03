import pytest

from AAA_Homework4_Python_morseCode import decode
from AAA_HW4_Python_one_hot_encoder import fit_transform


@pytest.mark.parametrize("test_input_morse_code, expected_morse_code", [('... --- ...', 'SOS'),
                                                                        ('- .. .-. . -..', 'TIRED'), ('--..', 'Z')])
def test_decode(test_input_morse_code, expected_morse_code):
    assert decode(test_input_morse_code) == expected_morse_code


@pytest.mark.parametrize("test_input_one_hot, expected_one_hot",
                         [(['A', 'B', 'C', 'D', 'B'],
                           [('A', [0, 0, 0, 1]),
                            ('B', [0, 0, 1, 0]),
                            ('C', [0, 1, 0, 0]),
                            ('D', [1, 0, 0, 0]),
                            ('B', [0, 0, 1, 0])]),

                          ([''], [('', [1])]),
                          (['HI!'], [('HI!', [1])]),

                          (['pot', 'pasta', 'boil', 'again', 'pomodoro', 'pasta', 'pomodoro'],
                           [('pot', [0, 0, 0, 0, 1]),
                            ('pasta', [0, 0, 0, 1, 0]),
                            ('boil', [0, 0, 1, 0, 0]),
                            ('again', [0, 1, 0, 0, 0]),
                            ('pomodoro', [1, 0, 0, 0, 0]),
                            ('pasta', [0, 0, 0, 1, 0]),
                            ('pomodoro', [1, 0, 0, 0, 0])
                            ]
                           )])
def test_fit_transform(test_input_one_hot, expected_one_hot):
    assert fit_transform(test_input_one_hot) == expected_one_hot
