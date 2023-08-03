# 
# ps2pr3.py - Problem Set 2, Problem 3
#
# More practice writing non-recursive functions
#

#function 1
def len_diff(s1, s2):
    """ return the difference between their lengths as a 
        non-negative number
    """
    value = len(s1) - len(s2)
    if len(s1) < len(s2):
        len_diff = -value
    else:
        len_diff = value
    return len_diff
        
#function 2
def combine(s1, s2, n):
    """ return a new string in which the first n characters
        of s1 are followed by the last n characters
        of s2
    """
    if n < (len(s1) and len(s2)):
        return s1[:n] + s2[-n:]   
    elif n > len(s1):
        return s1[:] + s2[-n:]
    elif n > len(s2):
        return s1[:n] + s2[:]
    else:
        return 0
                       
#function 3
def reverse_last(vals, n):
    """ return a new list in which the last n values
        of vals are reversed and all other values
        from vals remain in their original positions
    """
    if n >= len(vals):
        return vals[::-1]
    else:
        return vals[:-n] + vals[-1:-(n + 1):-1]