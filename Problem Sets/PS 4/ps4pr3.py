# 
# ps4pr3.py - Problem Set 4, Problem 3
#
# Functions that process binary numbers
#

# Function 1
def count_evens_rec(binvals):
    if binvals == []:
        return 0
    else:
        count_rest = count_evens_rec(binvals[1:])
        if binvals[0][-1] == '0':
            return 1 + count_rest
        else:
            return count_rest

# Function 2
def count_evens_lc(binvals):
    """ return the number of bitstrings in the list that 
        represent an even number
    """
    scored_evens = [1 for x in binvals if x[-1] == '0']
    return sum(scored_evens)

# Function 3
def add_bitwise(b1, b2):
    """ return the sum of two binary numbers
    """
    if b1 == '' and b2 == '':
        return ''
    elif b1 == '':
        return b2
    elif b2 == '':
        return b1
    else:
        add_bitwise_rest = add_bitwise(b1[:-1], b2[:-1])
        if b1[-1] == '1' and b2[-1] == '1':
            return add_bitwise(add_bitwise_rest, '1') + '0'
        elif b1[-1] == '1' and b2[-1] == '0':
            return add_bitwise_rest + '1'
        elif b1[-1] == '0' and b2[-1] == '1':
            return add_bitwise_rest + '1'
        elif b1[-1] == '0' and b2[-1] == '0':
            return add_bitwise_rest + '0'
       

