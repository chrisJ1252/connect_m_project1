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
            try: 
                player_move = input("Choose a column to place disk: ")
                while board_obj.checkValidMove(board, int(player_move)) == False:
                    player_move = input("Column is full, please pick another column to add a disk")

            except: 
                raise TypeError
        return player_move

            
if __name__ == "__main__":
    human = Player("X", True)
    board_obj = Board(5, 5, 2)
    board = board_obj.initializeBoard()
    board_obj.printBoard(board)
    human_move = human.get_move(board, board_obj=board_obj)
    board_obj.addDisk(board, human_move, human)