import math
from board import *
from player import *

class AI:
    def __init__(self, comp_symbol, human_symbol, win_con):
        self.comp_symbol = comp_symbol
        self.human_symbol = human_symbol
        self.win_con = win_con

        # setting depth limit or else tree would go infinitely deep\
        self.depth = 5

    def bestMove(self, board, board_obj):
        # TIP: entry point for the computer's turn
        # try every valid column, run alpha_beta on each result, return the col with best score
        best_score = float('-inf')
        best_col = None

        valid_columns = board_obj.getValidColumns(board)
        for col in valid_columns:
             # deep copy so each column starts from the same board state
             tempBoard = deepcopy(board)
             tempBoard = board_obj.addDisk(tempBoard, col, self.comp_symbol)
             # unpacking addDisk to retrieve only board to pass into alphaBeta
             tempBoard, row, col = tempBoard
            
             new_score = self.alphaBeta(tempBoard, self.depth, float('-inf'), float('inf'), True, board_obj)
             if new_score > best_score:
                 best_score = new_score
                 best_col = col
        return best_col
        

    def alphaBeta(self, board, depth, alpha, beta, maximizing, board_obj):
        # TIP: BASE CASES first — always check these before recursing:
        #   1. computer won → return a large positive number
        #   2. human won → return a large negative number  
        #   3. draw → return 0
        #   4. depth == 0 → return evaluate_board() (your heuristic estimate)
        
        # TIP: maximizing=True means it's the computer's turn (wants highest score)
        # TIP: maximizing=False means it's the human's turn (wants lowest score)
        
        # TIP: PRUNING — if beta <= alpha, break out of the loop early
        # this is the whole point of alpha-beta, you're skipping branches that can't matter
        pass

    def evaluateBoard(self, board, board_obj):
        # TIP: called when depth runs out and no winner yet
        # score every window of size win_con in all 4 directions (same loop structure as checkWin)
        # add up score_window() results for each window
        # TIP: also reward center column control — center pieces are statistically more valuable
        pass

    def scoreWindow(self, window):
        # TIP: window is a list of win_con cells
        # count how many are comp, human, or empty
        # if the window has BOTH comp and human pieces, return 0 — neither can win there
        # otherwise reward comp pieces and penalize human pieces
        # TIP: more pieces in a window should score exponentially more, not linearly
        pass



if __name__ == "__main__":
    board_obj = Board(5,5,3)
    board = board_obj.initializeBoard()
    ai = AI("O", "X", 3)
    ai_player = Player("O", False)
    ai_move = ai_player.get_move(board, board_obj, ai)