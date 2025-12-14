
from board import InvalidMoveException, OutsideValidPositionsException, InvalidPositionException, MillBoard
class MillGame:
    def __init__(self, game_board: MillBoard, game_stage):
        """
        Initialize the MillGame with the game board and game stage.

        :param game_board: The game board instance.
        :param game_stage: The current stage of the game.
        """
        self.board = game_board
        self.stage = game_stage
        self.remaining_player_pieces = 9
        self.player_pieces = 0
        self.remaining_computer_pieces = 9
        self.computer_pieces = 0
        self.player_positions = []
        self.computer_positions = []
        self.player_stage = 1
        self.computer_stage = 1

    def check_stalemate(self):
        """
        Check if the game is in a stalemate.

        :return: True if the game is in a stalemate, False otherwise.
        """
        if not self.count_adjacent_free_positions("player") and not self.count_adjacent_free_positions("computer"):
            return True
        return False

    def count_adjacent_free_positions(self, pc: str):
        """
        Count the number of adjacent free positions for the specified player or computer.

        :param pc: The player or computer ("player" or "computer").
        :return: The number of adjacent free positions.
        :raises ValueError: If the pc argument is not "player" or "computer".
        """
        count = 0
        if pc == "player":
            pieces = self.player_positions
        elif pc == "computer":
            pieces = self.computer_positions
        else:
            raise ValueError("Invalid argument: pc should be 'player' or 'computer'")

        for piece in pieces:
            row, column = piece
            for position in self.board.free_positions:
                free_row, free_column = position
                if self.board.is_adjacent(row, column, free_row, free_column):
                    count += 1
        return count

    def win_check(self):
        """
        Check if there is a winner in the game.

        :return: 1 if the player wins, 2 if the computer wins, 0 if there is no winner.
        """
        if self.stage > 1:
            if self.player_pieces <= 2:
                return 1
            if self.computer_pieces <= 2:
                return 2
            if self.count_adjacent_free_positions("player") == 0 and self.player_pieces > 2:
                return 1
            if self.count_adjacent_free_positions("computer") == 0 and self.computer_pieces > 2:
                return 2
        return 0

    def remove_pieces(self, pc: str, chosen):
        """
        Remove a piece from the specified player or computer.

        :param pc: The player or computer ("player" or "computer").
        :param chosen: The position of the piece to remove.
        :raises ValueError: If the chosen position is not found in the player's or computer's positions.
        """
        if pc == "computer":
            if chosen in self.computer_positions:
                index = self.computer_positions.index(chosen)
                removed_element = self.computer_positions.pop(index)
                row, column = removed_element
                self.board.data[row][column] = 0
                self.board.free_positions.append((row, column))
                self.computer_pieces = self.computer_pieces - 1
            else:
                raise ValueError(f"Position {chosen} not found in computer positions.")
        elif pc == "player":
            if chosen in self.player_positions:
                index = self.player_positions.index(chosen)
                removed_element = self.player_positions.pop(index)
                row, column = removed_element
                self.board.data[row][column] = 0
                self.board.free_positions.append((row, column))
                self.player_pieces = self.player_pieces - 1
            else:
                raise ValueError(f"Position {chosen} not found in player positions.")

    def computer_move(self, move):
        """
        Execute a move for the computer.

        :param move: The move to execute.
        :return: The move if successful, or an exception if the move is invalid.
        """
        if self.computer_stage == 1:
            try:
                row, column = move
                self.board.place(row, column, "computer")
                self.computer_positions.append((row, column))
                self.remaining_computer_pieces -= 1
                self.computer_pieces += 1
                return move
            except (OutsideValidPositionsException, InvalidMoveException, InvalidPositionException) as e:
                return e
        elif self.computer_stage == 2:
            try:
                old, new = move
                initial_row, initial_column = old
                row, column = new
                if (initial_row, initial_column) in self.computer_positions:
                    self.board.move(row, column, initial_row, initial_column)
                    self.computer_positions.append((row, column))
                    self.computer_positions.remove((initial_row, initial_column))
                    return (row, column)
                else:
                    raise ValueError(f"Position {old} not found in computer positions.")
            except (OutsideValidPositionsException, InvalidMoveException, InvalidPositionException) as e:
                return e
        elif self.computer_stage == 3:
            try:
                old, new = move
                initial_row, initial_column = old
                row, column = new
                if (initial_row, initial_column) in self.computer_positions:
                    self.board.free_move(row, column, initial_row, initial_column)
                    self.computer_positions.append((row, column))
                    self.computer_positions.remove((initial_row, initial_column))
                    return (row, column)
                else:
                    raise ValueError(f"Position {old} not found in computer positions.")
            except (OutsideValidPositionsException, InvalidMoveException, InvalidPositionException) as e:
                return e

    def player_move(self, move):
        """
        Execute a move for the player.

        :param move: The move to execute.
        :return: None if successful, or an exception if the move is invalid.
        """
        if self.player_stage == 1:
            try:
                row, column = move
                self.board.place(row, column, "player")
                self.player_positions.append((row, column))
                self.remaining_player_pieces -= 1
                self.player_pieces += 1
            except (OutsideValidPositionsException, InvalidMoveException, InvalidPositionException) as e:
                return e
        elif self.player_stage == 2:
            try:
                old, new = move
                initial_row, initial_column = old
                row, column = new
                if (initial_row, initial_column) in self.player_positions:
                    self.board.move(row, column, initial_row, initial_column)
                    self.player_positions.append((row, column))
                    self.player_positions.remove((initial_row, initial_column))
                else:
                    raise ValueError(f"Position {old} not found in player positions.")
            except (OutsideValidPositionsException, InvalidMoveException, InvalidPositionException) as e:
                return e
        elif self.player_stage == 3:
            try:
                old, new = move
                initial_row, initial_column = old
                row, column = new
                if (initial_row, initial_column) in self.player_positions:
                    self.board.free_move(row, column, initial_row, initial_column)
                    self.player_positions.append((row, column))
                    self.player_positions.remove((initial_row, initial_column))
                else:
                    raise ValueError(f"Position {old} not found in player positions.")
            except (OutsideValidPositionsException, InvalidMoveException, InvalidPositionException) as e:
                return e

    @property
    def board(self):
        """
        Get the game board.

        :return: The game board instance.
        """
        return self.__board

    @property
    def stage(self):
        """
        Get the current stage of the game.

        :return: The current stage of the game.
        """
        return self.__stage

    @board.setter
    def board(self, new_board):
        """
        Set a new game board.

        :param new_board: The new game board instance.
        """
        self.__board = new_board

    @stage.setter
    def stage(self, new_stage):
        """
        Set a new stage for the game.

        :param new_stage: The new stage of the game.
        """
        self.__stage = new_stage