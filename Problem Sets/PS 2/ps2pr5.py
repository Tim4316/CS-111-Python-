# 
# ps2pr5.py - Problem Set 2, Problem 5
#
# Problem 5: Fun with recursion, part 2
#

# function 1
def add(vals1, vals2):
    """ returns a new list in which each element is
        the sum of the elements at the corresponding
        positions in the original lists
    """
    if vals1 == [] or vals2 == []:
        return []
    else:
        add_in_rest = add(vals1[1:], vals2[1:])
        if len(vals1) != len(vals2):
            return []
        else:
            return [vals1[0] + vals2[0]] + add_in_rest

# funtion 2 
def contains(s,c):
    """ returns true or false using recursion to 
        determine if s contains the character c
    """
    if s == '':
        return False
    elif c[0] == s[0]:
         return True
    else:
        rest_contains = contains(s[1:], c[0])
        if s[0] == c[0]:
            return True
        else: 
            return rest_contains

# function 3
def process(vals):
    """ return a new list in which each even element
        of the original list has been tripled and each
        odd element has been left unchanged using recursion
    """
    if vals == []:
        return []
    else:
        rest_in_process = process(vals[1:])
        if vals[0] % 2 == 0:
            return [vals[0] * 3] + rest_in_process
        else:
            return [vals[0]] + rest_in_process
            