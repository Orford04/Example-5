"""Docstring."""


import unittest
from hamcrest.core.assert_that import assert_that
from hamcrest.core.core.is_ import is_
from src.sudoku.SudokuFourModel import SudokuFourModel

# https://stackoverflow.com/questions/33555891/make-python-unittest-show-assertionerror-but-no-traceback
__unittest = True


class SudokuFourTest(unittest.TestCase):
    """Docstring."""

    def test_sudoku_four_constructor(self):
        """Docstring."""
        m = SudokuFourModel()
        b = m.board
        lock = m.locked
        assert_that(len(b), is_(4),
                    "Board does not have correct number of rows")
        assert_that(len(b[0]), is_(4),
                    "Board does not have correct number of columns")
        assert_that(len(lock), is_(4),
                    "Locked does not have correct number of rows")
        assert_that(len(lock[0]), is_(4),
                    "Locked does not have correct number of columns")

    def test_sudoku_four_model_load_game(self):
        """Docstring."""
        m = SudokuFourModel()
        b = [
            [1, 0, 0, 0],
            [0, 3, 1, 0],
            [0, 0, 0, 0],
            [2, 0, 0, 4],
        ]
        lock = [
            [True, False, False, False],
            [False, True, True, False],
            [False, False, False, False],
            [True, False, False, True],
        ]
        m.load_game(b, lock)
        b2 = m.board
        l2 = m.locked
        assert_that(b2, is_(b), "Board is not replaced correctly")
        assert_that(l2, is_(lock), "Locked is not replaced correctly")

    def test_sudoku_four_model_check_puzzle_true(self):
        """Docstring."""
        m = SudokuFourModel()
        b2 = [
            [3, 1, 2, 4],
            [4, 2, 1, 3],
            [2, 3, 4, 1],
            [1, 4, 3, 2],
        ]
        l2 = [
            [False, False, False, False],
            [True, False, True, False],
            [False, True, False, False],
            [True, False, True, False],
        ]
        m.load_game(b2, l2)
        assert_that(m.check_puzzle(), is_(True),
                    "Board does not correctly report a solved puzzle")

    def test_sudoku_four_model_check_puzzle_false(self):
        """Docstring."""
        m = SudokuFourModel()
        b2 = [
            [3, 1, 2, 4],
            [4, 2, 1, 3],
            [2, 3, 4, 1],
            [1, 4, 3, 3],
        ]
        l2 = [
            [False, False, False, False],
            [True, False, True, False],
            [False, True, False, False],
            [True, False, True, False],
        ]
        m.load_game(b2, l2)
        assert_that(m.check_puzzle(), is_(False),
                    "Board does not correctly report an unsolved puzzle")

    def test_sudoku_four_model_check_row_true(self):
        """Docstring."""
        m = SudokuFourModel()
        b2 = [
            [3, 1, 2, 4],
            [4, 2, 1, 3],
            [2, 3, 4, 1],
            [1, 4, 3, 2],
        ]
        l2 = [
            [False, False, False, False],
            [True, False, True, False],
            [False, True, False, False],
            [True, False, True, False],
        ]
        m.load_game(b2, l2)
        assert_that(m.check_rows(1), is_(True),
                    "Board does not correctly report a solved row")

    def test_sudoku_four_model_check_row_false(self):
        """Docstring."""
        m = SudokuFourModel()
        b2 = [
            [3, 1, 2, 4],
            [4, 2, 1, 3],
            [2, 3, 4, 1],
            [1, 4, 3, 3],
        ]
        l2 = [
            [False, False, False, False],
            [True, False, True, False],
            [False, True, False, False],
            [True, False, True, False],
        ]
        m.load_game(b2, l2)
        assert_that(m.check_rows(1), is_(False),
                    "Board does not correctly report an unsolved row")

    def test_sudoku_four_model_check_column_true(self):
        """Docstring."""
        m = SudokuFourModel()
        b2 = [
            [3, 1, 2, 4],
            [4, 2, 1, 3],
            [2, 3, 4, 1],
            [1, 4, 3, 2],
        ]
        l2 = [
            [False, False, False, False],
            [True, False, True, False],
            [False, True, False, False],
            [True, False, True, False],
        ]
        m.load_game(b2, l2)
        assert_that(m.check_columns(1), is_(True),
                    "Board does not correctly report a solved column")

    def test_sudoku_four_model_check_column_false(self):
        """Docstring."""
        m = SudokuFourModel()
        b2 = [
            [3, 1, 2, 4],
            [4, 2, 1, 3],
            [2, 3, 4, 1],
            [1, 4, 3, 3],
        ]
        l2 = [
            [False, False, False, False],
            [True, False, True, False],
            [False, True, False, False],
            [True, False, True, False],
        ]
        m.load_game(b2, l2)
        assert_that(m.check_columns(1), is_(False),
                    "Board does not correctly report an unsolved column")

    def test_sudoku_four_model_check_region_true(self):
        """Docstring."""
        m = SudokuFourModel()
        b2 = [
            [3, 1, 2, 4],
            [4, 2, 1, 3],
            [2, 3, 4, 1],
            [1, 4, 3, 2],
        ]
        l2 = [
            [False, False, False, False],
            [True, False, True, False],
            [False, True, False, False],
            [True, False, True, False],
        ]
        m.load_game(b2, l2)
        assert_that(m.check_regions(1), is_(True),
                    "Board does not correctly report a solved region")

    def test_sudoku_four_model_check_region_false(self):
        """Docstring."""
        m = SudokuFourModel()
        b2 = [
            [3, 1, 2, 4],
            [4, 2, 1, 3],
            [2, 3, 4, 1],
            [1, 4, 3, 3],
        ]
        l2 = [
            [False, False, False, False],
            [True, False, True, False],
            [False, True, False, False],
            [True, False, True, False],
        ]
        m.load_game(b2, l2)
        assert_that(m.check_regions(1), is_(False),
                    "Board does not correctly report an unsolved region")
