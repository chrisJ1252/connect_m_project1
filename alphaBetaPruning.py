import math

class AI:
    def __init__(self, comp_symbol, human_symbol, win_con):
        # TIP: store both symbols so you know who's who during tree search
        # also set a depth limit here — start with 5, lower it if large boards are slow
        pass

    def best_move(self, board, board_obj):
        # TIP: entry point for the computer's turn
        # try every valid column, run alpha_beta on each result, return the col with best score
        pass

    def alpha_beta(self, board, depth, alpha, beta, maximizing, board_obj):
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

    def evaluate_board(self, board, board_obj):
        # TIP: called when depth runs out and no winner yet
        # score every window of size win_con in all 4 directions (same loop structure as checkWin)
        # add up score_window() results for each window
        # TIP: also reward center column control — center pieces are statistically more valuable
        pass

    def score_window(self, window):
        # TIP: window is a list of win_con cells
        # count how many are comp, human, or empty
        # if the window has BOTH comp and human pieces, return 0 — neither can win there
        # otherwise reward comp pieces and penalize human pieces
        # TIP: more pieces in a window should score exponentially more, not linearly
        pass