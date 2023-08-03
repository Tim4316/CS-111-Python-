# 
# ps2pr3.py - Problem Set 2, Problem 3
#
# Fun with recursion, part 1
#

#function 1
def total_len(words):
    """ return the value obtained by adding together 
        the lengths of all of the strings in the list
    """
    if  words == []:
        return 0
    else:
        len_in_rest = total_len(words[1:])
        return len_in_rest + len(words[0])
       
        
#function 2
def exclaim(s):
    """return the string formed by adding an
        exclamation point
    """
    if s == '':
        return ''
    else:
        exclaim_in_rest = exclaim(s[1:])
        return s[0] + "!" +  exclaim_in_rest