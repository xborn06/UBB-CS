from board import InvalidMoveException, OutsideValidPositionsException, InvalidPositionException
from computer_strategy import ComputerStrategy
from game import MillGame
class UI:
    def __init__(self, game: MillGame, computer_strategy: ComputerStrategy):
        self.game = game
        self.computer_strategy = computer_strategy

    def print_board(self):
        print(self.game.board)

    @staticmethod
    def menu1():
        while True:
            print("1. First turn")
            print("2. Second turn")
            x = input("Which turn do you want?")
            try:
                x = int(x)
                break
            except ValueError:
                print("Please enter a valid number.")
        return x

    def remove_menu(self, opponent_positions, p: str):
        k = 1
        for opponent_position in opponent_positions:
            print(f"{k}. {opponent_position}")
            k = k + 1
        while True:
            try:
                x = int(input("Which position do you want to remove? "))
                x = opponent_positions[x-1]
                self.game.remove_pieces(p,x)
                break
            except ValueError:
                print("Please enter a valid number.")


    def player_menu(self):
        if self.game.player_stage == 1:
            while True:
                k = 1
                for i in self.game.board.free_positions:
                    print(f"{k}: {i}")
                    k += 1
                try:
                    x = int(input("What position do you choose?"))
                    if x > len(self.game.board.free_positions):
                        print("Please enter a valid number.")
                        continue
                    x = self.game.board.free_positions[x-1]
                    if x in self.game.board.free_positions:
                        self.game.player_move(x)
                        return x
                    else:
                        print("Please enter a valid number.")
                except InvalidPositionException as e:
                    print(e)
                except InvalidMoveException as e:
                    print(e)
                except OutsideValidPositionsException as e:
                    print(e)
                except ValueError as e:
                    print("Please enter a valid number.")
        elif self.game.player_stage == 2:
            try:
                while True:
                    k = 1
                    for i in self.game.player_positions:
                        print(f"{k}: {i}")
                        k += 1
                    try:
                        x = int(input("What piece do you choose?"))
                        if x > len(self.game.player_positions):
                            print("Please enter a valid number.")
                            continue
                    except ValueError as e:
                        print("Please enter a valid number.")
                        continue
                    if x > len(self.game.player_positions):
                        print("Please enter a valid number.")
                        continue
                    x = self.game.player_positions[x - 1]
                    pos_list = []
                    k1 = 1
                    for position in self.game.board.free_positions:
                        row, column = position
                        initial_row , initial_column = x
                        if self.game.board.is_adjacent(row,column,initial_row,initial_column):
                            pos_list.append(position)
                            print(f"{k1}: {position}")
                            k1 += 1
                    if len(pos_list) == 0:
                        print("No valid moves.")
                        continue
                    try:
                        y = int(input("What position do you choose?"))
                        if y > len(pos_list):
                            print("Please enter a valid number.")
                            continue
                    except ValueError as e:
                        print("Please enter a valid number.")
                        continue
                    y = pos_list[y - 1]
                    if y in self.game.board.free_positions:
                        self.game.player_move((x, y))
                        return y
                    else:
                        print("Please enter a valid number.")
            except InvalidPositionException as e:
                print(e)
            except OutsideValidPositionsException as e:
                print(e)
            except InvalidMoveException as e:
                print(e)
        elif self.game.player_stage == 3:
            try:
                while True:
                    k = 1
                    for i in self.game.player_positions:
                        print(f"{k}: {i}")
                        k += 1
                    try:
                        x = int(input("What piece do you choose?"))
                        if x > len(self.game.player_positions):
                            print("Please enter a valid number.")
                            continue
                    except ValueError as e:
                        print("Please enter a valid number.")
                        continue
                    x = self.game.player_positions[x - 1]
                    if x in self.game.player_positions:
                        k1 = 1
                        for i in self.game.board.free_positions:
                            print(f"{k1}: {i}")
                            k1 += 1
                        try:
                            y = int(input("What position do you choose?"))
                            if y > len(self.game.board.free_positions):
                                print("Please enter a valid number.")
                                continue
                        except ValueError as e:
                            print("Please enter a valid number.")
                            continue
                        y = self.game.board.free_positions[y - 1]
                        if y in self.game.board.free_positions:
                            self.game.player_move((x, y))
                            return y
                        else:
                            print("Please enter a valid number.")
                    else:
                        print("Please enter a valid number.")
            except InvalidPositionException as e:
                print(e)
            except OutsideValidPositionsException as e:
                print(e)
            except InvalidMoveException as e:
                print(e)



    def run(self):
        turn = self.menu1()
        self.game.stage = 1
        while True:
            if self.game.stage == 1:
                if self.game.remaining_player_pieces == 0 and self.game.remaining_computer_pieces == 0:
                    self.game.stage = 2
                    self.game.player_stage = 2
                    self.game.computer_stage = 2
            elif self.game.stage == 2:
                if self.game.computer_pieces == 3:
                    self.game.stage = 3
                    self.game.computer_stage = 3
                if self.game.player_pieces == 3:
                    self.game.stage = 3
                    self.game.player_stage = 3
            if turn == 1:
                self.print_board()
                start_pos = self.player_menu()
                row, column = start_pos
                if self.game.board.check_three_in_a_row(row,column,turn):
                    self.print_board()
                    self.remove_menu(self.game.computer_positions,"computer")
                check = self.game.win_check()
                if check == 1:
                    print("You lost!")
                    break
                elif check == 2:
                    print("You won!")
                    break

            elif turn == 2:
                move = self.computer_strategy.best_move(self.game.computer_stage)
                if not move:
                    if self.game.win_check() == 1:
                        self.print_board()
                        print("You lost!")
                        break
                    if self.game.win_check() == 2:
                        self.print_board()
                        print("You won!")
                        break
                    elif self.game.stage > 1:
                        self.print_board()
                        print("Draw")
                        break
                pos = self.game.computer_move(move)
                row, column = pos
                if self.game.board.check_three_in_a_row(row,column,turn):
                    move = self.computer_strategy.evaluate_best_position_to_remove(self.game.player_positions,self.game.computer_positions)
                    self.game.remove_pieces("player",move)
                check = self.game.win_check()
                if check == 1:
                    self.print_board()
                    print("You lost!")
                    break
                elif check == 2:
                    self.print_board()
                    print("You won!")
                    break
                if self.game.stage == 1:
                    if self.game.remaining_player_pieces == 0 and self.game.remaining_computer_pieces == 0:
                        self.game.stage = 2
                        self.game.player_stage = 2
                        self.game.computer_stage = 2
                elif self.game.stage == 2:
                    if self.game.remaining_computer_pieces == 3:
                        self.game.stage = 3
                    if self.game.remaining_computer_pieces == 3:
                        self.game.stage = 3
            if turn == 1:
                turn = 2
            elif turn == 2:
                turn = 1

            if self.game.check_stalemate():
                self.print_board()
                print("Draw")
                break