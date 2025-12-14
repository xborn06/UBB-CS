import random


class ComputerStrategy:
    def __init__(self, game):
        """
        Initialize the ComputerStrategy with the game instance.

        :param game: The game instance containing the board and game state.
        """
        self.game = game

    def best_move(self, stage):
        """
        Determine the best move for the computer player based on the current stage of the game.

        :param stage: The current stage of the game (1, 2, or 3).
        :return: The best move for the computer player.
        """
        if stage == 1:
            return self.placement_phase()
        elif stage == 2:
            return self.moving_phase()
        elif stage == 3:
            return self.flying_phase()

    def placement_phase(self):
        """
        Determine the best position to place a piece during the placement phase.

        :return: The best position to place a piece.
        """
        for position in self.game.board.free_positions:
            row, col = position
            if self.blocks_first_mill_attempt(row, col):
                return position
        for position in self.game.board.free_positions:
            row, col = position
            if self.would_create_mill(row, col, "computer"):
                return position
        strategic_positions = [
            (0, 0), (0, 6), (6, 0), (6, 6),
            (3, 0), (3, 6), (0, 3), (6, 3)
        ]
        available_strategic_positions = [pos for pos in strategic_positions if pos in self.game.board.free_positions]
        if available_strategic_positions:
            return random.choice(available_strategic_positions)
        return random.choice(self.game.board.free_positions)

    def blocks_first_mill_attempt(self, row, col):
        """
        Check if placing a piece at the given position blocks the opponent's first mill attempt.

        :param row: The row of the position.
        :param col: The column of the position.
        :return: True if it blocks the opponent's first mill attempt, False otherwise.
        """
        original_value = self.game.board.get_position_value(row, col)
        self.game.board.set_position_value(row, col, 1)
        player_mill_threat = any(
            all(self.game.board.get_position_value(r, c) == 1 for r, c in line if (r, c) != (row, col))
            for line in self.game.board.get_possible_mills(row, col)
        )
        self.game.board.set_position_value(row, col, original_value)
        return player_mill_threat

    def would_create_mill(self, row, col, player):
        """
        Check if placing a piece at the given position would create a mill for the specified player.

        :param row: The row of the position.
        :param col: The column of the position.
        :param player: The player ("computer" or "player").
        :return: True if it would create a mill, False otherwise.
        """
        value = 2 if player == "computer" else 1
        original_value = self.game.board.get_position_value(row, col)
        self.game.board.set_position_value(row, col, value)

        mill_created = any(
            all(self.game.board.get_position_value(r, c) == value for r, c in line)
            for line in self.game.board.get_possible_mills(row, col)
        )

        self.game.board.set_position_value(row, col, original_value)
        return mill_created

    def moving_phase(self):
        """
        Determine the best move during the moving phase.

        :return: A tuple containing the best position to move to and the piece to move.
        """
        best_move = None
        best_score = -float('inf')

        for piece in self.game.computer_positions:
            initial_row, initial_column = piece
            for position in self.game.board.free_positions:
                row, column = position
                if self.game.board.is_adjacent(initial_row, initial_column, row, column):
                    new_positions = self.game.computer_positions.copy()
                    new_positions.remove(piece)
                    new_positions.append(position)
                    score = self.evaluate_position_impact(position, self.game.player_positions, new_positions)
                    if score > best_score:
                        best_score = score
                        best_move = (piece, position)

        return best_move

    def flying_phase(self):
        """
        Determine the best move during the flying phase.

        :return: A tuple containing the piece to move and the best position to move to.
        """
        best_move = None
        best_score = -float('inf')
        for piece in self.game.computer_positions:
            for position in self.game.board.free_positions:
                new_positions = self.game.computer_positions.copy()
                new_positions.remove(piece)
                new_positions.append(position)
                score = self.evaluate_position_impact(position, self.game.player_positions, new_positions)
                if score > best_score:
                    best_score = score
                    best_move = (piece, position)
        return best_move

    def creates_mill(self, position):
        """
        Check if placing a piece at the given position creates a mill for the computer.

        :param position: The position to check.
        :return: True if it creates a mill, False otherwise.
        """
        row, column = position
        return self.game.board.check_three_in_a_row(row, column, 2)

    def evaluate_position(self, computer_positions, player_positions):
        """
        Evaluate the current position of the board.

        :param computer_positions: The positions of the computer's pieces.
        :param player_positions: The positions of the player's pieces.
        :return: The evaluation score of the position.
        """
        computer_mills = sum(
            self.creates_mill(pos) for pos in computer_positions
        )
        player_mills = sum(
            self.creates_mill(pos) for pos in player_positions
        )
        return computer_mills - player_mills

    def evaluate_best_position_to_remove(self, player_positions, computer_positions):
        """
        Evaluate the best position to remove from the player's pieces.

        :param player_positions: The positions of the player's pieces.
        :param computer_positions: The positions of the computer's pieces.
        :return: The best position to remove.
        """
        best_position = None
        min_value = float('inf')
        for position in player_positions:
            row, column = position
            if not self.game.board.check_three_in_a_row(row, column, 1):
                value = self.evaluate_position_impact(position, player_positions, computer_positions)
                if value < min_value:
                    best_position = position
                    min_value = value

        if best_position is None:
            for position in player_positions:
                row, column = position
                value = self.evaluate_position_impact(position, player_positions, computer_positions)
                if value < min_value:
                    best_position = position
                    min_value = value

        return best_position

    def evaluate_position_impact(self, position, player_positions, computer_positions):
        """
        Evaluate the impact of a position on the game state.

        :param position: The position to evaluate.
        :param player_positions: The positions of the player's pieces.
        :param computer_positions: The positions of the computer's pieces.
        :return: The impact score of the position.
        """
        row, col = position
        impact = 0
        value = 2

        original_value = self.game.board.get_position_value(row, col)
        self.game.board.set_position_value(row, col, 0)

        reformable = False
        for line in self.game.board.get_possible_mills(row, col):
            empty_spots = [(r, c) for r, c in line if self.game.board.get_position_value(r, c) == 0]
            if len(empty_spots) == 1:
                r, c = empty_spots[0]
                if all(self.game.board.get_position_value(r, c) in [0, value] for r, c in line):
                    reformable = True
                    break

        self.game.board.set_position_value(row, col, original_value)

        if reformable:
            impact += 100

        if (row, col) in [(0, 0), (0, 6), (6, 0), (6, 6), (3, 3)]:
            impact -= 1

        for adj_row in range(self.game.board.get_rows()):
            for adj_col in range(self.game.board.get_columns()):
                if self.game.board.is_adjacent(row, col, adj_row, adj_col):
                    if (adj_row, adj_col) in player_positions:
                        impact -= 2

        for line in self.game.board.get_possible_mills(row, col):
            if all(self.game.board.get_position_value(r, c) in [0, 1] for r, c in line):
                impact += 3

        for adj_row in range(self.game.board.get_rows()):
            for adj_col in range(self.game.board.get_columns()):
                if self.game.board.is_adjacent(row, col, adj_row, adj_col):
                    if (adj_row, adj_col) in computer_positions:
                        impact += 1

        for line in self.game.board.get_possible_mills(row, col):
            if all(self.game.board.get_position_value(r, c) in [0, value] for r, c in line):
                impact += 2

        return impact