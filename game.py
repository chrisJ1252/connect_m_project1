from board import Board
from player import Player
from ai import AI

class Game:
    def __init__(self, N, M, H):
        # TIP: H=1 means human first, H=0 means computer first
        # assign symbols here — one player gets 'X', other gets 'O'
        # instantiate Board, both Players, and AI here
        pass

    def run(self):
        # TIP: alternate turns in a loop
        # each iteration: print board → get move → place disk → check win → check draw
        # TIP: track whose turn it is with a simple toggle (current_player = other_player)
        pass

    def announce_winner(self, player):
        pass

    def announce_draw(self):
        pass