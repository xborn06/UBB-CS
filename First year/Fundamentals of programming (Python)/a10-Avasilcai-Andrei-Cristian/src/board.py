from texttable import Texttable
class InvalidMoveException(Exception):
    def __init__(self, message):
        """
        Initialize the InvalidMoveException with a message.

        :param message: The exception message.
        """
        self.message = message

class OutsideValidPositionsException(Exception):
    def __init__(self, message):
        """
        Initialize the OutsideValidPositionsException with a message.

        :param message: The exception message.
        """
        self.message = message

class InvalidPositionException(Exception):
    def __init__(self, message):
        """
        Initialize the InvalidPositionException with a message.

        :param message: The exception message.
        """
        self.message = message

class MillBoard:
    def __init__(self, rows: int = 7, columns: int = 7):
        """
        Initialize the MillBoard with the specified number of rows and columns.

        :param rows: The number of rows in the board.
        :param columns: The number of columns in the board.
        """
        self.__rows = rows
        self.__columns = columns
        self.__data = [['=' for _ in range(columns)] for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                if (i == j or j == rows - i - 1) and i != 3 and j != 3:
                    self.__data[i][j] = 0
                elif (i == 3 or j == 3) and (i != 3 or j != 3):
                    self.__data[i][j] = 0
        self.__free_positions = []
        for i in range(rows):
            for j in range(columns):
                if self.__data[i][j] == 0:
                    self.__free_positions.append((i, j))

    def place(self, row: int, column: int, turn: str):
        """
        Place a piece on the board at the specified position.

        :param row: The row of the position.
        :param column: The column of the position.
        :param turn: The player making the move ("player" or "computer").
        :raises InvalidMoveException: If the move is outside the board.
        :raises OutsideValidPositionsException: If the position is not valid.
        :raises InvalidPositionException: If the position is already occupied.
        """
        if not (0 <= row <= self.__rows) or not (0 <= column <= self.__columns):
            raise InvalidMoveException(f"Move played outside the board ({row},{column})")
        if self.__data[row][column] != 0:
            raise OutsideValidPositionsException(f"Position is not valid ({row},{column})")
        if not (row, column) in self.__free_positions:
            raise InvalidPositionException(f"Position already occupied ({row},{column})")
        if turn == "player":
            self.__data[row][column] = 1
            self.__free_positions.remove((row, column))
        elif turn == "computer":
            self.__data[row][column] = 2
            self.__free_positions.remove((row, column))

    def move(self, row: int, column: int, initial_row: int, initial_column: int):
        """
        Move a piece on the board from the initial position to the new position.

        :param row: The row of the new position.
        :param column: The column of the new position.
        :param initial_row: The row of the initial position.
        :param initial_column: The column of the initial position.
        :raises InvalidMoveException: If the move is outside the board or not adjacent.
        :raises OutsideValidPositionsException: If the position is not valid.
        :raises InvalidPositionException: If the position is already occupied.
        """
        if not (0 <= row <= self.__rows) or not (0 <= column <= self.__columns):
            raise InvalidMoveException(f"Move played outside the board ({row},{column})")
        if self.__data[row][column] != 0:
            raise OutsideValidPositionsException(f"Position is not valid ({row},{column})")
        if self.__data[initial_row][initial_column] != 1 and self.__data[initial_row][initial_column] != 2:
            raise OutsideValidPositionsException(f"Position is not valid ({row},{column})")
        if not (row, column) in self.__free_positions:
            raise InvalidPositionException(f"Position already occupied ({row},{column})")
        if not self.is_adjacent(row, column, initial_row, initial_column):
            raise InvalidMoveException(f"Position is not adjacent ({row},{column})")
        if self.is_adjacent(row, column, initial_row, initial_column):
            self.__data[row][column] = self.__data[initial_row][initial_column]
            self.__data[initial_row][initial_column] = 0
            self.__free_positions.append((initial_row, initial_column))
            self.__free_positions.remove((row, column))

    def free_move(self, row: int, column: int, initial_row: int, initial_column: int):
        """
        Move a piece freely on the board from the initial position to the new position.

        :param row: The row of the new position.
        :param column: The column of the new position.
        :param initial_row: The row of the initial position.
        :param initial_column: The column of the initial position.
        :raises InvalidMoveException: If the move is outside the board.
        :raises OutsideValidPositionsException: If the position is not valid.
        :raises InvalidPositionException: If the position is already occupied.
        """
        if not (0 <= row <= self.__rows) or not (0 <= column <= self.__columns):
            raise InvalidMoveException(f"Move played outside the board ({row},{column})")
        if self.__data[initial_row][initial_column] != 1 and self.__data[initial_row][initial_column] != 2:
            raise OutsideValidPositionsException(f"Position is not valid ({row},{column})")
        if not (row, column) in self.__free_positions:
            raise InvalidPositionException(f"Position already occupied ({row},{column})")
        aux = self.__data[row][column]
        self.__data[row][column] = self.__data[initial_row][initial_column]
        self.__data[initial_row][initial_column] = aux
        self.__free_positions.remove((row, column))
        self.__free_positions.append((initial_row, initial_column))

    def is_adjacent(self, row: int, column: int, initial_row: int, initial_column: int) -> bool:
        """
        Check if the new position is adjacent to the initial position.

        :param row: The row of the new position.
        :param column: The column of the new position.
        :param initial_row: The row of the initial position.
        :param initial_column: The column of the initial position.
        :return: True if the new position is adjacent to the initial position, False otherwise.
        """
        adjacency_map = {
            (0, 0): [(0, 3), (3, 0)],
            (0, 3): [(0, 0), (0, 6), (1, 3)],
            (0, 6): [(0, 3), (3, 6)],
            (1, 1): [(1, 3), (3, 1)],
            (1, 3): [(0, 3), (1, 1), (1, 5), (2, 3)],
            (1, 5): [(1, 3), (3, 5)],
            (2, 2): [(2, 3), (3, 2)],
            (2, 3): [(1, 3), (2, 2), (2, 4)],
            (2, 4): [(2, 3), (3, 4)],
            (3, 0): [(0, 0), (3, 1), (6, 0)],
            (3, 1): [(1, 1), (3, 0), (3, 2), (5, 1)],
            (3, 2): [(2, 2), (3, 1), (4, 2)],
            (3, 4): [(2, 4), (3, 5), (4, 4)],
            (3, 5): [(1, 5), (3, 4), (3, 6), (5, 5)],
            (3, 6): [(0, 6), (3, 5), (6, 6)],
            (4, 2): [(3, 2), (4, 3)],
            (4, 3): [(4, 2), (4, 4), (5, 3)],
            (4, 4): [(3, 4), (4, 3)],
            (5, 1): [(3, 1), (5, 3)],
            (5, 3): [(4, 3), (5, 1), (5, 5), (6, 3)],
            (5, 5): [(3, 5), (5, 3)],
            (6, 0): [(3, 0), (6, 3)],
            (6, 3): [(6, 0), (5, 3), (6, 6)],
            (6, 6): [(3, 6), (6, 3)],
        }
        return (row, column) in adjacency_map.get((initial_row, initial_column), [])

    def check_three_in_a_row(self, row: int, column: int, player: int) -> bool:
        """
        Check if the specified position forms a mill (three in a row) for the given player.

        :param row: The row of the position.
        :param column: The column of the position.
        :param player: The player (1 for player, 2 for computer).
        :return: True if the position forms a mill, False otherwise.
        """
        lines = [
            [(0, 0), (0, 3), (0, 6)],
            [(1, 1), (1, 3), (1, 5)],
            [(2, 2), (2, 3), (2, 4)],
            [(3, 0), (3, 1), (3, 2)],
            [(3, 4), (3, 5), (3, 6)],
            [(4, 2), (4, 3), (4, 4)],
            [(5, 1), (5, 3), (5, 5)],
            [(6, 0), (6, 3), (6, 6)],
            [(0, 0), (3, 0), (6, 0)],
            [(1, 1), (3, 1), (5, 1)],
            [(2, 2), (3, 2), (4, 2)],
            [(0, 3), (1, 3), (2, 3)],
            [(4, 3), (5, 3), (6, 3)],
            [(2, 4), (3, 4), (4, 4)],
            [(1, 5), (3, 5), (5, 5)],
            [(0, 6), (3, 6), (6, 6)]
        ]
        for line in lines:
            if (row, column) in line:
                if all(self.__data[r][c] == player for r, c in line):
                    return True
        return False

    def get_possible_mills(self, row, col):
        """
        Get all possible mills (three in a row) that include the specified position.

        :param row: The row of the position.
        :param col: The column of the position.
        :return: A list of possible mills that include the specified position.
        """
        mill_lines = [
            [(0, 0), (0, 3), (0, 6)],
            [(1, 1), (1, 3), (1, 5)],
            [(2, 2), (2, 3), (2, 4)],
            [(3, 0), (3, 1), (3, 2)],
            [(3, 4), (3, 5), (3, 6)],
            [(4, 2), (4, 3), (4, 4)],
            [(5, 1), (5, 3), (5, 5)],
            [(6, 0), (6, 3), (6, 6)],
            [(0, 0), (3, 0), (6, 0)],
            [(1, 1), (3, 1), (5, 1)],
            [(2, 2), (3, 2), (4, 2)],
            [(0, 3), (1, 3), (2, 3)],
            [(4, 3), (5, 3), (6, 3)],
            [(2, 4), (3, 4), (4, 4)],
            [(1, 5), (3, 5), (5, 5)],
            [(0, 6), (3, 6), (6, 6)]
        ]
        return [line for line in mill_lines if (row, col) in line]

    @property
    def free_positions(self):
        """
        Get the list of free positions on the board.

        :return: The list of free positions.
        """
        return self.__free_positions

    @property
    def data(self):
        """
        Get the board data.

        :return: The board data.
        """
        return self.__data

    def __str__(self):
        """
        Get the string representation of the board.

        :return: The string representation of the board.
        """
        t = Texttable()
        t.header('/' + ''.join(str(i) for i in range(0, self.__columns)))
        for i in range(0, self.__rows):
            t.add_row([i] + self.__data[i])

        return t.draw()

    def __getitem__(self, row, col):
        """
        Get the value at the specified position.

        :param row: The row of the position.
        :param col: The column of the position.
        :return: The value at the specified position.
        """
        return self.__data[row][col]

    def __setitem__(self, position, value):
        """
        Set the value at the specified position.

        :param position: The position as a tuple (row, col).
        :param value: The value to set.
        """
        row, col = position
        self.__data[row][col] = value

    def __iter__(self):
        """
        Iterate over the positions on the board.

        :yield: The (row, col) coordinates of each position.
        """
        for row in range(len(self.__data)):
            for col in range(len(self.__data[row])):
                yield row, col

    def get_position(self, row, col):
        """
        Get the value at the specified position.

        :param row: The row of the position.
        :param col: The column of the position.
        :return: The value at the specified position.
        """
        return self.__data[row][col]

    def get_position_value(self, row, col):
        """
        Get the value at the specified position.

        :param row: The row of the position.
        :param col: The column of the position.
        :return: The value at the specified position.
        """
        return self.__data[row][col]

    def set_position_value(self, row, col, value):
        """
        Set the value at the specified position.

        :param row: The row of the position.
        :param col: The column of the position.
        :param value: The value to set.
        """
        self.__data[row][col] = value

    def get_rows(self):
        """
        Get the number of rows on the board.

        :return: The number of rows.
        """
        return self.__rows

    def get_columns(self):
        """
        Get the number of columns on the board.

        :return: The number of columns.
        """
        return self.__columns