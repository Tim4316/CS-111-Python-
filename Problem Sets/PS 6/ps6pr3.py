# 
# ps6pr3.py - Problem Set 6, Problem 3
#
# Functions that use loops
#

# Function 1
def repeat(s, n):
    """ return a string in which n copies of s 
        have been concatenated together """
    result = ''
    for i in range(n):
        result += s
    return result

# Function 2
def contains(s, c):
    """ return True if it does and False if it does not """
    for i in s:
        if i[0] == c:
            return True
    
    return False

# Function 3
def add(vals1, vals2):
    """ return a new list in which each element is the 
        sum of the elements at the corresponding positions 
        in the original lists """
    result = []
    len_longer = max(len(vals1), len(vals2))
    if len(vals1) > len(vals2):
        vals2 = [0] * (len(vals1) - len(vals2)) + vals2
    else:
        vals1 = [0] * (len(vals2) - len(vals1)) + vals1
    for i in range(len_longer):
        result += [vals1[i] + vals2[i]]
    return result
            
# Function 4
def negate_odds(values):
    """ return the modified list of its odd-valued elements """
    for i in range(len(values)):
        if values[i] % 2 == 1:
            values[i] *= -1