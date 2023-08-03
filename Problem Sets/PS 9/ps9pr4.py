#
# ps9pr4.py (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four  
#

import random  
from ps9pr3 import *

class AIPlayer(Player):
    """ data type of a AIPlyaer that connect four. """
    
    def __init__(self, checker, tiebreak, lookahead):
        """ constructs a new AIPlayer object."""
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead
        
    def __repr__(self):
        """  returns a string representing an AIPlayer object. """
        return 'Player ' + self.checker + ' (' + self.tiebreak + ', ' + str(self.lookahead) + ')'

    def max_score_column(self, scores):
        """ returns the index of the column with the maximum score. """
        
        max_num = max(scores)
        max_num_index = []
        
        for i in range(len(scores)):
            if scores[i] == max_num:
                max_num_index += [i]
        
        if self.tiebreak == 'LEFT':
            return max_num_index[0]
        elif self.tiebreak == 'RIGHT':
            return max_num_index[-1]
        else:
            return random.choice(max_num_index)
    
    def scores_for(self, b):
        """  takes a Board object b and determines the called AIPlayer‘s 
            scores for the columns in b. """
        
        scores = [1000] * b.width
        
        for col in range(b.width):
            if b.can_add_to(col) == False:
                scores[col] = -1
            elif b.is_win_for(self.checker) == True:
                scores[col] = 100
            elif b.is_win_for(self.opponent_checker()) == True:
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                b.add_checker(self.checker, col)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                opponent_scores = opponent.scores_for(b)
                if max(opponent_scores) == 100:
                    scores[col] = 0
                elif max(opponent_scores) == 0:
                    scores[col] = 100
                else:
                    scores[col] = 50
                
                b.remove_checker(col)
        
        return scores
    
    def next_move(self, b):
        """ return the called AIPlayer‘s judgment of its best possible move, 
            rather than asking the user for the next move, this version of next_move """
        
        self.num_moves += 1
        
        return self.max_score_column(self.scores_for(b))
        
                
        
        