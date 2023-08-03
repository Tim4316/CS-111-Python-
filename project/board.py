#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# name: Hyungu Lee
# email: hlee18@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]

import math

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[''] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.
        n = 0
        for r in range(3):
            for c in range(3):
                self.tiles[r][c] += digitstr[n]
                n += 1
                
        for r in range(3):
            for c in range(3):
                if self.tiles[r][c] == '0':
                    self.blank_r = r
                    self.blank_c = c
                    

    ### Add your other method definitions below. ###
    def __repr__(self):
        """ returns a string representation of a Board object. """
        b = ''
        for r in range(3):
            for c in range(3):
                if self.tiles[r][c] != '0':
                    b += str(self.tiles[r][c]) + ' '
                else:
                    b += '_ '
            b += '\n'
        return b
    
    def move_blank(self, direction):
        """ return True or False to indicate whether the requested move was possible. """
        if direction == 'left' or direction == 'right' or direction == 'up' or direction == 'down':
           if direction == 'left' and self.blank_c != 0:
               new_num = self.tiles[self.blank_r][self.blank_c - 1]
               self.tiles[self.blank_r][self.blank_c - 1] = '0'
               self.tiles[self.blank_r][self.blank_c] = new_num
               self.blank_c = self.blank_c - 1
               return True
           elif direction == 'right' and self.blank_c != 2:
               new_num = self.tiles[self.blank_r][self.blank_c + 1]
               self.tiles[self.blank_r][self.blank_c + 1] = '0'
               self.tiles[self.blank_r][self.blank_c] = new_num
               self.blank_c = self.blank_c + 1
               return True
           elif direction == 'up' and self.blank_r != 0:
               new_num = self.tiles[self.blank_r - 1][self.blank_c]
               self.tiles[self.blank_r - 1][self.blank_c] = '0'
               self.tiles[self.blank_r][self.blank_c] = new_num
               self.blank_r = self.blank_r - 1
               return True
           elif direction == 'down' and self.blank_r != 2:
               new_num = self.tiles[self.blank_r + 1][self.blank_c]
               self.tiles[self.blank_r + 1][self.blank_c] = '0'
               self.tiles[self.blank_r][self.blank_c] = new_num
               self.blank_r = self.blank_r + 1
               return True
           else:
               return False
        else:
            return False
        
    def digit_string(self):
        """ returns a string of digits that corresponds to the current contents of the 
            called Board object’s tiles attribute. """
        d = ''
        for r in range(3):
            for c in range(3):
                d += str(self.tiles[r][c])
        
        return d
                    
    def copy(self):
        """ returns a newly-constructed Board object that is a deep copy of the called object 
            (i.e., of the object represented by self). """
        new_board = Board(self.digit_string())
        return new_board
    
    def num_misplaced(self):
        """ returns the number of tiles in the called Board object that are not where they 
            should be in the goal state. """
        GOAL_TILES = '012345678'
        new_board = self.digit_string()
        n = 0
        
        for i in range(8):
            if new_board[i] != GOAL_TILES[i]:
                n += 1
            else:
                n += 0
        return n
    
    def __eq__(self, other):
        """ return True if the called object (self) and the argument (other) have the same values 
            for the tiles attribute, and False otherwise. """
        if self.tiles == other.tiles:
            return True
        else:
            return False
        
    def misplaced_length(self):
        """ returns the sum of the distance between each misplaced tile to the right placement.
            Each row and col has distance of 1
        """    
        GOAL_TILES = [[0, 1, 2],
                      [3, 4, 5],
                      [6, 7, 8]]
        num = 0
        for r in range(3):
            for c in range(3):
                if self.tiles[r][c] != GOAL_TILES[r][c] and self.tiles[r][c] != '0':
                    mis_placed = self.tiles[r][c]
                    for r1 in range(3):
                        for c1 in range(3):
                            if mis_placed == GOAL_TILES[r1][c1]:
                                row_diff = abs(r1 - r)
                                col_diff = abs(c1 - c)
                                length = math.sqrt(row_diff**2 + col_diff**2)
                                
                                num = num + length
        return num
                    
    
    def misplaced_rc(self):
        """ returns a new number as priority. If a number is not at the correct place """
        ans = 0
        
        for r in range(3):
            for c in range (3):
                if self.tiles[r][c] not in GOAL_TILES[r] and self.tiles[r][c] != '0':
                    ans = ans + 1    
                if self.tiles[r][c] != GOAL_TILES[r][c] and self.tiles[r][c] != '0':
                    mis_placed = self.tiles[r][c]
                    if mis_placed not in GOAL_TILES[0][c] \
                        and mis_placed not in GOAL_TILES[1][c] \
                            and mis_placed not in GOAL_TILES[2][c]:
                        ans = ans + 1                

        return ans

                
        
                    
                    
                
                
        
        
            
        
    
    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                      
                
                