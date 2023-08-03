# 
# ps4pr2.py - Problem Set 4, Problem 2
#
# Using your conversion functions
#

from ps4pr1 import bin_to_dec
from ps4pr1 import dec_to_bin

# Function 1
def mul_bin(b1, b2):
    """ return the result in the form of a string
        that represents a binary number
    """
    n1 = bin_to_dec(b1)
    n2 = bin_to_dec(b2)
    b = dec_to_bin(n1 * n2)
    return b

# Function 2
def largest_bin(binvals):
    """ return the string in binvals that represents
        the largest binary number
    """
    scored_binarys = [[bin_to_dec(x), x] for x in binvals]
    max_binary = max(scored_binarys)
    return max_binary[1]
    

  
   