#
# ps3pr4.py (Problem Set 3, Problem 4)
#
# More algorithm design!
#

# fucntion 1
def first_occur(elem, seq):
    """ return the index of the first occurrence of elem in seq
    """
    if seq == '' or seq ==[]:
        return -1
    elif elem == seq[0]:
        return 0
    else:
        first_occur_rest = first_occur(elem, seq[1:])
        if first_occur_rest == -1:
            return -1
        else:
            return 1 + first_occur_rest
        
# function 2
def rem_first(c, s):
    """ return a version of s in wich only the first occurrence
        of has been removed
    """
    if s == '':
        return ''
    elif s[0] == c:
        return s[1:]
    else:
        rem_first_rest = rem_first(c, s[1:])
        return s[0] + rem_first_rest

# function 3
def jscore(s1, s2):
    """ return the Jotto score of s1 compared with s2, the number
        of characters in s1 that are sharefd by s2
    """
    if s1 == '' or s2 == '':
        return 0
    else:
        if s1[0] in s2:
            jscore_rest = jscore(s1[1:], rem_first(s1, s2[1:]))
            return jscore_rest + 1
        else:
            jscore_rest = jscore(s1[1:], s2 )
            return jscore_rest 

# function 4
def negate_last(n, values):
    """ return a version of values in which only the last occurrence
        of n has been negated
    """
    if values == []:
        return []
    elif n == values[-1]:
        return values[:-1] + [-1 * (values[-1])] 
    else:
        negate_last_rest = negate_last(n, values[:-1])
        return negate_last_rest + [values[-1]]
       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        