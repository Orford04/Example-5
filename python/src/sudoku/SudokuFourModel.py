"""Four Square Sudoku Model.

Author: Russell Feldhausen russfeld@ksu.edu
Version: 0.1
"""
from typing import List


class SudokuFourModel:
    """Four Square Sudoku Model.

    Attributes:
        board:    Sudoku Board. Squares should have values 1 through 4.
                  Squares with value 0 are considered blank.
        locked:   Locked Squares. A True in this array means the corresponding
                  item in the board was part of the original puzzle.
    """

    @staticmethod
    def main(args: List[str]) -> None:
        """Sample main method.

        Args:
            args: the command-line arguments
        """
        m: SudokuFourModel = SudokuFourModel()
        b2: List[List[int]] = [
            [3, 1, 2, 4],
            [4, 2, 1, 3],
            [2, 3, 4, 1],
            [1, 4, 3, 2],
        ]
        l2: List[List[bool]] = [
            [False, False, False, False],
            [True, False, True, False],
            [False, True, False, False],
            [True, False, True, False],
        ]
        m.load_game(b2, l2)
        print(m.check_puzzle())

    def __init__(self) -> None:
        """Construct new model."""
        self.__board = [[0 for i in range(4)] for j in range(4)]
        self.__locked = [[False for i in range(4)] for j in range(4)]

    def load_game(self, board: List[List[int]],
                  locked: List[List[bool]]) -> None:
        """Load a game for testing."""
        self.__board = board
        self.__locked = locked

    @property
    def board(self) -> List[List[int]]:
        """Getter for board."""
        return self.__board

    @property
    def locked(self) -> List[List[bool]]:
        """Getter for locked."""
        return self.__locked

    def check_puzzle(self) -> bool:
        """Check if puzzle is solved.

        Returns: True if solved, else False
        """
        return (self.check_rows(1) and
                self.check_columns(1) and
                self.check_regions(1))

    def check_rows(self, val: int) -> bool:
        """Check if each row contains the given value.

        This method should be called recursively with
        initial value of 1

        Args:
            val: the value to check

        Returns: True if each row of the puzzle contains
                 that value and all subsequent ones, else false.
        """
        if val < 1 or val > 4:
            return False
        for i in range(0, 4):
            found: bool = False
            for j in range(0, 4):
                if self.__board[i][j] == val:
                    found = True
                    break
            if not found:
                return False
        return self.check_rows(val + 1)

    def check_columns(self, val: int) -> bool:
        """Check if each col contains the given value.

        This method should be called recursively with
        initial value of 1

        Args:
            val: the value to check

        Returns: True if each col of the puzzle contains
                 that value and all subsequent ones, else false.
        """
        if val < 1 or val > 4:
            return False
        for i in range(0, 4):
            found: bool = False
            for j in range(0, 4):
                if self.__board[j][i] == val:
                    found = True
                    break
            if not found:
                return False
        return self.check_columns(val + 1)

    def check_regions(self, val: int) -> bool:
        """Check if each region contains the given value.

        This method should be called recursively with
        initial value of 1

        Args:
            val: the value to check

        Returns: True if each region of the puzzle contains
                 that value and all subsequent ones, else false.
        """
        if val < 1 or val > 4:
            return False
        for region in range(0, 4):
            row1: int = 0
            row2: int = 1
            col1: int = 0
            col2: int = 1
            if region == 1 or region == 3:
                col1 = 2
                col2 = 3
            if region == 2 or region == 3:
                row1 = 2
                row2 = 3
            if ((self.__board[row1][col1] == val or
                 self.__board[row1][col2] == val or
                 self.__board[row2][col1] == val or
                 self.__board[row2][col2] == val)):
                continue
            else:
                return False
        return self.check_regions(val + 1)
