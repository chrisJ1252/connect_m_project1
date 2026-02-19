import numpy as np 

class Board:
    def  __init__(self, cols, rows,win_con):
        """
        :param cols: number of cols user specifies
        :param rows: number of rows user specifies 
        :param win_con: number of consecutive pieces needed to win
        """
        self.cols = cols 
        self.rows = rows
        self.win_con = win_con
    

    def initializeBoard(self):
        board = []
        for i in range(self.rows):
            board.append([])
            for j in range(self.cols):
                board[i].append(' ')
        return board
    
    def checkValidMove(self, col):
        """
        TODO: check if a move is valid 
        """


    def addDisk(self):
        """
        TODO: should allow player to pick a column to drop disk into 
        """
        pass

    def checkWin(self):
        """
        TODO: should check board for a win after player makes a move
        """
        pass

    def printBoard(self, board) -> None:
        """
        
        :param baord: board to print 
        TODO: should print the board in a game format
        """
        for row in board:
            print("| " + " | ".join(map(str, row)) + " |")

            # since there is always 1 "|", then add the length of the row multiplied by 4 
            # because the amount of characters that are constantly added to added a column is 4 meaning one char for space then disk, then space again then a "|"
            print("-" * (1 + len(row) * 4))
if __name__ == "__main__":
    board = Board(10,10,4)
    initboard = board.initializeBoard()
    board.printBoard(initboard)
    