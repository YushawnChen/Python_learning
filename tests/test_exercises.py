"""Focused CLI regressions; inputs and random outcomes are deterministic."""
import contextlib
import io
from pathlib import Path
import runpy
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]


def run_exercise(relative_path, inputs):
    output = io.StringIO()
    with patch('builtins.input', side_effect=inputs), contextlib.redirect_stdout(output):
        runpy.run_path(str(ROOT / 'course' / relative_path), run_name='__main__')
    return output.getvalue()


class ExerciseRegressions(unittest.TestCase):
    def test_username_length_boundary(self):
        for name, accepted in [('abcdefghijkl', True), ('abcdefghijklm', False)]:
            with self.subTest(name=name):
                output = run_exercise('01_basics/username_validator.py', [name])
                self.assertEqual('you made it' in output, accepted)

    def test_guess_counter_ignores_invalid_and_out_of_range_input(self):
        with patch('random.randint', return_value=42):
            output = run_exercise('02_collections_games/number_guessing_game.py',
                                  ['oops', '0', '101', '40', '42'])
        self.assertIn('You have tried 2 times.', output)

    def test_first_correct_guess_counts_once(self):
        with patch('random.randint', return_value=42):
            output = run_exercise('02_collections_games/number_guessing_game.py', ['42'])
        self.assertIn('You have tried 1 times.', output)

    def test_quiz_names_the_correct_playwright(self):
        output = run_exercise('02_collections_games/quiz_game.py', ['B', 'C', 'A', 'D'])
        self.assertIn('D.William Shakespeare', output)
        self.assertIn('Your quiz result is: 4', output)

    def test_concession_total_including_repeated_item(self):
        output = run_exercise('02_collections_games/concession_stand.py',
                              ['pizza', 'soda', 'pizza', 'q'])
        self.assertIn('PLN50.67', output)

    def test_empty_concession_cart(self):
        output = run_exercise('02_collections_games/concession_stand.py', ['q'])
        self.assertIn('PLN0.00', output)


if __name__ == '__main__':
    unittest.main()
