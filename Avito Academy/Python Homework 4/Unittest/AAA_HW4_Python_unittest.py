from AAA_HW4_Python_one_hot_encoder import fit_transform
import unittest


class TestCountLetters(unittest.TestCase):
    def test_letters(self):
        actual = fit_transform(['A', 'B', 'C', 'D', 'B'])
        expected = [
            ('A', [0, 0, 0, 1]),
            ('B', [0, 0, 1, 0]),
            ('C', [0, 1, 0, 0]),
            ('D', [1, 0, 0, 0]),
            ('B', [0, 0, 1, 0]),
        ]
        self.assertEqual(actual, expected)

    def test_nothing_in(self):
        actual = fit_transform([''])
        expected = [
            ('', [1]),
        ]
        unexpected = ['', [0]]
        self.assertEqual(actual, expected)

    def test_nothing_notin(self):
        actual = fit_transform([''])
        expected = [
            ('', [1]),
        ]
        unexpected = ['', [0]]
        self.assertNotIn(actual, unexpected)

    def test_pasta_pomodoro(self):
        actual = fit_transform(['pot', 'pasta', 'boil', 'again', 'pomodoro', 'pasta', 'pomodoro'])
        expected = [
            ('pot', [0, 0, 0, 0, 1]),
            ('pasta', [0, 0, 0, 1, 0]),
            ('boil', [0, 0, 1, 0, 0]),
            ('again', [0, 1, 0, 0, 0]),
            ('pomodoro', [1, 0, 0, 0, 0]),
            ('pasta', [0, 0, 0, 1, 0]),
            ('pomodoro', [1, 0, 0, 0, 0]),
        ]
        self.assertEqual(actual, expected)
