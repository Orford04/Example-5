"""Sample Main Project File.

This file is executed when the entire src directory is run using Python
and serves as the main entry point for the application.

Usage:
    python3 -m src - execute this program (when run from project root).

Author: Russell Feldhausen russfeld@ksu.edu
Version: 0.1
"""

import sys
# sys.path.append("/home/codio/workspace/python/")
from src.tictactoe.TicTacToe import TicTacToe
# from src.sudoku.SudokuFourModel import SudokuFourModel
TicTacToe.main(sys.argv)
# SudokuFourModel.main(sys.argv)
