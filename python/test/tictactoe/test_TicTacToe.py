"""Test Class for TicTacToe.

Author: Russell Feldhausen russfeld@ksu.edu
Version: 0.1
"""

from src.tictactoe.TicTacToe import TicTacToe


class TestTicTacToe():
    """Test Class for `src.tictactoe.TicTacToe`."""

    def execute(self, file, cap):
        """Docstring."""
        TicTacToe.main(["TicTacToe", "inputs/{}.in".format(file)])
        captured = cap.readouterr()
        with open("inputs/{}.out".format(file)) as infile:
            data = infile.read()
        assert captured.out.strip() == data.strip()

    def test_input1(self, capsys):
        """Docstring."""
        file = "1"
        self.execute(file, capsys)

    def test_input2(self, capsys):
        """Docstring."""
        file = "2"
        self.execute(file, capsys)

    def test_input3(self, capsys):
        """Docstring."""
        file = "3"
        self.execute(file, capsys)

    def test_input4(self, capsys):
        """Docstring."""
        file = "4"
        self.execute(file, capsys)

    def test_inputcol1(self, capsys):
        """Docstring."""
        file = "col1"
        self.execute(file, capsys)

    def test_inputcol2(self, capsys):
        """Docstring."""
        file = "col2"
        self.execute(file, capsys)

    def test_inputcoldraw(self, capsys):
        """Docstring."""
        file = "coldraw"
        self.execute(file, capsys)

    def test_inputdiagdraw(self, capsys):
        """Docstring."""
        file = "diagdraw"
        self.execute(file, capsys)

    def test_inputdowndiag1(self, capsys):
        """Docstring."""
        file = "downdiag1"
        self.execute(file, capsys)

    def test_inputdowndiag2(self, capsys):
        """Docstring."""
        file = "downdiag2"
        self.execute(file, capsys)

    def test_inputdraw1(self, capsys):
        """Docstring."""
        file = "draw1"
        self.execute(file, capsys)

    def test_inputdrawinvalid(self, capsys):
        """Docstring."""
        file = "drawinvalid"
        self.execute(file, capsys)

    def test_inputinvalidwin(self, capsys):
        """Docstring."""
        file = "invalidwin"
        self.execute(file, capsys)

    def test_inputrow1(self, capsys):
        """Docstring."""
        file = "row1"
        self.execute(file, capsys)

    def test_inputrow2(self, capsys):
        """Docstring."""
        file = "row2"
        self.execute(file, capsys)

    def test_inputrowdraw(self, capsys):
        """Docstring."""
        file = "rowdraw"
        self.execute(file, capsys)

    def test_inputtiny(self, capsys):
        """Docstring."""
        file = "tiny"
        self.execute(file, capsys)

    def test_inputupdiag1(self, capsys):
        """Docstring."""
        file = "updiag1"
        self.execute(file, capsys)

    def test_inputupdiag2(self, capsys):
        """Docstring."""
        file = "updiag2"
        self.execute(file, capsys)
