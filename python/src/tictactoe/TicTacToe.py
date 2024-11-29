"""Docstring."""

from typing import List, TextIO
import sys


class TicTacToe:
    """Docstring."""

    @staticmethod
    def main(args: List[str]) -> None:
        """Docstring."""
        # If an argument is present, we are reading from a file
        # specified in sys.argv[1]
        if len(args) > 1:
            reader: TextIO = open(args[1])

        # If no argument, read from stdin
        else:
            reader = sys.stdin

        # -=-=-=-=- DO NOT MODIFY THE CODE ABOVE -=-=-=-=- #

        # -=-=-=-=- YOUR CODE STARTS HERE -=-=-=-=- #

        # Variable declarations
        # Read board dimensions from input
        # Create board array and fill with default values
        # Initialize the current player and symbol

        m: int = int(reader.readline())
        n: int = int(reader.readline())

        array: List[List[int]] = []
        for i in range(0, m):
            array.append([])
            for j in range(0, n):
                array[i].append(-1)

        player: int = 0

        remaining: int = m * n

        # Loop to read next lines of input
        # You may modify this condition as desired
        while True:

            # Print the move (you will remove this line)
            # print(inputString)

            x: int = int(reader.readline())
            y: int = int(reader.readline())

            # Check if that square is empty
            # Output an invalid move message if so

            if array[x][y] != -1:
                print("Invalid move at " + str(x) + " " + str(y))
            else:

                # Fill that square with the player's symbol

                array[x][y] = player
                remaining -= 1

                # Determine if that was a winning move
                # Output a winning move message if so
                # and terminate the program

                row: bool = True
                for i in range(0, m):
                    if array[i][y] != player:
                        row = False
                        break

                column: bool = True
                for i in range(0, n):
                    if array[x][i] != player:
                        column = False
                        break

                diagonal1: bool = False
                diagonal2: bool = False
                if m == n:
                    diagonal1 = True
                    diagonal2 = True

                    for i in range(0, m):
                        if array[i][i] != player:
                            diagonal1 = False
                        if array[i][i] != player:
                            diagonal2 = False
                        if not diagonal1 and not diagonal2:
                            break

                if row or column or diagonal1 or diagonal2:
                    print("Winning move at " + str(x) + " " + str(y))
                    break

                # Determine if that move filled the board
                # Output a draw message if so
                # and terminate the program

                if remaining <= 0:
                    print("Draw at " + str(x) + " " + str(y))
                    break

            # Switch to the next player's turn and
            # read the next input

            player = (player + 1)
