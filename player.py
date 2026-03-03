from alphaBetaPruning import *
from board import *

class Player:
    def __init__(self, symbol: str, is_human: bool):
       self.symbol = symbol,
       self.is_human = is_human

    def get_move(self, board: str, board_obj,  ai=None):
        # TIP: if human — loop until they give a valid column (handle bad input with try/except)
        # remember input is 1-indexed but your board is 0-indexed internally
        # TIP: if computer — just call ai.best_move(), no input needed
        if self.is_human == True: 

            human_move = input("Choose a column to place disk using a number displayed above: ")
            human_move = int(human_move) - 1

            try: 
                while board_obj.checkValidMove(board, human_move) == False:
                     human_move = input("Not a valid move, please pick another column to add a disk: ")

                return human_move
            except: 
                raise TypeError("You did not input a number")

            
if __name__ == "__main__":
    human = Player("X", True)
    board_obj = Board(5, 5, 2)
    board = board_obj.initializeBoard()
    board_obj.printBoard(board)
    human_move = human.get_move(board, board_obj)
    print(human_move)
    board_obj.addDisk(board, int(human_move), human)
    board_obj.printBoard(board)