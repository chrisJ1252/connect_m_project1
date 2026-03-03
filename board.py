from copy import deepcopy

class Board:
    def __init__(self, cols, rows, win_con):
        self.cols = cols 
        self.rows = rows
        self.win_con = win_con

    def initializeBoard(self):
        
        # Initializing board with empty spaces
        board = []
        for i in range(self.rows):
            board.append([])
            for j in range(self.cols):
                board[i].append(' ')
        return board
    
    def checkValidMove(self, board, col):
        # a column is valid if the TOP cell is still empty
        # also make sure col is within bounds
        if col < 0 or col >= self.cols:
            return False
        return board[0][col] == " "
    
    def getValidColumns(self, board):
        # loop through all columns, return list of cols where checkValidMove is True
        # used by AI to know what moves it can try
        valid = []
        for col in range(self.cols):
            if self.checkValidMove(board, col):
             valid.append(col)
        return valid

    def addDisk(self, board, col, player):
        # TIP: gravity — disk falls to the lowest empty row in that column
        # deepcopy so we don't mutate the original board (important for AI tree search)
        tempBoard = deepcopy(board)
        for row in range(self.rows - 1, -1, -1):
            if tempBoard[row][col] == " ":
                tempBoard[row][col] = player
                return tempBoard, row, col
        return None  # column was full, shouldn't happen if you check validity first

    def checkWin(self, board, player):
        # TIP: check all 4 directions for win_con consecutive pieces
        # 4 directions to check: horizontal, vertical, diagonal /, diagonal \
        # for each cell, look in each direction and count consecutive matches
        
        # HORIZONTAL: for each row, slide a window of size win_con across columns
        for row in range(self.rows):
            # loop self.cols - self.win_con to get the last safest place to start without exceeding board size, and + 1 because range does not include the last number 
            for col in range(self.cols - self.win_con + 1):
                # window builds a list of size win_con horizontally to use to check if one player fills all spaces for a win
                window = [board[row][col + k] for k in range(self.win_con)]
                # if "all" cells equals a player for each cell in our window return True else false
                if all(cell == player for cell in window):
                    return True
        
        # VERTICAL: for each col, slide a window of size win_con down rows
        for col in range(self.cols):
            for row in range(self.rows - self.win_con + 1):
                window = [board[row + k][col] for k in range(self.win_con)]
                if all(cell == player for cell in window):
                    return True
        
        # DIAGONAL \ (top-left to bottom-right)
        for row in range(self.rows - self.win_con + 1):
            for col in range(self.cols - self.win_con + 1):
                window = [board[row + k][col + k] for k in range(self.win_con)]
                if all(cell == player for cell in window):
                    return True
        
        # DIAGONAL / (bottom-left to top-right)
        for row in range(self.win_con - 1, self.rows):
            for col in range(self.cols - self.win_con + 1):
                window = [board[row - k][col + k] for k in range(self.win_con)]
                if all(cell == player for cell in window):
                    return True
        
        return False

    def checkDraw(self, board):
        # simplest version: board is full (no valid moves)
        return len(self.getValidColumns(board)) == 0

    def printBoard(self, board):
        # TIP: print column numbers on top so human knows which col to pick (1-indexed)
        print("  " + "   ".join(str(i + 1) for i in range(self.cols)))
        print("+" + "---+" * self.cols)
        for row in board:
            print("| " + " | ".join(row) + " |")
            print("+" + "---+" * self.cols)