#
# ps9pr3.py  (Problem Set 9, Problem 3)
#
# Playing the game 
#   

from ps9pr1 import Board
from ps9pr2 import Player
import random
    
def connect_four(p1, p2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: p1 and p2 are objects representing Connect Four
          players (objects of the class Player or a subclass of Player).
          One player should use 'X' checkers and the other player should
          use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if p1.checker not in 'XO' or p2.checker not in 'XO' \
       or p1.checker == p2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    board = Board(6, 7)
    print(board)
    
    while True:
        if process_move(p1, board) == True:
            return board

        if process_move(p2, board) == True:
            return board
    
def process_move(p, board):
    """ that takes two parameters: a Player object p for the player whose move 
        is being processed, and a Board object b for the board on which the game 
        is being played. """
    print(p.__repr__() + "'s turn")
    col = p.next_move(board)
    board.add_checker(p.checker, col)
    print()
    print(board)
    
    if board.is_win_for(p.checker):
        print(p.__repr__() + ' wins in ' + str(p.num_moves) + 'moves.')
        print('Congratulation!')
        return True
    elif board.is_full():
        print('Its a tie!')
        return True
    else:
        return False
    
class RandomPlayer(Player):
    """ can be used for an unintelligent computer player that chooses at random 
        from the available columns. """
    def next_move(self, b):
        """ overrides (i.e., replaces) the next_move method that is inherited from Player. """       
        self.num_moves += 1
    
        left = []
        for i in range(b.width):
            if b.can_add_to(i) == True:
                left += [i]
    
        Ran = random.choice(left)
        return Ran
        
              

