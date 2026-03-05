from board import *

class Player:
    def __init__(self, symbol: str, is_human: bool):
       self.symbol = symbol
       self.is_human = is_human

    def get_move(self, board: str, board_obj,  ai=None):
        # remember input is 1-indexed but your board is 0-indexed internally
        # TIP: if computer — just call ai.best_move(), no input needed
        if self.is_human == True: 
            while True:
                human_move = input("Choose a column to place disk using a number displayed above: ")
                
                if human_move.isdigit() == False:
                    print("You did not enter a number, try again")
                
                elif board_obj.checkValidMove(board, int(human_move)) == False:
                    print("Invalid move, choose another column")
        
                else:
                    # mapping 1-index to 0 index by subtracting human move by 1 
                    human_move = int(human_move) - 1
                    return human_move
        else:
            # dont need to import bestMove, we assumme when its passed in that ai has a function called bestMove which it does
            return ai.bestMove(board, board_obj)
            
               

            
if __name__ == "__main__":
    human = Player("X", True)

    board_obj = Board(5, 5, 2)
    board = board_obj.initializeBoard()
    board_obj.printBoard(board)
    
    human_move = human.get_move(board, board_obj)
    board = board_obj.addDisk(board, int(human_move), human.symbol)

    # unpacking tuple to get only board since addDisk retutns:  tempoard, row, col 
    board, row, col = board 
    board_obj.printBoard(board)