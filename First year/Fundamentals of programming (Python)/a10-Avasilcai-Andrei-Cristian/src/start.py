from src.ui import UI
from src.game import MillGame
from src.board import MillBoard
from src.computer_strategy import ComputerStrategy

def main():
    board = MillBoard()
    game = MillGame(board,1)
    computer_strategy = ComputerStrategy(game)
    ui = UI(game, computer_strategy)
    ui.run()



if __name__ == '__main__':
    main()
